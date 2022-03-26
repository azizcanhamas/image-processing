#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

#dahili kameradan goruntu okur
kamera=cv2.VideoCapture(0)

#goruntuyu XVID algoritmasi ile kaydetmek icin degisken.
fourcc=cv2.VideoWriter_fourcc(*'XVID')

#goruntyu kayit adinda avi formatinda fourcc ile 
#saniyede 20 defa 640x480 boyutunda kaydeder
kayit=cv2.VideoWriter('kayit.avi',fourcc,20.0,(640,480))

#kamera acik oldugu muddetce
while(kamera.isOpened()):
    #frame oku
    ret,frame=kamera.read()
    #frame okunabiliyorsa
    if ret==True:
        #goruntuyu ters cevirir.
        frame=cv2.flip(frame,0)
        #frame'i kaydet
        kayit.write(frame)
        cv2.imshow("frame",frame)
        if cv2.waitKey(25)&0xFF==ord("q"):
            break
#kamera ve kaydi serbest birak
kamera.release()
kayit.release()
cv2.destroyAllWindows()
        