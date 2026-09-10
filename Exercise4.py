# Network to scan: 192.168.1.1 to 192.168.1.20
# Your program should:
# 1. Use a for loop with range(1, 21)
# 2. Print "Scanning 192.168.1.X..." for each IP
# 3. For IPs ending in 5, 10, 15: print " → Device found!"
# 4. For IP ending in 13: print " → SUSPICIOUS DEVICE!" and break
# 5. Count total IPs scanned before breaking
def networkscan(network_to_scan: str, range_start: int, range_end: int, device_found: list, suspicious_device: list):
    network_range = range(range_start, range_end)
    # Device_found = [5, 10, 15]
    for scan in network_range:
        print(f"Scanning {network_to_scan}{scan}...")
        if scan in device_found:
            print(f"Device found!")
        elif scan in suspicious_device:
            print(f"SUSPICIOUS DEVICE!\nINVESTIGATE NOW!")
            break
    print(f"{scan} Scans were made")

print("Exercise 4: IP Scanner")
print("\nScan 1")
networkscan("192.168.1.", 1, 21, [5, 10, 15], [13])
print("\nScan 2")
networkscan("192.168.1.", 1, 21, [3, 7, 14, 17], [])