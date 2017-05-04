#!/usr/bin/env python
#encoding:UTF-8

from captcha_break import captcha_break
import cv2
import os

print os.getcwd()

#----------------------------------------------------------------------
def load_model(model='mymodel.h5'):
    """"""
    cb = captcha_break()
    cb.load_model(model)
    return cb

if __name__ == "__main__":
    img = cv2.imread("yanzhengma58.png")    
    cb = load_model()
    print cb.predict(img)