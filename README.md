# UsbKeyboardDataHacker

> 复刻自 [UsbKeyboardDataHacker](https://github.com/WangYihang/UsbKeyboardDataHacker)
> Forked from [UsbKeyboardDataHacker](https://github.com/WangYihang/UsbKeyboardDataHacker)

## 更改 Changes

使用 uv 管理依赖，重写了符合更具复用性的代码。

Use uv to manage dependencies and rewrite code for better reusability.

仅用于获得 pcap 文件中的 USB 键盘数据。

Only for obtaining USB keyboard data from pcap files.

## 使用 Usage

```bash
uv sync
python ./hacker.py --input <pcap_file>
```

> For more information, please read `hacker.py` and upstream repository.
