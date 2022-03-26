import cv2
import numpy as np

#orjinal resmimizi okuduk.
img_rgb=cv2.imread("ana_resim.jpg")
#arama islemi icin resmi grayscale yaptik.
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)

#arama isleminde baz alacagimiz template resmimizi okuduk.
nesne=cv2.imread("template.jpg",0)

#template resminin widt,height degerlerini aldik.
w,h=nesne.shape[::-1]

#grayscale resimde template ile TM_CCOFF_NORMED yontemiyle arama yapiyoruz.
#metot bize buldugu eslesmelerin konumlarini donduruyor.
res=cv2.matchTemplate(img_gray,nesne,cv2.TM_CCOEFF_NORMED)

#buldugu nesnenin dogruluk orani %75'den yuksekse
dogruluk_orani=0.75

#sonuclar arasindan dogruluk orani %75'den buyuk olanlari
#loc dizisine aktar.
loc=np.where(res>dogruluk_orani)

for i in zip(*loc[::-1]):
    #orjinal resime sonuclari cizdiriyoruz.
    cv2.rectangle(img_rgb,i,(i[0]+w,i[1]+h),(0,255,255),1)

cv2.imshow("sonuc",img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()