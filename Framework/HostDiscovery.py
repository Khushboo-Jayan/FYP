import os
import nmap

def device_discovery():
    """
    Perform device discovery on the specified IP range.
    """
    # Displaying module information
    print("----------------------------------------------------------------------------------------------------------------------\n\n")
    print("'device_discovery' module is used to detect the connected stations on the requested network ID and their MAC addresses")
    print("\n\n----------------------------------------------------------------------------------------------------------------------")

    # Displaying system IP configuration
    os.system("ip addr show")

    # Inputting IP range for host discovery
    target_ip_range = input("Enter the IP range to perform the host discovery on: ")

    # Initializing nmap PortScanner object
    nm = nmap.PortScanner()
    nm.scan(hosts=target_ip_range, arguments='-sn')

    # Storing scan results
    scan_results = []

    # Iterating through scan results and storing host information
    for host in nm.all_hosts():
        host_info = {
            'host': host,
            'status': nm[host].state(),
            'hostname': nm[host].hostname(),
            'mac': ', '.join(nm[host]['vendor'].values()) if 'vendor' in nm[host] else 'Unknown',
        }
        scan_results.append(host_info)

    # Displaying host information
    for result in scan_results:
        print(f"Host: {result['host']} | Status: {result['status']} | Hostname: {result['hostname']} | MAC: {result['mac']}")
