#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img=cv2.imread("test.jpeg")

#okumus oldugumuz resmin yukselik,genislik ve renk kanal
#bilgisini verir. Eger resmin 0 parametresi ile gri tonda
#okursak shape metodundan sonra ucuncu parametre gelmez.
#cunku tek kanal olmus olur.
print(img.shape)

#Bir resmin renkli olup olmadigini anlamak icin
#eger uc degeri geliyorsa resim birden fazla kanal degerine
#sahiptir. eger 2 degeri geliyorsa resmin kanal degeri yoktur.
#tek kanallidir.
print(len(img.shape))


cv2.imshow("Pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()