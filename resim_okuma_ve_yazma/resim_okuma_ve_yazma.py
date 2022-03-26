#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#opencv kutuphanesini dahil ettik
import cv2

#python dosyasi ile ayni yerde olan test.jpeg
#dosyasini sayisal olarak okuduk.
# resim=cv2.imread("test.jpeg")

#okuma islemi 0 parametresi ile yapilirse
#gri tonda okuma gerceklesir.
resim=cv2.imread("test.jpeg",0)
#gri tonda okumus oldugumuz resmi gri.png isminde
#python dosyasi ile ayni yere kaydettik.
cv2.imwrite("gri.png",resim)

#okudugumuz sayisal veriyi Pencere adinda
#bir pencerede goruntuledik
cv2.imshow("Pencere",resim)

#Goruntuleme islemi cok kisa surecegi icin
#programin sonsuza kadar beklemesini saglamaliyiz.
cv2.waitKey(0)

#Kullanici herhangi bir tusa bastigi zaman program sonlansin.
cv2.destroyAllWindows()

