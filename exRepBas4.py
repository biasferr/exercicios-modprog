# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 10:50:26 2026

@author: PC-PROF
"""
# Ex4: Escreva um programa para ler a nota1 e a 
# nota2 de cada aluno de uma turma, calculando 
# e exibindo a media de cada aluno e ao final 
# exibir QUANTOS APROVADOS há em uma turma de 
# 4 alunos. Escreva e utilize a função calcula_media 
# que recebe as duas notas do alunos e retorna a 
# media do aluno.
# OBS: media >=5  está  APV, do contrário está REP. 


def calcula_media(nt1,nt2):
    return (nt1+nt2)/2 

#BP
cont = 0 
contAprov = 0  # CONTADOR DO CRITERIO
while cont < 2:
    print('-----')
    nt1 = float(input('Nota 1 do aluno:'))
    nt2 = float(input('Nota 2 do aluno:'))
    med = calcula_media(nt1,nt2)
    print(f'Esse aluno teve media {med:.1f}')
    if med >= 5.0:
        contAprov+=1 
    cont+=1 

#SOMENTE APOS O TERMINO DA REPETICAO
print(f'Qtd apv:{contAprov}')


