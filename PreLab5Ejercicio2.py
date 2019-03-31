#Abel Zavaleta
#15-11574

N=(int(input("Ingrese el numero N de numeros a calcular")))
A = [ int(input("A[" + str(i) + "]= ")) for i in range(0,N) ]
suma,i=0,0
cota=N-i

assert(N>0)
assert(suma==sum(A[j] for j in range(0,i)) and 0<=i<N)
assert(Cota>=0)	

for i in range(0,N):
	assert(suma==sum(A[j] for j in range(0,i)) and 0<=i<N)	
	suma=suma+A[i]
	
assert(suma==sum(A[i] for i in range(0,N)))	
print("La suma es", suma)
