#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

resim=np.zeros((400,400,3))

#resim_verisi,sol_alt_kose_konum,font,font_buyukluk,renk,kalinlik,tip
cv2.putText(resim,"aziz",(200,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),2,cv2.LINE_4)

cv2.imshow("resim",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()