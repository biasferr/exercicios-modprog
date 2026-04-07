# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:41:53 2026

@author: PC25
"""

def calcula_IMC(peso,altura):
    IMC= peso/altura**2
    return IMC

def classifica_IMC(IMC):
    if IMC<18.5:
        cat= 'AbaixoDoPeso'
    elif IMC<25:
        cat= 'PesoNormal'
    elif IMC<30:
        cat= 'Sobrepeso'
    else:
        cat= 'Obesidade'
    return cat

#BP
nome= input('Digite seu nome:')
peso= float(input('Digite seu peso:'))
altura= float(input('Digite sua altura:'))