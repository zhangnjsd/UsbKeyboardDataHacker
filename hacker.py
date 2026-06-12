#!/usr/bin/env python
"""USB Keyboard Stream Hacker.

Parse USB HID keyboard reports from pcap files and reconstruct typed keystrokes.
Usable both as a CLI tool and as an importable library.

CLI usage:
    python hacker.py --input capture.pcap
    python hacker.py --input capture.pcap --quiet

Library usage:
    from hacker import parse_pcap_file, process_key

    for timestamp, hid_data in parse_pcap_file("capture.pcap"):
        char = process_key(timestamp, hid_data)
        if char:
            print(char, end="")
"""

import sys
import os
import argparse
import struct
import logging
import datetime

logger = logging.getLogger(__name__)

# ── key mapping -----------------------------------------------------------
try:
    from config import KEY_MAPPINGS as _DEFAULT_KEY_MAPPINGS
except ImportError:
    _DEFAULT_KEY_MAPPINGS = {}

# ── pcap link types -------------------------------------------------------
_LINKTYPE_USB_LINUX         = 189
_LINKTYPE_USB_LINUX_MMAPPED = 220
_LINKTYPE_USB_DARWIN        = 249

# USB pcap header lengths per link type
_USB_HEADER_LENS = {
    _LINKTYPE_USB_LINUX:         48,   # usbmon binary format (64-bit timestamps)
    _LINKTYPE_USB_LINUX_MMAPPED: 64,   # usbmon mmapped format
    _LINKTYPE_USB_DARWIN:        27,   # macOS USB capture
}


def _read_pcap_global_header(f):
    """Return (endian, network_linktype) from pcap global header."""
    data = f.read(24)
    if len(data) < 24:
        raise ValueError("truncated pcap global header")
    magic = struct.unpack('<I', data[0:4])[0]
    if magic == 0xa1b2c3d4:
        endian = '<'
    elif magic == 0xd4c3b2a1:
        endian = '>'
    else:
        raise ValueError(f"unknown pcap magic: 0x{magic:08x}")
    network = struct.unpack(endian + 'I', data[20:24])[0]
    return endian, network


def parse_pcap_file(filepath):
    """Parse a pcap file and yield (timestamp, hid_bytes) for each keyboard report.

    Supports USB pcap captures from Linux (usbmon), macOS, and generic formats.
    Falls back to scapy when available; otherwise uses a built-in binary parser.
    
    Args:
        filepath: Path to the pcap file.
    Yields:
        (float_timestamp, bytes_8byte_hid_report)
    """
    try:
        from scapy.all import rdpcap, Raw
        from scapy.layers.usb import USBpcap
        yield from _parse_with_scapy(filepath, rdpcap, Raw, USBpcap)
        return
    except ImportError:
        pass

    logger.info("scapy not installed – using built-in binary parser")
    yield from _parse_raw(filepath)


def _parse_with_scapy(filepath, rdpcap, Raw, USBpcap):
    """Scapy-based parser (handles all USB link types natively)."""
    for pkt in rdpcap(filepath):
        if USBpcap not in pkt or Raw not in pkt:
            continue
        data = pkt[Raw].load
        if len(data) == 8 and data[1] == 0x00:
            yield float(pkt.time), data


def _parse_raw(filepath):
    """Built-in binary pcap parser (no external dependencies)."""
    with open(filepath, 'rb') as f:
        endian, network = _read_pcap_global_header(f)
        usb_header_len = _USB_HEADER_LENS.get(network)
        
        if usb_header_len is None:
            logger.warning(
                "Unknown USB link type %d – will scan for 8-byte HID data heuristically",
                network,
            )
        
        while True:
            hdr = f.read(16)
            if len(hdr) < 16:
                break
            ts_sec  = struct.unpack(endian + 'I', hdr[0:4])[0]
            ts_usec = struct.unpack(endian + 'I', hdr[4:8])[0]
            incl_len = struct.unpack(endian + 'I', hdr[8:12])[0]
            
            pkt_data = f.read(incl_len)
            if len(pkt_data) < incl_len:
                break
            
            timestamp = ts_sec + ts_usec / 1_000_000.0
            
            if usb_header_len is not None:
                # Known USB format: HID data follows the header
                hid_data = pkt_data[usb_header_len:usb_header_len + 8]
                if len(hid_data) == 8 and hid_data[1] == 0x00:
                    yield timestamp, hid_data
            else:
                # Heuristic: scan for 8-byte HID reports inside the packet
                for offset in range(0, len(pkt_data) - 7):
                    candidate = pkt_data[offset:offset + 8]
                    if candidate[1] == 0x00 and _is_valid_keyboard_report(candidate):
                        yield timestamp, candidate
                        break


def _is_valid_keyboard_report(data):
    """Return True if *data* looks like a genuine 8-byte USB HID keyboard report."""
    if len(data) != 8 or data[1] != 0x00:
        return False
    
    keys = [data[i] for i in range(2, 8)]
    nonzero = [k for k in keys if k != 0x00]
    
    if not nonzero:                     # idle report – no key pressed
        return False
    if len(nonzero) != len(set(nonzero)):  # duplicate key codes = noise
        return False
    if any(k < 0x04 or k > 0x65 for k in nonzero):  # outside keyboard range
        return False
    
    return True


def process_key(timestamp, data, key_mappings=None):
    """Decode an 8-byte USB HID keyboard report into a character string.

    Args:
        timestamp: float Unix timestamp (used for log formatting only).
        data: 8-byte bytes or colon-separated hex str (e.g. "00:00:16:00:00:00:00:00").
        key_mappings: Optional dict overriding the default KEY_MAPPINGS.

    Returns:
        Decoded character string, or None if the report produced no printable output.
    """
    if key_mappings is None:
        key_mappings = _DEFAULT_KEY_MAPPINGS

    # Normalise input to list of 8 ints -----------------------------------
    if isinstance(data, bytes):
        if len(data) != 8:
            return None
        if not _is_valid_keyboard_report(data):
            return None
        items = list(data)
    elif isinstance(data, str):
        items = [int(i, 16) for i in data.split(":")]
        if len(items) != 8:
            return None
    else:
        return None

    modifier = items[0]
    key_code = items[2]

    # Modifier bits (USB HID 1.11 §B.1) ----------------------------------
    left_ctrl   = (modifier >> 0) & 1
    left_shift  = (modifier >> 1) & 1
    left_alt    = (modifier >> 2) & 1
    left_gui    = (modifier >> 3) & 1
    right_ctrl  = (modifier >> 4) & 1
    right_shift = (modifier >> 5) & 1
    right_alt   = (modifier >> 6) & 1
    right_gui   = (modifier >> 7) & 1
    
    shift = left_shift or right_shift

    # Look up key (USB HID Usage Tables §10: Keyboard/Keypad Page) -------
    entry = key_mappings.get(key_code, ("", ""))
    char = entry[1 if shift else 0] if isinstance(entry, (tuple, list)) else entry

    if not char:
        return None

    # Logging -------------------------------------------------------------
    pressed = []
    if left_ctrl:   pressed.append("left_ctrl")
    if left_shift:  pressed.append("left_shift")
    if left_alt:    pressed.append("left_alt")
    if left_gui:    pressed.append("left_gui")
    if right_ctrl:  pressed.append("right_ctrl")
    if right_shift: pressed.append("right_shift")
    if right_alt:   pressed.append("right_alt")
    if right_gui:   pressed.append("right_gui")
    
    ts_fmt = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')
    mod_str = f", modifiers={', '.join(pressed)}" if pressed else ""
    logger.info("time=%s, key=%r%s", ts_fmt, char, mod_str)

    return char


# ── CLI -------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="USB Keyboard Data Hacker – extract keystrokes from USB pcap captures",
    )
    parser.add_argument("--input", required=True, help="Path to input pcap file")
    parser.add_argument(
        "--verbose", "-v",
        action="store_const", const=logging.DEBUG, default=logging.INFO,
        help="Enable debug-level logging",
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_const", const=logging.WARNING, dest="verbose",
        help="Suppress info logging (only warnings & errors)",
    )
    args = parser.parse_args()

    # Only configure logging when running as CLI
    try:
        import coloredlogs
        coloredlogs.install(level=args.verbose, logger=logger)
    except ImportError:
        logging.basicConfig(level=args.verbose, format="%(asctime)s %(name)s %(levelname)s %(message)s")

    if not os.path.exists(args.input):
        logger.error("Input file does not exist: %s", args.input)
        sys.exit(1)

    buffer = []
    for timestamp, press in parse_pcap_file(args.input):
        key = process_key(timestamp, press)
        if key:
            buffer.append(key)
    print("".join(buffer))


if __name__ == "__main__":
    main()