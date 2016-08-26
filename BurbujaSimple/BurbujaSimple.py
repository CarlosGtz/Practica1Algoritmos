#!/usr/bin/python

from time import time
import random


array = []
TAM = 11000

def llenaArreglo(p):
	for i in range(TAM):
		p.append(random.randint(1, 5000000))

def BurbujaSimple(A,n):
	for i in range(n):
		for j in range(n-1):
			if A[j] > A[j+1]:
				temp = A[j]
				A[j] = A[j+1]
				A[j+1] = temp

def writeFile(fTime):
	archivo = open("BurbujaSimple.txt", "r+")
	contenido = archivo.read()
	final_de_archivo = archivo.tell()	 
	archivo.write(fTime+" "+str(TAM)+"\n")
	archivo.seek(final_de_archivo)
	archivo.close()

llenaArreglo(array)
init_time = time()
BurbujaSimple(array,len(array))
final_time = time()
e_time = final_time - init_time
str_time = str("%.15f" % e_time)
writeFile(str_time)
print str_time

