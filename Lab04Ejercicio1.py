#Abel Zavaleta 15-11574
#Este programa realiza calculos dependiendo de un valor C en un intervalor A,B

def prod( iterable ):
	p= 1
	for n in iterable:
		p *= n
	return p


print("Sea A<B")
A=int(input("Ingrese el numero A"))
B=int(input("Ingrese el numero B"))
C=int(input("Ingrese el numero C"))
ProdAcum=1
cont=0
cota=B-A+1

if (A==0):
	A=A+1
elif (B==0):
	B=B+1

assert(A>0 and B>0 and C>=0 and A<B)
assert(cota>=0)
assert(0<A<=B+1 and ProdAcum==prod(j for j in range (A,B+1) if (j%2==0 and j%3==0))) 

if C==0:
	while(A<=B):
		if(A%2==0 and A%3==0):
			ProdAcum=A*ProdAcum
		A=A+1
		#assert(0<A<=B+1 and ProdAcum==prod(j for j in range (A,B+1) if (A%2==0 and A%3==0)))
		assert(cota>B-A+1)
		cota=B-A+1
		assert(cota>=0)
	print (ProdAcum)
elif C==1:
	while(A<=B):
		if(A%3==0 or A%5==0):
			cont=cont+1
		A=A+1
		assert(cota>B-A+1)
		cota=B-A+1
		assert(cota>=0)
	print(cont)
else:
	print ("-1")
	
assert(B>=0 and A>=0 )
