import os

def switch_monitor_mode():
    print("---------------------------------------------------------------------")
    print("Switching the network adapter to monitor mode")
    os.system("airmon-ng check kill")
    os.system("airmon-ng start wlan0")
    os.system("ifconfig")
    print("---------------------------------------------------------------------\n\n\n")
