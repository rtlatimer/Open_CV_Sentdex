# Capture video with your webcam using OpenCV


# import modules
import cv2
import numpy as np

# Use VideoCapture method and '0' for default webcam
cap = cv2.VideoCapture(0)
 
# create an infinite loop that returns webcam footage in grayscale
# break if you hit the 'q' key
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()