from djitellopy import Tello
from HostDiscovery import device_discovery
from ConnectCrackedNetwork import connect_to_cracked_network
from MonitorMode import switch_monitor_mode
from WPA_Handshake import wpa_capture_password_cracking
from RestartNetwork import restart_network_services


def tello_take_control():
    tello = Tello()

    switch_monitor_mode()
    wpa_capture_password_cracking()
    restart_network_services()
    connect_to_cracked_network()
    device_discovery()

    print("-----------------------------------------------------------------")
    print("Initiating the motion controls using the framework ")
    print("-----------------------------------------------------------------")

    # tello.connect()
    #
    # tello.takeoff()
    # tello.land()