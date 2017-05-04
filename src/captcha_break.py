#!/usr/bin/env python
#encoding:UTF-8

from keras.models import load_model
import cv2

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
        
    #----------------------------------------------------------------------
    def load_model(self, model):
        """"""
        self.model = load_model(model)
    
    #----------------------------------------------------------------------
    def predict(self, img):
        """"""
        if self.model is None:
            raise ValueError('No model was loaded!')
        pred_y = model.predict(img)
        return decode(pred_y)[:-1]
    
    
if __name__ == '__main__':
    model = captcha_break()
    model.load_model('mymodel.h5')
    img = cv2.imread("yanzhengma58.png")
    print model.predict(img)