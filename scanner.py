import socket
import sys
from datetime import datetime

def port_scanner(target):
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n [!] Hostname could not be resolved. Invalid IP/Domain.")
        sys.exit()

    print("=" * 50)
    print("      [ 🛡️  Coded by CyberPorza ]")
    print("=" * 50)
    print(f" Scan Started: {ip}")
    print(f" Time: {str(datetime.now())}")
    print("-" * 50)

    common_ports = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 
        53: "DNS", 80: "HTTP", 443: "HTTPS", 3306: "MySQL", 
        3389: "RDP", 8080: "HTTP-Proxy"
    }

    try:
        for port in range(1, 1025): 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            
            result = s.connect_ex((ip, port))
            if result == 0:
                service = common_ports.get(port, "Unknown Service")
                print(f" [+] Port {port} is Open \t [Service: {service}]")
            s.close()

    except KeyboardInterrupt:
        print("\n [!] Process interrupted by user.")
        sys.exit()
    except Exception as e:
        print(f"\n [!] Error: {e}")
        sys.exit()

    print("-" * 50)
    print(" Scan Completed.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_ip = sys.argv[1]
    else:
        target_ip = input("Enter Target IP or Domain: ")
    
    port_scanner(target_ip)
