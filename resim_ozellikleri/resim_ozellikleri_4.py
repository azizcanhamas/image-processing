#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img=cv2.imread("test.jpeg")

#Herhangi iki resmi toplarken iki resminde veri
#tipinin ayni olmasi gerekmektedir. Bunu kontrol etmek icin
print(img.dtype)

cv2.imshow("Pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()