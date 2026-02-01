import time
import os
from ping3 import ping
from colorama import Fore, Style, init

init()

TARGETS = [
    {"name": "ROUTER", "ip": "192.168.1.254"},
    {"name": "GOOGLE DNS", "ip": "8.8.8.8"},
    {"name": "LOL (NA)", "ip": "104.160.131.1"}
]

print(f"{Style.BRIGHT}--- NETWORK LAG MONITOR (CTRL+C to quit) ---{Style.RESET_ALL}")
print(f"{'TARGET':<15} | {'PING':<10} | {'STATUS'}")
print("-" * 40)

try:
    while True:
        # Dashboard mode: Move cursor up 4 lines
        print("\033[4A", end="") 

        for target in TARGETS:
            try:
                latency = ping(target['ip'], timeout=1)
                
                if latency is None:
                    color = Fore.RED
                    status_text = "TIMEOUT"
                    ms_text = "---"
                else:
                    ms = round(latency * 1000)
                    if ms < 40:
                        color = Fore.GREEN
                    elif ms < 100:
                        color = Fore.YELLOW
                    else:
                        color = Fore.RED
                    
                    status_text = "Good" if ms < 100 else "LAG"
                    ms_text = f"{ms} ms"

                print(f"{target['name']:<15} | {color}{ms_text:<10}{Style.RESET_ALL} | {color}{status_text:<10}{Style.RESET_ALL}")
            
            except Exception:
                pass

        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitor stopped.")
