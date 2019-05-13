# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:33:54 2019

@author: Jhoan Saavedra
"""

import requests
req=requests.post('http://localhost:14/foro', json={'num':2})
print(req)

int(req.content.decode())