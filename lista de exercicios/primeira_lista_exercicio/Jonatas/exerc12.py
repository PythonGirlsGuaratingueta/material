#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

n1 = int(input("Digite o primeiro número(int): "))
n2 = int(input("Digite o segundo número(int): "))
n3 = int(input("Digite o terceiro número(float): "))

print("\nA) O produto do dobro do primeiro com metade do segundo: {a}\n\
B) A soma do triplo do primeiro com o terceiro: {b}\n\
C) O terceiro elevado ao cubo: {c}".format(a=((n1*2)*(n2/2)), b=(n1*3+n3), c=(n3**3)))
