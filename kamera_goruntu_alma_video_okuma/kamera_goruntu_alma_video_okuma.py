#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

#Dahili kamera -> 0
#USB Kamera    -> 1
#Video -> file_path

#Dahili kameraya baglan
kamera=cv2.VideoCapture(0)

#video okunacaksa waitKey 30 yapilmalidir.
#kamera=cv2.VideoCapture("video.mp4")

#surekli olarak frame almasi icin sonsuz dongu
while True:
    #ret: goruntu alip alamadigini bildirir.(bool)
    #frame : goruntu verisini tutar
    #kameradan goruntu oku
    ret,frame=kamera.read()
    #okunan frame'i goruntule
    cv2.imshow("frame",frame)
    #1ms bekle ve q tusuna basildiysa donguyu kir
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
#kamerayi serbest birak
#tum pencereleri kapat
kamera.release()
cv2.destroyAllWindows()