# USB HID Keyboard/Keypad Page (0x07) Mappings
# Based on USB HID Usage Tables 1.12, Section 10: Keyboard/Keypad Page
# Format: { code: (normal, shifted) }

KEY_MAPPINGS = {
    0x00: ("", ""),           # Reserved (no event)
    0x01: ("", ""),           # Keyboard ErrorRollOver
    0x02: ("", ""),           # Keyboard POSTFail
    0x03: ("", ""),           # Keyboard ErrorUndefined
    0x04: ("a", "A"),
    0x05: ("b", "B"),
    0x06: ("c", "C"),
    0x07: ("d", "D"),
    0x08: ("e", "E"),
    0x09: ("f", "F"),
    0x0A: ("g", "G"),
    0x0B: ("h", "H"),
    0x0C: ("i", "I"),
    0x0D: ("j", "J"),
    0x0E: ("k", "K"),
    0x0F: ("l", "L"),
    0x10: ("m", "M"),
    0x11: ("n", "N"),
    0x12: ("o", "O"),
    0x13: ("p", "P"),
    0x14: ("q", "Q"),
    0x15: ("r", "R"),
    0x16: ("s", "S"),
    0x17: ("t", "T"),
    0x18: ("u", "U"),
    0x19: ("v", "V"),
    0x1A: ("w", "W"),
    0x1B: ("x", "X"),
    0x1C: ("y", "Y"),
    0x1D: ("z", "Z"),
    0x1E: ("1", "!"),
    0x1F: ("2", "@"),
    0x20: ("3", "#"),
    0x21: ("4", "$"),
    0x22: ("5", "%"),
    0x23: ("6", "^"),
    0x24: ("7", "&"),
    0x25: ("8", "*"),
    0x26: ("9", "("),
    0x27: ("0", ")"),
    0x28: ("\n", "\n"),       # Enter / Return
    0x29: ("", ""),           # Escape
    0x2A: ("\b", "\b"),       # Backspace / Delete
    0x2B: ("\t", "\t"),       # Tab
    0x2C: (" ", " "),         # Spacebar
    0x2D: ("-", "_"),
    0x2E: ("=", "+"),
    0x2F: ("[", "{"),
    0x30: ("]", "}"),
    0x31: ("\\", "|"),
    0x32: ("#", "~"),         # Non-US # and ~
    0x33: (";", ":"),
    0x34: ("'", '"'),
    0x35: ("`", "~"),
    0x36: (",", "<"),
    0x37: (".", ">"),
    0x38: ("/", "?"),
    0x39: ("", ""),           # Caps Lock
    # F1-F12
    0x3A: ("<F1>", "<F1>"),
    0x3B: ("<F2>", "<F2>"),
    0x3C: ("<F3>", "<F3>"),
    0x3D: ("<F4>", "<F4>"),
    0x3E: ("<F5>", "<F5>"),
    0x3F: ("<F6>", "<F6>"),
    0x40: ("<F7>", "<F7>"),
    0x41: ("<F8>", "<F8>"),
    0x42: ("<F9>", "<F9>"),
    0x43: ("<F10>", "<F10>"),
    0x44: ("<F11>", "<F11>"),
    0x45: ("<F12>", "<F12>"),
    0x46: ("", ""),           # Print Screen
    0x47: ("", ""),           # Scroll Lock
    0x48: ("", ""),           # Pause
    0x49: ("", ""),           # Insert
    0x4A: ("<HOME>", "<HOME>"),
    0x4B: ("<PAGEUP>", "<PAGEUP>"),
    0x4C: ("<DELETE>", "<DELETE>"),
    0x4D: ("<END>", "<END>"),
    0x4E: ("<PAGEDOWN>", "<PAGEDOWN>"),
    0x4F: ("<RIGHT>", "<RIGHT>"),
    0x50: ("<LEFT>", "<LEFT>"),
    0x51: ("<DOWN>", "<DOWN>"),
    0x52: ("<UP>", "<UP>"),
    # Keypad
    0x53: ("", ""),           # Num Lock / Clear
    0x54: ("/", "/"),         # Keypad /
    0x55: ("*", "*"),         # Keypad *
    0x56: ("-", "-"),         # Keypad -
    0x57: ("+", "+"),         # Keypad +
    0x58: ("\n", "\n"),       # Keypad Enter
    0x59: ("1", "1"),         # Keypad 1 / End
    0x5A: ("2", "2"),         # Keypad 2 / Down
    0x5B: ("3", "3"),         # Keypad 3 / PageDn
    0x5C: ("4", "4"),         # Keypad 4 / Left
    0x5D: ("5", "5"),         # Keypad 5
    0x5E: ("6", "6"),         # Keypad 6 / Right
    0x5F: ("7", "7"),         # Keypad 7 / Home
    0x60: ("8", "8"),         # Keypad 8 / Up
    0x61: ("9", "9"),         # Keypad 9 / PageUp
    0x62: ("0", "0"),         # Keypad 0 / Insert
    0x63: (".", "."),         # Keypad . / Delete
    0x64: ("\\", "|"),        # Non-US \ and |
    0x65: ("", ""),           # Keyboard Application
    0x66: ("", ""),           # Keyboard Power (no event)
    0x67: ("=", "="),         # Keypad =
    # F13-F24
    0x68: ("<F13>", "<F13>"),
    0x69: ("<F14>", "<F14>"),
    0x6A: ("<F15>", "<F15>"),
    0x6B: ("<F16>", "<F16>"),
    0x6C: ("<F17>", "<F17>"),
    0x6D: ("<F18>", "<F18>"),
    0x6E: ("<F19>", "<F19>"),
    0x6F: ("<F20>", "<F20>"),
    0x70: ("<F21>", "<F21>"),
    0x71: ("<F22>", "<F22>"),
    0x72: ("<F23>", "<F23>"),
    0x73: ("<F24>", "<F24>"),
    0x74: ("", ""),           # Keyboard Execute
    0x75: ("", ""),           # Keyboard Help
    0x76: ("", ""),           # Keyboard Menu
    0x77: ("", ""),           # Keyboard Select
    0x78: ("", ""),           # Keyboard Stop
    0x79: ("", ""),           # Keyboard Again
    0x7A: ("", ""),           # Keyboard Undo
    0x7B: ("", ""),           # Keyboard Cut
    0x7C: ("", ""),           # Keyboard Copy
    0x7D: ("", ""),           # Keyboard Paste
    0x7E: ("", ""),           # Keyboard Find
    0x7F: ("", ""),           # Keyboard Mute
    0x80: ("", ""),           # Keyboard Volume Up
    0x81: ("", ""),           # Keyboard Volume Down
    0x85: (",", ","),         # Keypad Comma (Brazilian)
    0x87: ("", ""),           # Keyboard International1 (Ro)
    0x88: ("", ""),           # Keyboard International2 (Katakana/Hiragana)
    0x89: ("", ""),           # Keyboard International3 (Yen)
    0x8A: ("", ""),           # Keyboard International4
    0x8B: ("", ""),           # Keyboard International5
    0x8C: ("", ""),           # Keyboard International6
    0x8D: ("", ""),           # Keyboard International7
    0x8E: ("", ""),           # Keyboard International8
    0x8F: ("", ""),           # Keyboard International9
    0x90: ("", ""),           # Keyboard LANG1 (Hangul/English)
    0x91: ("", ""),           # Keyboard LANG2 (Hanja)
    0x92: ("", ""),           # Keyboard LANG3 (Katakana)
    0x93: ("", ""),           # Keyboard LANG4 (Hiragana)
    0x94: ("", ""),           # Keyboard LANG5 (Zenkaku/Hankaku)
    0x95: ("", ""),           # Keyboard LANG6
    0x96: ("", ""),           # Keyboard LANG7
    0x97: ("", ""),           # Keyboard LANG8
    0x98: ("", ""),           # Keyboard LANG9
    0x9B: ("", ""),           # Keyboard Alternate Erase
    0x9C: ("", ""),           # Keyboard SysReq/Attention
    0x9D: ("", ""),           # Keyboard Cancel
    0x9E: ("", ""),           # Keyboard Clear
    0x9F: ("", ""),           # Keyboard Prior
    0xA0: ("", ""),           # Keyboard Return
    0xA1: ("", ""),           # Keyboard Separator
    0xA2: ("", ""),           # Keyboard Out
    0xA3: ("", ""),           # Keyboard Oper
    0xA4: ("", ""),           # Keyboard Clear/Again
    0xA5: ("", ""),           # Keyboard CrSel/Props
    0xA6: ("", ""),           # Keyboard ExSel
    # Reserved range
    0xE0: ("<LEFT_CTRL>", "<LEFT_CTRL>"),
    0xE1: ("<LEFT_SHIFT>", "<LEFT_SHIFT>"),
    0xE2: ("<LEFT_ALT>", "<LEFT_ALT>"),
    0xE3: ("<LEFT_GUI>", "<LEFT_GUI>"),
    0xE4: ("<RIGHT_CTRL>", "<RIGHT_CTRL>"),
    0xE5: ("<RIGHT_SHIFT>", "<RIGHT_SHIFT>"),
    0xE6: ("<RIGHT_ALT>", "<RIGHT_ALT>"),
    0xE7: ("<RIGHT_GUI>", "<RIGHT_GUI>"),
}
