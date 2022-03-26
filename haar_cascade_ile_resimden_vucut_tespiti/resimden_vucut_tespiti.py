import cv2

test_img=cv2.imread("r2.jpg")
body_cascade=cv2.CascadeClassifier("haarcascade_fullbody.xml")

bodys=body_cascade.detectMultiScale(test_img,1.5,4)

for (x,y,w,h) in bodys:
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("img",test_img)
cv2.waitKey(0)
cv2.destroyAllWindows()