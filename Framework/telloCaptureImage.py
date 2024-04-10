import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

print(tello.get_battery())
tello.streamon()

while True:
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imwrite("test4.png", img)
    cv2.waitKey(1)
