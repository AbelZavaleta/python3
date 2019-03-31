#Abel Zavaleta 15-11574
# Este programa calcula el producto de los digitos de un numero diferentes de cero 

A=int(input("Ingrese un numero A")) #Numero para calcular
a=A #Guardo mi numero A en una variable auxiliar para manipularlo  
i,n=1,0 # Defino mis variables auxiliares que me ayudaran a contar en las interacion
b=1 #Variable que me guarda el resultado en cada iteracion


while(a>0): 
	if(a%10**i!=0): 
		a=a-10**(i-1)
		n=n+1
		if(a==0):
			print("El resultado del producto de los digitos diferentes de cero de un numero es:")
			print("Para el numero", A,"el resultado es",b*n)
	elif(a%10**i==0):
		if(n!=0):
			b=b*n
			n=0
		i=i+1
