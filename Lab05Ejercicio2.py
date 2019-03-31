#Abel Zavaleta
#15-11574

A=[[1,2],[3,4]]
T=[[1,3],[2,4]]
Es,i,j,N=True,0,0,2
cota=N-i

#Verificacion de invariante y cota en el inicio
assert(N>=0)
assert(Es==all(A[k][z]==T[z][k] for k in range(0,i) for z in range(0,j)) and 0<=i<=N and 0<=j<=N)
assert(cota>=0)
while i<N and Es:
	cota2=N-j
	assert(N>=0)
	assert(cota>=0)
	while j<N and Es:
		if A[i][j]!=T[j][i]:
			Es=False
		j=j+1
		#Verificacion de invariante y cota en cada iteracion
		assert(Es==all(A[k][z]==T[z][k] for k in range(0,i) for z in range(0,j)) and 0<=i<=N  and 0<=j<=N)
		assert(cota2>N-j)
		cota2=N-j
		assert(cota>=0)
	i,j=i+1,0
	#Verificacion de invariante y cota en cada iteracion
	assert(Es==all(A[k][j]==T[j][k] for k in range (0,i) for j in range(0,N)) and 0<=i<=N and 0<=j<=N)
	assert(cota>N-i)
	cota=N-i
	assert(cota>=0)

print(Es)
for i in range (2):
	print(A[i]," ",T[i])

