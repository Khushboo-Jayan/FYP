import os

def restart_network_services():
    """
    Restart network services
    """
    try:
        os.system("ifconfig wlan0mon down")
        os.system("iwconfig wlan0mon mode managed")
        os.system("systemctl restart NetworkManager")
        os.system("iwconfig")
        os.system("ifconfig wlan0mon up")
    except Exception as e:
        print(f"Error restarting network services: {e}")