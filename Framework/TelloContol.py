from djitellopy import Tello
import cv2
import time
from threading import Thread
from HostDiscovery import device_discovery
from ConnectCrackedNetwork import connect_to_cracked_network
from MonitorMode import switch_monitor_mode
from WPA_Handshake import wpa_capture_password_cracking
from RestartNetwork import restart_network_services

tello = Tello()

#
# def motion_control():
#     # fly
#     tello.connect()
#     tello.takeoff()
#     time.sleep(2)
#     tello.land()
#
#
# def click_snapshot():
#     # # take picture
#     tello.connect()
#     tello.streamon()
#     frame_read = tello.get_frame_read()
#     # tello.takeoff()
#     cv2.imwrite("test2.png", frame_read.frame)
#     # tello.land()
#
#
# def record_video():



def tello_take_control():
    # switch_monitor_mode()
    # wpa_capture_password_cracking()
    # restart_network_services()
    # connect_to_cracked_network()
    # device_discovery()

    print("-----------------------------------------------------------------")
    print("Initiating the motion controls using the framework ")
    print("-----------------------------------------------------------------")

    tello.connect()

    keep_recording = True
    tello.streamon()
    frame_read = tello.get_frame_read()

    def videoRecorder():
        # create a VideoWrite object, recoring to ./video.avi
        height, width, _ = frame_read.frame.shape
        video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

        while keep_recording:
            video.write(frame_read.frame)
            time.sleep(1 / 30)

        video.release()

    # we need to run the recorder in a seperate thread, otherwise blocking options
    #  would prevent frames from getting added to the video
    recorder = Thread(target=videoRecorder)
    recorder.start()
    time.sleep(3)
    keep_recording = False
    recorder.join()
