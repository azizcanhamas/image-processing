#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

#dahili kameradan veri okuyacagimizi belirttik
kamera=cv2.VideoCapture(0)

#goruntu boyutunu 1920x1080 olarak belirledik.
kamera.set(3,1920)
kamera.set(4,1080)

while True:
    #frame okuduk
    ret,frame=kamera.read()
    
    #okudugumuz frame'i BGR uzayindan HSV renk uzayina cevirdik
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #HSV RENK UZAYI ALT_UST LIMITLER
#   Turuncu	(0, 100, 100)	(22, 255, 255)
#   Sarı	(22, 100, 100)	(38, 255, 255)
#   Yeşil	(38, 100, 100)	(75, 255, 255)
#   Mavi	(75, 100, 100)	(130, 255, 255)
#   Mor	    (130, 100, 100)	(160, 255, 255)
#   Kırmızı	(160, 100, 100)	(179, 255, 255)
#   Beyaz   (0,0,140) (256,60,256)
    
    
    
#    dusuk_kirmizi=np.array([160,100,100])
#    yuksek_kirmizi=np.array([179,255,255])
#    mask=cv2.inRange(hsv,dusuk_kirmizi,yuksek_kirmizi)
    
    #Goruntude tespit edecegimiz mavinin alt araligini belirttik
    dusuk_mavi=np.array([75,100,100])
    #Goruntude tespit edecegimiz mavinin ust araligini belirttik
    yuksek_mavi=np.array([130,255,255])
    #hsv isimli goruntudeki renk deger verilerinden belirttigimiz araliga
    #girenleri goruntulemek icin inRange metodunu kullandik
    mask=cv2.inRange(hsv,dusuk_mavi,yuksek_mavi)
    
    #and islemi ile frame'imize maskeyi uyguladik
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("son",son_resim)
    # cv2.imshow("hsv",hsv)
    # cv2.imshow("frame",frame)
    
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
    
kamera.release()
cv2.destroyAllWindows()