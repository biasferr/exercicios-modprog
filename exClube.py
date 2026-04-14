# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:45:46 2026

@author: PC25
"""


qntPessoas = int(input('Quantidade de pessoas que vieram a festa:'))
cont = 0
while cont < qntPessoas:
    nome = input('Nome:')
    plano = input ('Plano:')
    if plano == 'diamante'
        desconto = 50
    elif plano != 'diamante':
        idade = int(input('Idade:'))
        if idade < 12:
            desconto = 40
        elif idade > 60:
            desconto = 30
        elif 