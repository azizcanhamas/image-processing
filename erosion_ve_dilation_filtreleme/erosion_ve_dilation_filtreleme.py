import cv2
import numpy as np

j=cv2.imread("j.png",0)
j2=cv2.imread("j2.png",0)
j3=cv2.imread("j3.png",0)

# İlk once gurultuleri silmek icin erosion islemi
# uygulayacagiz. Bu islemden sonra harf incelmis olacagindan dolayi
# tekrar dilation islemi uygulayarak harfi
# genisletiyoruz.
kernel=np.ones((4,4),np.uint8)
islem=cv2.erode(j2,kernel,iterations=1)
islem=cv2.dilate(islem,kernel,iterations=1)
cv2.imshow("j2",j2)
cv2.imshow("j2_islemli",islem)

#İlk once bosluklari doldurmak icin dilation islemi
#uygulayacagiz. Bu islemden sonra harf daha cok genislemis
#olacagindan dolayi tekrar erosion islemi uygulayarak harfi
#eski haline getiriyoruz.
kernel=np.ones((5,5),np.uint8)
j3_islem=cv2.dilate(j3,kernel,iterations=1)
j3_islem=cv2.erode(j3_islem,kernel,iterations=1)
cv2.imshow("j3",j3)
cv2.imshow("j3_islemli",j3_islem)

cv2.waitKey(0)
cv2.destroyAllWindows()