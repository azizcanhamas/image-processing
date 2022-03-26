#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import cv2
import numpy as np

im1=cv2.imread("messi.jpg")
im2=cv2.imread("logo.jpg")

#logo resminin yukseklik,genislik ve kanal bilgisini
#degiskenlere aktariyoruz.
satir,sutun,kanal=im2.shape
print(satir,sutun,kanal)
#logo resminde olculere gore messi resminde roi cikariyoruz.
roi=im1[0:satir,0:sutun]

#threshold uygulayabilmek icin logoyu grayscale yapmamiz gerekir.
im2gray=cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)

#grayscale kanalinda piksel renk degeri 10'dan buyuk 255'den kucuk olanlari
#beyaz yap ve mask degiskenine goruntuyu kaydet
ret,mask=cv2.threshold(im2gray,10,255,cv2.THRESH_BINARY)

#beyazlari siyah, siyahlari beyaz yap.
mask_inv=cv2.bitwise_not(mask)

#logomuz siyaha dondu. roi ile andledigimiz zaman 
#siyah olarak kalip aktarilmis olacak.
im1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)

#logonun thresholdlanmis haliyle kendisine maske uyguladigimiz zaman
#siyah arka plan silinir.
im2_fg=cv2.bitwise_and(im2,im2,mask=mask)

#arka planini silmis oldugumuz logoyu messi resmiyle topluyoruz.
son_resim=cv2.add(im2_fg,roi)
im1[0:satir,0:sutun]=son_resim

cv2.imshow("pencere",im1)

#plt.subplot(441),plt.imshow(cv2.cvtColor(im1,cv2.COLOR_BGR2RGB)),plt.title("im1")
#plt.subplot(442),plt.imshow(cv2.cvtColor(im2,cv2.COLOR_BGR2RGB)),plt.title("im2")
#plt.subplot(443),plt.imshow(cv2.cvtColor(roi,cv2.COLOR_BGR2RGB)),plt.title("roi")
#plt.subplot(444),plt.imshow(cv2.cvtColor(im2gray,cv2.COLOR_BGR2RGB)),plt.title("im2gray")
#plt.subplot(445),plt.imshow(cv2.cvtColor(mask,cv2.COLOR_BGR2RGB)),plt.title("mask")
#plt.subplot(446),plt.imshow(cv2.cvtColor(mask_inv,cv2.COLOR_BGR2RGB)),plt.title("mask_inv")
#plt.subplot(447),plt.imshow(cv2.cvtColor(im1_bg,cv2.COLOR_BGR2RGB)),plt.title("im1_bg")
#plt.subplot(448),plt.imshow(cv2.cvtColor(im2_fg,cv2.COLOR_BGR2RGB)),plt.title("im2_fg")
#plt.subplot(449),plt.imshow(cv2.cvtColor(son_resim,cv2.COLOR_BGR2RGB)),plt.title("son_resim")
#plt.subplot(441),plt.imshow(cv2.cvtColor(im1,cv2.COLOR_BGR2RGB)),plt.title("im1_son")

cv2.waitKey(0)
cv2.destroyAllWindows()
