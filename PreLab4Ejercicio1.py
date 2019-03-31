#Abel Zavaleta 15-11574
#15-11574


#Definimos el cuantificador producto para python
def prod( iterable ):
	p= 1
	for n in iterable:
		p *= n
	return p

print("Este programa calcula la suma de los factoriales desde 0 hasta N")
N=int(input("Ingrese el numero factorial"))
suma,fact,k=0,1,0 #Inicializamos la variable
cota=N+1-k #Definimos la cota

#Verificacion de invariante y cota al inicio
assert(N>=0)
assert(0<=k<=N+1 and suma == sum ( prod(j for j in range (1,i+1))  for i in range(0,k)) and fact== prod(j for j in range(1,k)))
assert(cota>=0)
 
while (k<=N):
	if(k>0):
		fact=fact*k
	suma=suma+fact
	k=k+1
	#Verificacion de invariante y cota en cada iteracion
	assert(0<=k<=N+1 and suma == sum ( prod(j for j in range (1,i+1))  for i in range(0,k)) and fact== prod(j for j in range(1,k)))
	assert(cota>N+1-k)
	cota=N+1-k
	assert(cota>=0)
	
#Verificamos la postcondicion
assert(suma==sum(prod(j for j in range(1,i+1)) for i in range(0,k)))
	
print("El resultado es",suma)
