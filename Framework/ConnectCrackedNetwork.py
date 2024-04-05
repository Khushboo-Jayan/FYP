import os

def connect_to_cracked_network():
    """
    Connect to a Wi-Fi network
    """
    try:
        print("-----------------------------------------------------------------\n\n")
        print("Connect to the network using password extracted by wpahandshake ")
        print("\n\n-----------------------------------------------------------------")

        os.system("nmcli device wifi list")

        BSSID = input("\nEnter the BSSID of any network to be connected: ")
        password = input("Enter the password extracted using wpa2 handshake password cracking : ")

        os.system("nmcli device wifi connect " + BSSID + " password " + password)

    except Exception as e:
        print(f"Error connecting to Wi-Fi network: {e}")
