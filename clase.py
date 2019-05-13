# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:16:01 2019

@author: Jhoan Saavedra
"""

Colores=['Azul','Rojo','Verde']

class Carro:
    nPuertas=2
    nLlantas=3
    def __init__(self,nVentanas=5,color=None):
        if not isinstance(nVentanas,int):
            raise ValueError('Ventanas debe ser un entero')
        else:
            self.nVentanas=nVentanas
        
        if color is not None:
            if isinstance(color,str):
                if color in Colores:
                    self.color=color;
                else:
                    print('El color no existe lo voy a poner azul')
                    self.color='Azul'
            else:
                raise ValueError('Color no es un string')
        else:
            self.color='Rojo'
                
Porshe=Carro(nVentanas=21)
print(Porshe.color)