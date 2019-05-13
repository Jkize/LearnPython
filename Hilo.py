# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:10:06 2019

@author: Jhoan Saavedra
"""

import threading
import time
def Multipy(a,b):
    time.sleep(10)
    return a*b

multThread=threading.Thread(target='Multipy',args(5,6))
multThread.start();
print('Hola')
A='NO MAS?'