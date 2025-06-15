# BadUSB Web Simulator (CTF Lab)

🧪 Web-based simulation of BadUSB (Rubber Ducky style) attack flow  
Perfect for CTF challenges, security awareness training, or educational demos.

## 🐳 Quick Start (Docker)

```bash
docker build -t badusb-web .
docker run -d -p 5000:5000 --name badusb-container badusb-web

```
Access: http://localhost:5000

## 📄 File Upload Instructions

⚠️ **Only `.ino` files are accepted for upload.**  
The simulator is designed to parse and emulate payloads written in [DuckyScript](https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript) format, typically used in USB HID attacks.

> ❗ Uploading `.txt`, `.py`, or any other file type will be rejected.

### ✅ Accepted Example
```ino
DELAY 1000
GUI r
DELAY 300
STRING calc.exe
ENTER
