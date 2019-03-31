#Abel Zavaleta 15-11574
#15-11574

print("Este programa calcula cuantos divisores tiene un numero N por favor")
N=int(input("Ingrese un numero entero diferente de cero"))
cuenta,i=0,1 #Inicializamos las variables
cota=N-i+2 #Definimos la cota

#Verificacion de invariante y cota al inicio
assert(N>0)
assert(0<i<=N+1 and cuenta==sum(1 for j in range (1,i) if (N%j==0)))
assert(cota>=0)
 
while (i<=N):
	if(N%i==0):
		cuenta=cuenta+1
	i=i+1
	#Verificacion de invariante y cota en cada iteracion
	assert(0<i<=N+1 and cuenta==sum(1 for j in range (1,i) if (N%j==0)))
	assert(cota>N-i+2)
	cota=N-i+2
	assert(cota>=0)
#Verificacion de la postcondicion 
assert(cuenta==sum( 1 for x in range(1,N+1) if (N%x==0)))
print("El numero de divisores que posee el numero",N,"es",cuenta)
