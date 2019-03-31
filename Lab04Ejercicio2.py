#Abel Zavaleta 15-11574
#Este programa calcula el MCD de dos numeros 

A=int(input("Ingrese un numero A")) #Pido un numero A para calcular el MCD
B=int(input("Ingrese un numero B")) #Pido un numero B para calcular el MCD
a=A #Variable auxiliar para manipular el numero A
b=B #Variabale auxliar para manipular el nummero B


assert(A==a and b==B and a>=0 and b>=0)


if(a==0):
	print("El MCD de",A,"y",B,"es",b)
elif(b==0):
	print("El MCD de",A,"y",B,"es",a)
else:
	while(a!=b):
		if (a<b):
			b=b-a
		elif(b<a):
			a=a-b
	print("El MCD de",A,"y",B,"es",a)

assert(b>=0 or a>=0 or a==b)
