#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img=cv2.imread("test.jpeg")

#Resmin 100x100 pikselinde yesil renginin degerini oku
#resim default olarak bgr formatinda okundugu icin
# 0 -> blue
# 1- -> green
# 2- -> red şeklinde ucuncu parametre girilmelidir.
print(str(img.item(100,100,1)))

#resmin 100x100 pikselinin yesil degerini 255 yaptik
#resim ciktisina dikkatli bakilirsa yesil bir nokta gozlemlenebilir.
img.itemset((100,100,1),255)

cv2.imshow("Pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()