#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

resim=np.zeros((400,400,3))
#resim verisine sol ust kose 100x100 sag alt kose 300x300
# 255,255 renginde 2px kalinliginda cizgi cizer
cv2.line(resim,(100,100),(300,300),(255,255,0),2)

#resim verisine 200x200 merkez noktasi 100px cap degeri ile 255,0,0
#renginde 1 kalinliginda daire cizer.
cv2.circle(resim,(200,200),100,(255,0,0),1)

cv2.imshow("resim",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
