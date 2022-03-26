#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img=cv2.imread("messi.jpg")

#resmi kanallarına ayirma ve tekrar birlestirme
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

#yontem_2
img[:,:,0]=0 #resmin tum mavi degerlerini sifirlar.


cv2.imshow("ORIGINAL",img)
cv2.waitKey(0)
cv2.destroyAllWindows()