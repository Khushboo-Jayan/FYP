import cv2
from djitellopy import Tello
from ConnectCrackedNetwork import connect_to_cracked_network
from MonitorMode import switch_monitor_mode
from WPA_Handshake import wpa_capture_password_cracking
from RestartNetwork import restart_network_services


def take_tello_image():
    # switch_monitor_mode()
    # wpa_capture_password_cracking()
    # restart_network_services()
    # connect_to_cracked_network()

    tello = Tello()

    tello.connect()

    print("Your Drone battery is: " + str(tello.get_battery()))
    tello.streamon()

    while True:
        img = tello.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        cv2.imshow("Photo", img)

        # Wait for a key press and display all windows
        cv2.waitKey(1)
        cv2.destroyAllWindows()





