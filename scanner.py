import socket
import sys
from datetime import datetime

def scanner():
    green = "\033[1;32m"
    red = "\033[1;31m"
    reset = "\033[0m"
    blue = "\033[1;34m"

    banner = r"""
    ______________________________________________________________
    
       ______      __             ____                      
      / ____/_  __/ /_  ___  ____/ __ \____  _____________ _
     / /   / / / / __ \/ _ \/ __/ /_/ / __ \/ ___/_  / __ `/
    / /___/ /_/ / /_/ /  __/ / / ____/ /_/ / /    / /_/ /_/ 
    \____/\__, /_.___/\___/_/ /_/    \____/_/    /___/\__,_/  
         /____/          [ NetScanner v1.2 ] 🛡️
    ______________________________________________________________
    """
    print(green + banner + reset)
    print(f"{blue}             Powered by CyberPorza{reset}")

    if len(sys.argv) < 2:
        print(red + " [!] Usage: python3 scanner.py <target_ip_or_domain>" + reset)
        print(blue + " Example: python3 scanner.py 192.168.1.1" + reset)
        sys.exit()

    target = sys.argv[1]
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(red + " [!] Error: Could not resolve hostname." + reset)
        sys.exit()

    print("-" * 62)
    print(f"{blue} [*] Scanning Target: {target_ip}")
    print(f" [*] Scan Started: {datetime.now().strftime('%H:%M:%S')}{reset}")
    print("-" * 62)

    ports = {
        21: "FTP", 
        22: "SSH", 
        23: "Telnet", 
        25: "SMTP", 
        53: "DNS", 
        80: "HTTP", 
        110: "POP3",
        443: "HTTPS", 
        3306: "MySQL", 
        8080: "HTTP-Proxy"
    }

    try:
        found_ports = 0
        for port, service in ports.items():
           
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) 
            
            
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"{green} [+] Port {port} ({service}): OPEN{reset}")
                found_ports += 1
            s.close()
            
    except KeyboardInterrupt:
        print(red + "\n [!] Scan interrupted by user (CyberPorza)." + reset)
        sys.exit()
    except socket.error:
        print(red + " [!] Could not connect to server." + reset)
        sys.exit()

    print("-" * 62)
    print(f"{blue} [*] Scan complete. Found {found_ports} open ports.{reset}")
    print("=" * 62)

if __name__ == "__main__":
    scanner()
