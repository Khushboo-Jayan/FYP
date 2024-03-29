import os
import nmap


def device_discovery(target):
    os.system("ip addr show")
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-sn')

    scan_results = []

    for host in nm.all_hosts():
        host_info = {
            'host': host,
            'status': nm[host].state(),
            'hostname': nm[host].hostname(),
        }
        scan_results.append(host_info)

    return scan_results


target_ip_range = input("Enter the IP range to perform the host discovery on")
results = device_discovery(target_ip_range)


for result in results:
    print(f"Host: {result['host']} | Status: {result['status']} | Hostname: {result['hostname']}")

