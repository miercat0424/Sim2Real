import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Green
    low_Green   = np.array([30, 175, 0])
    high_Green  = np.array([110 , 255, 255])
    Green_mask  = cv2.inRange(hsv_frame, low_Green, high_Green)
    Green       = cv2.bitwise_and(frame, frame, mask=Green_mask)

    if np.array([100, 190, 100]) in Green_mask == True:
        print("True")

    # Red
    low_Red   = np.array([0, 0, 0])
    high_Red  = np.array([138, 12, 2])
    Red_mask  = cv2.inRange(hsv_frame, low_Red, high_Red)
    Red       = cv2.bitwise_and(frame, frame, mask=Red_mask)

    # cv2.imshow("Frame",frame)
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", Red)
    cv2.imshow("Green", Green)

    key = cv2.waitKey(1)
    if key == 27:
        break