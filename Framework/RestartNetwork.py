import os

def restart_network_services():
    """
    Restart network services
    """
    try:
        print("-----------------------------------------------------------------------------------------------\n\n")
        print("Restarting the network services to switch the wifi adapter mode to managed instead of monitor")
        print("\n\n-------------------------------------------------------------------------------------------")
        os.system("ifconfig wlan0mon down")
        os.system("iwconfig wlan0mon mode managed")
        os.system("systemctl restart NetworkManager")
        os.system("iwconfig")
        os.system("ifconfig wlan0mon up")
    except Exception as e:
        print(f"Error restarting network services: {e}")