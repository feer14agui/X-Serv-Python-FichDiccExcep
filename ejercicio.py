#!/usr/bin/python
# -*- coding: utf-8 -*-

#Fernando Aguilar Santos

fd = open('/etc/passwd', 'r')

Dicc = {}							#Declaro el diccionario
lineas = fd.readlines()			
fd.close()

for linea in lineas:
	elementos = linea.split(':')
	Dicc[elementos[0]]= elementos[-1][:-1] 			#Guardo cada key y value en el diccionario(1 a 1)

try:

	print Dicc["root"]
	print Dicc["imaginario"]

except :			#elevo la excepción para el caso de que no encuentro la key

	print "key no encontrada"
