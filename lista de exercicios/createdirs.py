#!/usr/bin/env python3.4
#-*- coding: utf-8 -*-

from os import makedirs, mkdir
from sys import argv

rootdir = argv[1] # Nome da pasta raiz
namedirs = argv[2] # Nome do arquivo com nomes dos participantes

mkdir(rootdir) # Cria pasta raiz

f = open(namedirs) # Abre arquivo

for l in f.readlines(): # Laco para criacao das pastas
    makedirs('{rootdir}/{dir}'.format(rootdir=rootdir, dir=l.strip()))
