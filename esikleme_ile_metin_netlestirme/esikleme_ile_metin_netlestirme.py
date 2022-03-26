import cv2

#Resmi oldugu okuyup 10 degerine gore basic threshold islemi
# img=cv2.imread("sayfa.jpg")
# _,th1=cv2.threshold(img,10,255,cv2.THRESH_BINARY)

#Resmi oldugu gibi okuyup 6 degeriyle ters threshold islemi
# img=cv2.imread("sayfa.jpg")
# _,th2=cv2.threshold(img,6,255,cv2.THRESH_BINARY_INV)

#Resmi grayscale okuyup 4 degeriyle ters threshold islemi
# img=cv2.imread("sayfa.jpg",0)
# _,th3=cv2.threshold(img,4,255,cv2.THRESH_BINARY_INV)

#Adaptive Gauss Threshold Yontemi ile
img=cv2.imread("sayfa.jpg",0)
gauss=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)

#Otsu (Bu ornekte iyi performans vermedi.)
# img=cv2.imread("sayfa.jpg",0)
# _,otsu=cv2.threshold(img,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("sayfa",img)
# cv2.imshow("th1",th1)
# cv2.imshow("th2",th2)
# cv2.imshow("th3",th3)
cv2.imshow("gauss_adaptive",gauss)
# cv2.imshow("otsu_",otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()