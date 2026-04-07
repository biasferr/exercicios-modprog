# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:10:13 2026

@author: PC25
"""

def calcula_media_ponderada (nota1,peso1,nota2,peso2,nota3,peso3):
    media= ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3))/ (peso1 + peso2 + peso3)
    return media
    
def calcila_nota_final (p1, tA1, tB1, p2, tA2, tB2, trabalho):
    grau1 = calcula_media_ponderada(p1, 2, tA1, 1, tB1, 1)
    grau2 = calcula_media_ponderada(p2, 5, tA2, 2, tB2, 3)
    nota_final= calcula_media_ponderada(grau1, 1, grau2, 2, trabalho, 2)
    return nota_final


#bp
p1= float(input('Digite sua nota da P1:'))
tA1= float(input('Digite sua nota do teste A do G1:'))
tB1=float(input('Digite sua nota do teste B do G1:'))
p2= float(input('Digite sua nota da P2:'))
tA2=float(input('Digite sua nota do teste A do G1:'))
tB2=float(input('Digite sua nota do teste B do G1:'))
trabalho=float(input('Digite sua nota do trabalho:'))
    
grau1= calcula_media_ponderada(p1, 2, tA1, 1, tB1, 1)
grau2= calcula_media_ponderada(p2, 5, tA2, 2, tB2, 3)
NF= calcila_nota_final(p1, tA1, tB1, p2, tA2, tB2, trabalho) 
 
print (f'Grau 1: {grau1:.1f} \nGrau 1: {grau2:.1f} \nSua nota final é {NF:.1f}')
    
if NF>=5:
    print("APROVADO")
elif NF>=3:
    print("Fazer prova final.")
else:
    print("REPROVADO")