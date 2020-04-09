#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:11:24 2020

@author: ash
"""
from keras.backend import clear_session
clear_session()

from keras import models
import numpy as np
import json


#model=models.load_model('EIML/EINetV2_2.h5')
#model._make_predict_function()
class EIML:
    
    def __init__(self,model_file='EIML/EINetV2_2.h5'):
        self.model=models.load_model(model_file)
        self.X_names=json.load(open("EIML/X_names.json","r"))
        self.y_names=json.load(open("EIML/y_names.json","r"))
        self.label_to_index_dict={l:i for i,l in self.X_names.items()}
        #self.model._make_predict_function()
        
    @property
    def input_labels(self):
        return self.X_names

    @property
    def output_labels(self):
        return self.y_names
    
    @property
    def label_to_index(self):
        return self.label_to_index_dict
    
    def convert(self,o):
        if isinstance(o, np.int64): return int(o)  
        raise TypeError
    
    def get_jobs(self,X_in):
        X_in=np.reshape(X_in,(-1,*X_in.shape))
        l=self.model.predict(x=X_in)
        res={i:(v,self.y_names[str(v)]) for i,v in enumerate(l.argsort()[0][::-1])}
        return res
    
    
    def prepare_input(self,labels=[]):
        if len(labels)==0 and not all(label in labels for label in self.X_names):
            return None
        X_in=np.zeros((len(self.X_names)))
        try:
            for label in labels:
                X_in[int(self.label_to_index_dict[label])]=1
                
        except Exception as e:
            X_in=e
            
        finally:
            return X_in
    
    
    def predict(self,labels=[]):
        try:
            X_in=self.prepare_input(labels)
            result=self.get_jobs(X_in)
            return result
        except Exception as e:
            return e
    

