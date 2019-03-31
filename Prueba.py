
v,a,m,am,r=1200,6600,33000,155000,510000

def Cal(M,R):
	i,ren,saldo,dias=0,8280,0,0
	while(ren<=35000):
		saldo+=ren*24
		if saldo>=M*100:
			i+=1
			saldo=saldo-M*100
			ren+=R
		dias+=1
	print(dias,ren,saldo,i)
print("Dias,Ren,Saldo,N")
Cal(v,60)
Cal(a,360)
Cal(m,1980)
Cal(am,10020)
Cal(r,35040)

i,ren,saldo,dias,j=0,8280,0,0,0
while(ren<=35000):
	saldo+=ren*24
	if saldo>=m*100:
		i+=1
		saldo=saldo-m*100
		ren+=1980
		print(dias-j,dias)
		j=dias
	dias+=1
print(dias,ren,saldo,i)