# BadUSB Web Simulator (CTF Lab)

🧪 Web-based simulation of BadUSB (Rubber Ducky style) attack flow  
Perfect for CTF challenges, security awareness training, or educational demos.

## 🐳 Quick Start (Docker)

```bash
docker build -t badusb-web .
docker run -d -p 5000:5000 --name badusb-container badusb-web

Access: http://localhost:5000