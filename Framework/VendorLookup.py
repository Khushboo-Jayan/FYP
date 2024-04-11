import os
from MonitorMode import switch_monitor_mode
from mac_vendor_lookup import MacLookup

def mac_addr_vendor_lookup():
    """
    Lookup MAC address vendor
    """
    switch_monitor_mode()

    global BSSID
    global channel

    try:
        print("-----------------------------------------------------------------")
        print("Use this module to detect the registered mac vendors by passing the mac address of the station connected")
        os.system("airodump-ng --band abg wlan0mon")

        BSSID = input("Enter the BSSID of any network to be sniffed: ")
        channel = input("Enter the channel this network is working on: ")

        os.system("airodump-ng wlan0mon -c " + channel + " --bssid " + BSSID)

        macAddr = input("Enter the mac address for the vendor lookup: ")
        try:
            print("\nMacAddress: " + macAddr + "\nVendor: " + MacLookup().lookup(macAddr))
            print("-----------------------------------------------------------------")
        except:
            print("Mac vendor not registered")
    except Exception as e:
        print(f"Error performing MAC address vendor lookup: {e}")