#!/usr/bin/env python3
"""Modulus Readme Creator"""
import os
import re


"""
Debe tener: 
- Nombre del proyecto - Es el primer párrafo
- Objetivos de aprendizaje
- Tarea - Tabla archivo - Descripción
- About me y datos de contacto
"""

titulo = ''
objetivos = []
tareas = []
archivos = []

archi = re.compile(r'File:*')
tarea = re.compile(r'\d*\.')
iniob = re.compile(r'General\n*')
finob = re.compile(r'Requirements')

with open('origen', 'r', encoding='utf-8') as f:
    lines = f.readlines()

inifin = 0

for i, line in enumerate(lines):
    titulo = lines[0]
    if lines[i] == 'General\n' and lines[i - 1] != 'Requirements\n':
        inifin = 1
        print("Valor de control {}, linea: {}".format(inifin, line))
    if lines[i] == 'General\n' and lines[i - 1] == 'Requirements\n':
        inifin = 0
        print("Valor de control {}, linea: {}".format(inifin, line))
    if inifin == 1:
        objetivos.append(line)
    if tarea.match(line):
        tareas.append(line)
    if archi.match(line):
        archivos.append(line.split()[1])

# print(lines)
print(titulo)
print(objetivos)
print(tareas)
print(archivos)