#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

l = float(input('Digite o valor do lado do quadrado(cm): '))
area = l**2

print('O quadrado tem área {area}cm² e o dobro desta área equivale a {dobro}cm²'.format(area=area, dobro=(area*2)))
