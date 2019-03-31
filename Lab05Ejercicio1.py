#Abel Zavaleta
#15-11574

M=(int(input("Ingrese el numero del maximo grado")))
A=[int(input("Ingrese el coeficiente "+str(i)+":")) for i in range(M+1)]
i=0
cota=M+1-i
print("P(x)=",end="")
#Precondicion
assert(all(len(str(A[i]))>0 for i in range (0,M+1))and 0<=i<=M+1)
#Verificacion de la cota 
assert(M>=0)
assert(cota>=0)
for i in range(M+1):
	if(i==0):
		print(A[i],end='+')
	elif (i==1):
		print(str(A[i])+"x",end='')
	else:
		print("+"+str(A[i])+"x^"+str(i),end='')

		
