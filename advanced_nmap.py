import nmap

scanner = nmap.PortScanner()

target = input("Enter Target IP: ")
ports = input("Enter Ports (e.g. 22,80,443): ")

print(f"\n[+] Scanning Target: {target}")

scanner.scan(target, ports)

host = target

print(f"Host: {host}")
print(f"State: {scanner[host].state()}")

for port in ports.split(','):
    port = int(port)
    state = scanner[host]['tcp'][port]['state']
    print(f"Port {port} → {state}")
