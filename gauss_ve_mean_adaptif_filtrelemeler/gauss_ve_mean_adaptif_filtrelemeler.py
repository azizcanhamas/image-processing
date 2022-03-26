#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

#0 verilmezse hata verir.
img=cv2.imread("sudoku.jpeg",0)

ret,threshold1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#11 piksel komsuluklariyla BINARY_THRESH kullanarak normal ortalamasini alarak esikleme
mean=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

#11 piksel komsuluklariyla BINARY_THRESH kullanarak agirlikli ortalamasini alarak esikleme
gaus=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    


cv2.imshow("gaussian",gaus)
cv2.imshow("mean",mean)
cv2.imshow("basic_thresh",threshold1)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()