import os
import nmap

def device_discovery():
    print("----------------------------------------------------------------------------------------------------------------------\n\n")
    print("'device_discovery' module is used detect the connected stations on the requested network ID and their mac addresses")
    print("\n\n----------------------------------------------------------------------------------------------------------------------")

    os.system("ip addr show")

    target_ip_range = input("Enter the IP range to perform the host discovery on: ")

    nm = nmap.PortScanner()
    nm.scan(hosts=target_ip_range, arguments='-sn')

    scan_results = []

    for host in nm.all_hosts():
        host_info = {
            'host': host,
            'status': nm[host].state(),
            'hostname': nm[host].hostname(),
            'mac': ', '.join(nm[host]['vendor'].values()) if 'vendor' in nm[host] else 'Unknown',
        }
        scan_results.append(host_info)

    for result in scan_results:
        print(f"Host: {result['host']} | Status: {result['status']} | Hostname: {result['hostname']} | MAC: {result['mac']}")

