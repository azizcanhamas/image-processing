#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
     
from matplotlib import pyplot as plt

img=cv2.imread("gradient.jpg")
#THRESHOLD CESITLERİ

#piksel degeri 100'den buyuk olanlarin degerini 150 yap
ret,threshold1=cv2.threshold(img,100,150,cv2.THRESH_BINARY)
ret,threshold2=cv2.threshold(img,100,150,cv2.THRESH_BINARY_INV)
ret,threshold3=cv2.threshold(img,100,150,cv2.THRESH_TRUNC)
ret,threshold4=cv2.threshold(img,100,150,cv2.THRESH_TOZERO)
ret,threshold5=cv2.threshold(img,100,150,cv2.THRESH_TOZERO_INV)

basliklar=["orjinal","binary","binary_inv","trunc","tozero","tozero_inv"]
resimler=[img,threshold1,threshold2,threshold3,threshold4,threshold5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(resimler[i],"gray")
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])

plt.show()