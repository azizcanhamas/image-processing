#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

img=cv2.imread("messi.jpg")

canny=cv2.Canny(img,50,200)

cv2.imshow("canny",canny)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

