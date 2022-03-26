#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
resim=cv2.imread("messi.jpg")
cv2.rectangle(resim,(70,60),(400,350),(255,0,0),1)
cv2.imshow("messi",resim)

resim=np.zeros((400,400,3),dtype="uint8")
cv2.rectangle(resim,(100,100),(300,300),(255,255,0),1)
cv2.imshow("siyah",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()

