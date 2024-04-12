import os


def switch_monitor_mode():
    """
    Switch the network adapter to monitor mode.
    """
    print("---------------------------------------------------------------------")
    print("Switching the network adapter to monitor mode")

    # Kill interfering processes
    os.system("airmon-ng check kill")

    # Start monitor mode on wlan0 interface
    os.system("airmon-ng start wlan0")

    # Display network interface information
    os.system("ifconfig")

    print("---------------------------------------------------------------------\n\n\n")
