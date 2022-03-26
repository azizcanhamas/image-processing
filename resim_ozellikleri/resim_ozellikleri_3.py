#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img=cv2.imread("test.jpeg")
#resimde kac adet piksel oldugu bilgisini verir.
print(img.size)

#¶esmi gri tonda okudugumuz zaman renkliye gore 3'te bir
#oraninda piksel degeri gozukmektedir. cunku gri tondaki resimler
#tek katmanlidir.
img=cv2.imread("test.jpeg",0)
#resimde kac adet piksel oldugu bilgisini verir.
print(img.size)

cv2.imshow("Pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()