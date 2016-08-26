#!/usr/bin/python

from time import time
import random

array = []
tam = 100000


def llenaArreglo(p):
	for i in range(tam):
		p.append(random.randint(1, 5000000))
	
def Producto2Mayores(A,n):
	if (A[0] > A[1]):
		mayor1 = A[0]
		mayor2 = A[1]
	else:
		mayor1 = A[1]
		mayor2 = A[0]
	i = 3
	while i <= n:
		if (A[i] > mayor1):
			mayor2 = mayor1
			mayor1 = A[i]
		elif(A[i] > mayor2):
			mayor1 = A[i]
		i += 1
	return mayor1 * mayor2

def writeFile(fTime):
	archivo = open("Producto2Mayores.txt", "r+")
	contenido = archivo.read()
	final_de_archivo = archivo.tell()	 
	archivo.write(fTime+" "+str(tam)+"\n")
	archivo.seek(final_de_archivo)
	archivo.close()


llenaArreglo(array)
init_time = time()
Producto2Mayores(array,tam-1)
final_time = time()
e_time = final_time - init_time
str_time = str("%.20f" % e_time)
print str_time
writeFile(str_time)







