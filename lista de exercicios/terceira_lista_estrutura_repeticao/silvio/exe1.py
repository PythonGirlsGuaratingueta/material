# -*- coding: utf-8 -*-
"""
@author: Silvio Luis
"""

"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.
"""
while True:
    nota = int(input("Entre com uma nota de [1 - 10]: "))
    if(nota < 1 or nota > 10):
                print("Nota inválida!")
                continue
    break
print("Nota", nota ," foi aceita!")

