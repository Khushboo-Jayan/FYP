import os


def restart_network_services():
    """
    Restart network services to switch the wifi adapter mode to managed instead of monitor.
    """
    try:
        print("-----------------------------------------------------------------------------------------------\n\n")
        print("Restarting the network services to switch the wifi adapter mode to managed instead of monitor")
        print("\n\n-------------------------------------------------------------------------------------------")

        # Take down the wlan0mon interface
        os.system("ifconfig wlan0mon down")

        # Set the wlan0mon interface mode to managed
        os.system("iwconfig wlan0mon mode managed")

        # Restart the NetworkManager service
        os.system("systemctl restart NetworkManager")

        # Display current wifi configuration
        os.system("iwconfig")

        # Bring the wlan0mon interface back up
        os.system("ifconfig wlan0mon up")

    except Exception as e:
        print(f"Error restarting network services: {e}")
