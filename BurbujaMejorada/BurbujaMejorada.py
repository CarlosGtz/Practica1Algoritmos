#!/usr/bin/python

from time import time
import random


array = []
TAM = 1200

def llenaArreglo(p):
	for i in range(TAM):
		p.append(random.randint(1, 1000))

def BurbujaMejorada(A,n):
	for i in range(n):
		j = 0
		while j < i:
			if A[i] < A[j]:
				temp = A[j]
				A[j] = A[i]
				A[i] = temp
			j += 1

def writeFile(fTime):
	archivo = open("BurbujaMejorada.txt", "r+")
	contenido = archivo.read()
	final_de_archivo = archivo.tell()	 
	archivo.write(fTime+" "+str(TAM)+"\n")
	archivo.seek(final_de_archivo)
	archivo.close()

llenaArreglo(array)
init_time = time()
BurbujaMejorada(array,len(array))
final_time = time()
e_time = final_time - init_time
str_time = str("%.20f" % e_time)
writeFile(str_time)
print "Time: %.20f" % e_time
				
