#Abel Zavaleta
#15-11574


N=(int(input("Ingrese el orden de la matriz N")))
A=[[int(input("M["+str(i)+","+str(j)+"]=")) for j in range(0,N)] for i in range(0,N)]
D,i,j=True,0,0
Cota=N-i

#Verificacion de invariante y cota en el inicio
assert(N>=0)
assert(D==all(A[k][z]==0 for k in range(0,i)) for z in range(0,j) if i!=j and 0<=k<i and 0<=z<j)
assert(Cota>=0)
while i<N and D:
	Cota2=N-j
	while j<N and D:
		if i!=j and A[i][j]!=0:
			D=False 
		j=j+1
		#Verificacion de invariante y cota en cada iteracion
		assert(D==all(A[k][z]==0 for k in range(0,i)) for z in range(0,j) if i!=j and 0<=k<i and 0<=z<j)
		assert(Cota2>N-j)
		Cota2=N-j
		assert(Cota2>=0)
	i,j=i+1,0
	#Verificacion de invariante y cota en cada iteracion
	assert(D==all(A[k][j]==0 for k in range(0,i))for j in range(0,N) if i!=j and 0<=k<i)
	assert(Cota>N-i)
	Cota=N-i
	assert(Cota>=0)
#Verificamos postcondicion	
assert (D==all(A[i][j]==0 for i in range(0,N)) for j in range(0,N) if i!=j and 0<=j<N and 0<=i<N)

for j in range(0,N):
	print (A[j])
	
if D:
	print("La matriz es diagonal")
else: 
	print("La matriz NO es diagonal")
