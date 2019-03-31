#Abel Zavaleta
#15-11574

M=(int(input("Ingrese el numero del maximo grado")))
A=[int(input("Ingrese el coeficiente "+str(i)+":")) for i in range(M+1)]


def MostarPolinomio(Lista,num):
	i=0
	cota=num+1-i
	print("P(x)=",end="")
	#Precondicion
	assert(all(len(str(Lista[i]))>0 for i in range (0,num+1))and 0<=i<=num+1)
	#Verificacion de la cota 
	assert(num>=0)
	assert(cota>=0)
	for i in range(num+1):
		if(i==0):
			print(Lista[i],end='+')
		elif (i==1):
			print(str(Lista[i])+"x",end='')
		else:
			print("+"+str(Lista[i])+"x^"+str(i),end='')

MostarPolinomio(A,M)
			
