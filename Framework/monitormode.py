import os

def switch_monitor_mode():
    print("Switching the network adapter to monitor mode")
    print("---------------------------------------------------------------------")
    os.system("airmon-ng check kill")
    os.system("airmon-ng start wlan0")
    os.system("ifconfig")
    print("---------------------------------------------------------------------\n\n\n")
