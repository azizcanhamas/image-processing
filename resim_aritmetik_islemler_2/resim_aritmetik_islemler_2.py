#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:04:59 2022

@author: azu
"""

import cv2
import numpy as np

#uint8=unsigned int 8
#işaretsiz 8 bitlik aralikta deger alir.
#yani 0...256
#250+10=260-256=4 olur.
x=np.uint8([250])
y=np.uint8([10])
print(x+y) 

#cv2 kutuphanesi gore toplamada
#255 doyum noktasıdır. tasma olmaz.
print(cv2.add(x,y))
