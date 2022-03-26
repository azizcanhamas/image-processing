#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

img=cv2.imread("messi.jpg")
ekran_cozunurluk=640,720


skala_genislik=ekran_cozunurluk[0]/img.shape[1]
skala_yukseklik=ekran_cozunurluk[1]/img.shape[0]
skala=min(skala_genislik,skala_yukseklik)

#pencere genislik ve yukseklik degerlerinin hesaplanmasi
pencere_genislik=int(img.shape[1]*skala)
pencere_yukseklik=int(img.shape[0]*skala)

#pencereyi boyutlandirilabilir yapar
cv2.namedWindow("Boyutlanabilir Pencere",cv2.WINDOW_NORMAL)

#pencereyi hesaplanan olculerde baslatir.
cv2.resizeWindow("Boyutlanabilir Pencere",pencere_genislik,pencere_yukseklik)

cv2.imshow("Boyutlanabilir Pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

