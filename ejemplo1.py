#
# Ejemplo1.py
#
# DESCRIPCION: Programa que dados tres enteros a,b y c,
# calcula la division de a*a entre (b-c). Dicho resultadohttps://cchang.wordpress.com/
# es almacenado en d.https://cchang.wordpress.com/
#
# Autor: 
#	Prof. Rosseline Rodriguez
#
# Ultima modificacion: 9/01/2018
#

# VARIABLES:
#	A: int   // ENTRADA: Valor cuyo cuadrado sera el dividendo
#	B: int   // ENTRADA: Parte del divisor
#	C: int   // ENTRADA: Parte del divisor
#	d: float // SALIDA: Resultado de la division

# Valores iniciales:
A = 25
B = 10
C = 25
	
# Precondicion: 
assert((B-C) != 0)

# Calculos:
d = A*A / (B-C)	

# Postcondicion: 
assert(d ==(A*A)/(B-C))

# Salida:
print("El resultado es ")
print(d)
