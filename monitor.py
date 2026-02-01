import time
import os
from ping3 import ping
from colorama import Fore, Style, init

# Initialize colors
init()

# ==========================================
# 🎯 TARGETS (The servers we are watching)
# ==========================================
TARGETS = [
    {"name": "ROUTER (Home)", "ip": "192.168.1.254"},  # Your Gateway
    {"name": "ISP (Google)",  "ip": "8.8.8.8"},        # Internet Check
    {"name": "GAME (LoL NA)", "ip": "104.160.131.1"}   # Riot Games Server
]
# ==========================================

print(f"{Style.BRIGHT}--- STARTING LAG MONITOR (Press CTRL+C to stop) ---{Style.RESET_ALL}")
print(f"{'TARGET':<15} | {'PING (ms)':<10} | {'STATUS'}")
print("-" * 40)

try:
    while True:
        # Move cursor up 4 lines to overwrite previous data (creates a "Dashboard" effect)
        print("\033[4A", end="") 

        for target in TARGETS:
            try:
                # Send ping (returns seconds, so we multiply by 1000 for ms)
                latency = ping(target['ip'], timeout=1)
                
                if latency is None:
                    # Packet Loss (Red)
                    color = Fore.RED
                    status_text = "TIMEOUT / LOSS 💀"
                    ms_text = "---"
                else:
                    ms = round(latency * 1000)
                    
                    # Color Logic
                    if ms < 40:
                        color = Fore.GREEN  # Perfect
                    elif ms < 80:
                        color = Fore.YELLOW # Okay
                    else:
                        color = Fore.RED    # LAG SPIKE
                    
                    status_text = "Good" if ms < 80 else "LAG SPIKE"
                    ms_text = f"{ms} ms"

                # Print the row
                print(f"{target['name']:<15} | {color}{ms_text:<10}{Style.RESET_ALL} | {color}{status_text}{Style.RESET_ALL}")
            
            except Exception as e:
                print(f"Error: {e}")

        # Wait 1 second before next check
        print("-" * 40)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopping Monitor.")
