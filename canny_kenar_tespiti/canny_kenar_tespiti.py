#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,frame=kamera.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    alt_mavi=np.array([75,100,100])
    ust_mavi=np.array([130,255,255])
    
    #Laplacian ve Sobel
#    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
#    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
#    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    
    #Canny
    #threshold degerleri verilmelidir.
    kenarlar=cv2.Canny(frame,100,200)
    
    mask=cv2.inRange(hsv,alt_mavi,ust_mavi)
    son=cv2.bitwise_and(frame,frame,mask=mask)
    
#    cv2.imshow("laplacian",laplacian)
#    cv2.imshow("sobelx",sobelx)
#    cv2.imshow("sobely",sobely)
    cv2.imshow("canny",kenarlar)
    cv2.imshow("mavi",son)
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
kamera.release()
cv2.destroyAllWindows()