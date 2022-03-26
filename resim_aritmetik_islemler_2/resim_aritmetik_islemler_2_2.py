#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

import cv2
import  numpy as np

im1=cv2.imread("1.png")
im2=cv2.imread("x.jpg")

#birebir iki resmi toplar.
toplam=cv2.add(im1,im2)

#%70 im1 resminden %30 im2 resminden kullanarak topla
agirlikli=cv2.addWeighted(im1,0.7,im2,0.3,0)

#ciktilari tek resimde goster.
plt.subplot(221),plt.imshow(cv2.cvtColor(im1,cv2.COLOR_BGR2RGB)),plt.title("1")
plt.subplot(222),plt.imshow(cv2.cvtColor(im2,cv2.COLOR_BGR2RGB)),plt.title("x")
plt.subplot(223),plt.imshow(cv2.cvtColor(toplam,cv2.COLOR_BGR2RGB)),plt.title("toplam")
plt.subplot(224),plt.imshow(cv2.cvtColor(agirlikli,cv2.COLOR_BGR2RGB)),plt.title("agirlikli")

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
