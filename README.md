# Pi Network Monitor

A lightweight, terminal-based network latency monitor designed for Raspberry Pi. This tool helps competitive gamers and power users identify exactly where lag is occurring—whether it's your local Wi-Fi, your ISP, or the game servers themselves.

## 🚀 Features

* **Real-time HUD**: Uses ANSI escape codes to update the dashboard in place without scrolling.
* **Targeted Monitoring**: Pings your local gateway, Google DNS, and League of Legends (NA) servers simultaneously.
* **Color-Coded Status**:
    * 🟢 **Green**: Latency < 40ms (Optimal)
    * 🟡 **Yellow**: Latency 40ms - 100ms (Acceptable)
    * 🔴 **Red**: Latency > 100ms or Packet Loss (Lag)

## 🛠️ Installation

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/ZaviQ7/pi-lag-monitor.git](https://github.com/ZaviQ7/pi-lag-monitor.git)
    cd pi-lag-monitor
    ```

2.  **Set up a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 📈 Usage

Because the script uses raw sockets for high-precision pings, it must be run with `sudo` pointing to the virtual environment's Python:

```bash
sudo ./venv/bin/python monitor.py
```


