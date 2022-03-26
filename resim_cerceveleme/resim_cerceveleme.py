#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

import cv2
import numpy as np

#mavi rengini array olarak tanimliyoruz.
mavi=[255,0,0]
img=cv2.imread("messi.jpg")

#resmin sırasıyla ust,alt,sol,sag kisimlarindan 100'er piksellik cerceve ekliyoruz.
#birden fazla cerceve cesidi vardir. Constant cercevesine renk atamasi yapilabilir.
replicate=cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_REPLICATE)
reflect=cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_REFLECT)
reflect101=cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_REFLECT101)
wrap=cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_WRAP)
constant=cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_CONSTANT,value=mavi)

#cv2.imshow("Replicate",replicate)
#cv2.imshow("Reflect",reflect)
#cv2.imshow("Reflect101",reflect101)
#cv2.imshow("Wrap",wrap)
#cv2.imshow("Constant",constant)

#yukarida oldugu gibi surekli imshow komutu ile gozlem yapmak yerine
#matplotlib altindaki pyplot, plt etiketiyle import edilir.
#2x3 seklinde gosterilmesi icin 23 yazilir ve yanina sirasiyla index numarasi verilir.
plt.subplot(231),plt.imshow(img),plt.title("orjinal")
plt.subplot(232),plt.imshow(replicate),plt.title("replicate")
plt.subplot(233),plt.imshow(reflect),plt.title("reflect")
plt.subplot(234),plt.imshow(reflect101),plt.title("reflect101")
plt.subplot(235),plt.imshow(wrap),plt.title("wrap")
plt.subplot(236),plt.imshow(constant,"gray"),plt.title("constant")

plt.show()

#cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()