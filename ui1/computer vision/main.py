import cv2
import pickle 
import cvzone
import numpy as np
#videofeed

cap = cv2.VideoCapture(r'C:\Users\Mohd Salman\Downloads')

while True:
       if cap.get(cv2.CAP_PROP_POS_FRAMES)==cap.get(cv2.CAP_PROP_FRAME_COUNT):
              cap.set(cv2.CAP_PROP_POS_FRAMES,0)
      
              success,img = cap.read()
              cv2.imshow('image',img)
              cv2.waitKey(1)
