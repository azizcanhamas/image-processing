#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

#Bu islem goruntude bir seyi ararken (yuz,vucut vb.) farkli cozunurluklerde
#aramamizi saglar.

#ornek resim okuduk
img=cv2.imread("messi.jpg")

#resmi kuculttuk
down=cv2.pyrDown(img)
#resmi buyuttuk
up=cv2.pyrUp(img)

#ciktilari pencereye aktardik.
cv2.imshow("img",img)
cv2.imshow("up",up)
cv2.imshow("down",down)

cv2.waitKey(0)
cv2.destroyAllWindows()