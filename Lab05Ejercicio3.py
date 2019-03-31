#Abel Zavaleta
#15-11574
 
class Estudiante:
	nombre=""
	P1,P2,P3=0,0,0
	indice=0
	prom=0
	nota=0
N,i=10,0
Clase=[Estudiante() for i in range(N)]

Clase[0].nombre,Clase[0].P1,Clase[0].P2,Clase[0].P3="Carlos1",30,35,35
Clase[1].nombre,Clase[1].P1,Clase[1].P2,Clase[1].P3="Juan1",1,5,6
Clase[2].nombre,Clase[2].P1,Clase[2].P2,Clase[2].P3="Carlos2",25,30,5
Clase[3].nombre,Clase[3].P1,Clase[3].P2,Clase[3].P3="Juan2",2,32,8
Clase[4].nombre,Clase[4].P1,Clase[4].P2,Clase[4].P3="Carlos3",15,23,15
Clase[5].nombre,Clase[5].P1,Clase[5].P2,Clase[5].P3="Juan3",12,35,0
Clase[6].nombre,Clase[6].P1,Clase[6].P2,Clase[6].P3="Carlos4",17,20,5
Clase[7].nombre,Clase[7].P1,Clase[7].P2,Clase[7].P3="Juan4",23,5,35
Clase[8].nombre,Clase[8].P1,Clase[8].P2,Clase[8].P3="Carlos5",2,5,8
Clase[9].nombre,Clase[9].P1,Clase[9].P2,Clase[9].P3="Juan5",6,3,5

cota=N-i
#Verificacion de invariante y cota en el inicio
assert (all(Clase[z].indice<=5 and Clase[z].nota<=100 and 0<len(Clase[z].nombre) for z in range(0,i)) and 0<=i<=N)
assert (all(Clase[z].nota==Clase[z].P1+Clase[z].P2+Clase[z].P3 and Clase[z].prom==Clase[z].nota/3 for z in range(0,i)) and 0<=i<=N)
assert(cota>=0)
for i in range(N):
	#Verificacion de invariante y cota en cada iteracion
	assert (all(Clase[z].indice<=5 and Clase[z].nota<=100 and 0<len(Clase[z].nombre) for z in range(0,i)) and 0<=i<N)
	assert (all(Clase[z].nota==Clase[z].P1+Clase[z].P2+Clase[z].P3 and Clase[z].prom==Clase[z].nota/3 for z in range(0,i)) and 0<=i<N)
	Clase[i].nota=Clase[i].P1+Clase[i].P2+Clase[i].P3
	Clase[i].prom=Clase[i].nota/3
	
	if Clase[i].nota>=85:
		Clase[i].indice=5
	elif Clase[i].nota>=70:
		Clase[i].indice=4
	elif Clase[i].nota>=50:
		Clase[i].indice=3
	elif Clase[i].nota>=30:
		Clase[i].indice=2
	else:
		Clase[i].indice=1
#PostCondicion
assert (all(Clase[i].indice<=5 and Clase[i].nota<=100 and 0<len(Clase[i].nombre) for i in range(0,N)))
assert (all(Clase[i].nota==Clase[i].P1+Clase[i].P2+Clase[i].P3 and Clase[i].prom==Clase[i].nota/3 for i in range(0,N)))

for i in range(N):

	print(Clase[i].nombre)
	print("Parcial1 Parcial2 Parcial3 Prom Nota Indice ")
	print(Clase[i].P1,"\t",Clase[i].P2,"\t ",Clase[i].P3,"\t ",'%.2f'%Clase[i].prom," ",Clase[i].nota,"  ",Clase[i].indice)
