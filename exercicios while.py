# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:38:14 2026

@author: PC25
"""

def calcula_media(nota1,nota2):
    media= (nota1 + nota2)/2
    return media


alunos= 4
cont= 0

while cont<alunos:
    nota1 = float(input('Digite a sua primeira nota: '))
    nota2 = float(input('Digite a sua segunda nota: '))
    media= calcula_media(nota1, nota2)
    print (f'A sua média é: {media:.2f}')
    if media >= 5:
        print ('APROVADO')
    else:
        print ('REPROVADO')
    cont += 1