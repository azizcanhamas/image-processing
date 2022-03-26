#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img=cv2.imread("test.jpeg")

#Resmin herhangi bir alanini almaya calisalim.
#ilk once y araligi ardindan x araligi verilmelidir.
ROI=img[270:325,380:440]
cv2.imshow("ROI",ROI)

#ROI degiskenine aldigimiz piksel alanini baska bir yere klonluyoruz.
img[270:325,480:540]=ROI

cv2.imshow("ORIGINAL",img)
cv2.waitKey(0)
cv2.destroyAllWindows()