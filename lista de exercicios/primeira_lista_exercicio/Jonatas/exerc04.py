#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

soma = 0

for i in range(1,5):
    soma = soma + int(input("Digite a nota do {bim}º bimestre: ".format(bim=i)))

print("A média final é {med}".format(med=(soma/4)))
