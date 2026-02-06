import socket

target = input("Enter target IP: ")

ports = [21, 22, 23, 25, 53, 76, 80, 110, 139, 443]

print("\nStarting scan on", target)
print("-" * 40)

for port in ports:
    s = socket.socket()
    s.settimeout(2)

    try:
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} OPEN")

            try:
                banner = s.recv(1024)
                if banner:
                    print(f"    Banner: {banner.decode(errors='ignore').strip()}")
                else:
                    print("    Banner: <no banner>")
            except:
                print("    Banner: <could not grab>")

        else:
            print(f"[-] Port {port} CLOSED")

    except socket.timeout:
        print(f"[!] Port {port} FILTERED (timeout)")

    except Exception as e:
        print(f"[!] Error on port {port}: {e}")

    finally:
        s.close()
