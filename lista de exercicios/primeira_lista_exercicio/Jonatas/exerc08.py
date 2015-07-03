#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

vHora = float(input("Digite o salário p/ hora: "))
nHoras = int(input("Digite o número de horas trabalhadas no mês: "))

print('Ao final do mês o sálario equivale a R${valorFinal:.2f}'.format(valorFinal=(vHora*nHoras)))
