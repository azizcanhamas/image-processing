#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

#dahili kameramizdan goruntuyu okuduk
kamera=cv2.VideoCapture(0)

#kamera verisininn 3. parametresi width
#4. parametresi height degeridir.
#kameradan gelen veriyi set metodu ile
#1920x1080 boyutuna getirdik.
def cozunurluk_1080():
    kamera.set(3,1920)
    kamera.set(4,1080)
    
def cozunurluk_720():
    kamera.set(3,1280)
    kamera.set(4,720)
    
def cozunurluk_480():
    kamera.set(3,640)
    kamera.set(4,480)

#rastgele degerlerle cozunurluk belirleme
def coz_belirle(width,height):
    kamera.set(3,width)
    kamera.set(4,height)

#okunan framein default olarak %75 ini alir.
#ve frame verisini yeniden boyutlandirilmis sekilde
#geri dondurur
def scalalama(frame,percent=75):
    width=int(frame.shape[1]*percent/100)
    height=int(frame.shape[0]*percent/100)
    boyut=(width,height)
    return cv2.resize(frame,boyut,interpolation=cv2.INTER_AREA)
    

cozunurluk_1080()

while True:
    ret,frame=kamera.read() 
    fr75=scalalama(frame)
    cv2.imshow("fr75",fr75)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
kamera.release()
cv2.destroyAllWindows()
    