import cv2 as cv2
import pickle

img = cv2.imread(r'ui1\computer vision\smart car detection.py')
 
width ,height =  32 , 73

try:
   with open('carparkpos','rb') as f:
    pickle.load(f)
except:
   poslist = []

def mouseclick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        poslist.append((x,y))
    if events == cv2.EVENT_RBUTTONDBLCLK:
        for i , pos in enumerate(poslist):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+width:
                poslist.pop(i)


while True:
    img = cv2.imread(r'ui1\computer vision\car.jpg')
      # cv2.rectangle(img,(67,47),(99,120),(255,0,255),2)
    for pos in poslist:
         cv2.rectangle(img,pos ,(pos[0] + width, pos[1] + height),(255,0,255), 2)
         cv2.imshow('image',img)
         cv2.setMouseCallback("image", mouseclick)
         cv2.waitKey(1)