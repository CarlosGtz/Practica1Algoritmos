#!/usr/bin/python

from time import time
import random

array = []
TAM = 25500

def llenaArreglo(p):
	for i in range(TAM):
		p.append(random.randint(1, 5000000))

def OrdenamientoInterCambio(a,n):
	for i in range(n):
		j = i + 1
		while j < n:
			if a[j] < a[i]:
				temp = a[i]
				a[i] = a[j]
				a[j] = temp
			j += 1
			


def writeFile(fTime):
	archivo = open(" OrdenamientoIntercambio.txt", "r+")
	contenido = archivo.read()
	final_de_archivo = archivo.tell()	 
	archivo.write(fTime+" "+str(TAM)+"\n")
	archivo.seek(final_de_archivo)
	archivo.close()


llenaArreglo(array)
init_time = time()
OrdenamientoInterCambio(array,TAM)
final_time = time()
e_time = final_time - init_time
str_time = str("%.20f" % e_time)
print str_time
writeFile(str_time)