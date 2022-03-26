#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

kamera=cv2.VideoCapture(0,0)

#kameradan gelecek olan framelerin boyutunu ayarlar. (YONTEM-1)
#kamera.set(cv2.CAP_PROP_FRAME_WIDTH,sq1280)
#kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    ret,frame=kamera.read()
    #kameradan okunan goruntunun grayscale hale getirilmesi
    gri_ton=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gri_ton",gri_ton)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()