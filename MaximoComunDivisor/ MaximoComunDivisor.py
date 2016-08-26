#!/usr/bin/python

from time import time
tam = 50000
def  MaximoComunDivisor(m ,n):
	a = max(n,m)
	b = min(n,m)
	residuo = 1
	while residuo > 0:
		residuo = a % b
		a = b
		b = residuo
	MaximoComunDivisor = a
	return MaximoComunDivisor

def writeFile(fTime):
	archivo = open("MaximoComunD.txt", "r+")
	contenido = archivo.read()
	final_de_archivo = archivo.tell()	 
	archivo.write(fTime+" "+str(tam)+"\n")
	archivo.seek(final_de_archivo)
	archivo.close()

init_time = time()
res = MaximoComunDivisor(129970,tam)
final_time = time()
e_time = final_time - init_time
print "MCD: "+str(res)
str_time = str("%.15f" % e_time)
print str_time
writeFile(str_time)
