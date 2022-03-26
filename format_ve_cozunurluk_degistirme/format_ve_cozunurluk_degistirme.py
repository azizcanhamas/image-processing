#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

# (path_bilgisi,resim_verisi,kalite_orani(%),sıkıstırma_orani(0...1))
def kaydet(path,image,jpg_kalite=None,png_compress=None):
    #eger kalite orani verildiyse
    if jpg_kalite:
        #resmi verilen kalite oraniyla path bilgisine gore kaydet
        cv2.imwrite(path,image,[int(cv2.IMWRITE_JPEG_QUALITY),jpg_kalite])
    elif png_compress:
        #resmi verilen sıkıstırma oraniyla path bilgisine gore kaydet
        cv2.imwrite(path,image,[int(cv2.IMWRITE_PNG_COMPRESSION),png_compress])
    else:
        #oldugu gibi resmi kaydet
        cv2.imwrite(path,image)
        
def main():
    #ornek bir resim okuyoruz.
    impath="messi.jpg"
    img=cv2.imread(impath)
    
    #okudugumuz resmi goruntuluyoruz.
    cv2.imshow("messi",img)
    
    #islemden sonra dosyanin kaydedilecegi path bilgisini belirliyoruz.
    cikis_jpeg="messi2.jpg"
    # (path bilgisi,ornek_resim,%85 kalite)
    kaydet(cikis_jpeg,img,85)
    
    cikis_png="messi2.png"
    kaydet(cikis_png,img,png_compress=0.4)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
main()

