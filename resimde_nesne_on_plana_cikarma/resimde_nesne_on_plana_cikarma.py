import cv2
import numpy as np
from matplotlib import pyplot as plt

#on plana cikarma islemi uygulayacagimiz resmi okuyoruz.
img=cv2.imread("on_plan.jpg")

mask=np.zeros(img.shape[:2],np.uint8)

bgdModel=np.zeros((1,65),np.float64)
fgdModel=np.zeros((1,65),np.float64)

#resimde tespit etmek istedigimiz nesnenin bulundugu alanin
#yaklasik piksel koordinatlarini veriyoruz.
dikdortgen=(250,125,150,250)
cv2.grabCut(img,mask,dikdortgen,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
img=img*mask2[:,:,np.newaxis]

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()