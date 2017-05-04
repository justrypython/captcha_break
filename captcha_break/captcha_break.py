#!/usr/bin/env python
#encoding:UTF-8

from keras.models import load_model
import numpy as np
import cv2
import matplotlib.pyplot as plt

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghijlmnqrtuwxy"
width, height, n_len, n_class = 100, 40, 5, len(chars)
def decode(y):
    y = np.argmax(np.array(y), axis=2)[:,0]
    return ''.join([chars[x] for x in y])

########################################################################
class captcha_break(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        self.model = None
        self.load_model('mymodel.h5')
        
    #----------------------------------------------------------------------
    def load_model(self, model):
        """"""
        self.model = load_model(model)
    
    #----------------------------------------------------------------------
    def predict(self, img):
        """"""
        if self.model is None:
            raise ValueError('No model was loaded!')
        img = img.reshape([1, height, width, -1])
        pred_y = self.model.predict(img)
        return decode(pred_y)[:-1]
    
    
if __name__ == '__main__':
    model = captcha_break()
    img = cv2.imread("yanzhengma58.png")
    plt.imshow(img)
    plt.show()
    print model.predict(img)