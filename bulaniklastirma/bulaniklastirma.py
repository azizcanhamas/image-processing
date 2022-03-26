#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

kamera=cv2.VideoCapture(0)

while True:
    ret,frame=kamera.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    alt_mavi=np.array([75,100,100])
    ust_mavi=np.array([130,255,255])
    
    mask=cv2.inRange(hsv,alt_mavi,ust_mavi)
    son=cv2.bitwise_and(frame,frame,mask=mask)
    
    #15x15'lik alani bulaniklastirmak icin ortalamasini aliyoruz.
    kernel=np.ones((15,15),np.float32)/225
    #derinlik -1
    smoothed=cv2.filter2D(son,-1,kernel)
    
    #Gaussian Yontemi ile Blurlastirma
    blur=cv2.GaussianBlur(son,(15,15),0)
    
    #Median Blur Yontemi ile Blurlastirma
    median=cv2.medianBlur(son,15)
    
    #Bilateral ile Blurlastirma
    bilateral=cv2.bilateralFilter(son,15,75,75)
    
    cv2.imshow("bilateral",bilateral)
    cv2.imshow("median",median)
    cv2.imshow("gaussian",blur)
    cv2.imshow("blur",smoothed)
    cv2.imshow("son",son)
    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
kamera.release()
cv2.destroyAllWindows()