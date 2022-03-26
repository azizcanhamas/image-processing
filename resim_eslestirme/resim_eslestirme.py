import cv2
import numpy as np
import matplotlib.pyplot as plt

resim_aranacak=cv2.imread('kucuk_resim.JPG',0)

buyuk_resim=cv2.imread('buyuk_resim.JPG',0)

orb=cv2.ORB_create()
an1,hedef1=orb.detectAndCompute(resim_aranacak,None)
an2,hedef2=orb.detectAndCompute(buyuk_resim,None)

bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
eslesmeler=bf.match(hedef1,hedef2)
eslesmeler=sorted(eslesmeler,key=lambda x:x.distance)
son_resim=cv2.drawMatches(resim_aranacak,an1,buyuk_resim,
                          an2,eslesmeler[:10],None,flags=2)
cv2.imshow("son",son_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
