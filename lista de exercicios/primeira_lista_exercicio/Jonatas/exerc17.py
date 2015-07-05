#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

h = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo(M/F): ")

peso = (72.7*h)-58 if sexo.upper() == "M" else (62.1*h)-44.7

print("Seu peso ideal é {:.2f}kg".format(peso))
