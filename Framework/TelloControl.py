import time

from djitellopy import Tello
from ConnectCrackedNetwork import connect_to_cracked_network
from MonitorMode import switch_monitor_mode
from WPA_Handshake import wpa_capture_password_cracking
from RestartNetwork import restart_network_services
import os

def take_flight_control():
    # switch_monitor_mode()
    # wpa_capture_password_cracking()
    # restart_network_services()
    # connect_to_cracked_network()

    tello = Tello()

    tello.connect()
    tello.streamon()

    print("Your Drone battery is: " + str(tello.get_battery()) + "%")
    os.system('netstat -anp | grep "11111"')
    os.system("ffplay udp://@:11111 &")
    tello.takeoff()
    tello.send_rc_control(0,10,0,0)
    time.sleep(2)
    tello.send_rc_control(0,10,0,30)
    time.sleep(2)
    tello.send_rc_control(0,0,0,0)
    tello.land()


