# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 01:41:00 2017

@author: AB Sanyal
"""

"""
The creature module. It defines the amibi object along with it's genetics. Refer to README.md for details.
"""

#imports
#import numpy as np

#Generator for generating unique id number for each amibi
def id_gen():
    i = 1
    while (True):
        yield i
        i += 1

t_idno = id_gen()

#The main creature class
class amibi:

    def __init__( self, t_money = 1 ):
        self.idno = next(t_idno)
        self.money = t_money