#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
img=cv2.imread("messi.jpg")

#100x100 pikselinin renk degerlerini yazdirir.
print(img[100,100])

#100x100 noktasini beyaz yapar.
img[100,100]=[255,255,255]

#resmin belli bir konumunu degiskene alir
bolge=img[100:200,100:200]

#resmin belli bir alanina bolge degiskenindeki veriyi uygular.
img[200:300,200:300]=bolge

#(uygulanacak_resim,pt1,pt2,renk,kalinlik) dikdortgen cizer
cv2.rectangle(img,(375,266),(440,327),(0,255,255),1)


cv2.imshow("Bolge",bolge)
cv2.imshow("Orijinal",img)
cv2.waitKey(0)
cv2.destroyAllWindows()