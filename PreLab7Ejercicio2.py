#Abel Zavaleta
#15-11574
 
class Estudiante:
	nombre=""
	P1,P2,P3=0,0,0
	indice=0
	prom=0
	nota=0
N=10

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

def CalcularDatos(Lista,num):
	i=0
	cota=num-i
	#Verificacion de invariante y cota en el inicio
	assert (all(Lista[z].indice<=5 and Lista[z].nota<=100 and 0<len(Lista[z].nombre) for z in range(0,i)) and 0<=i<=num)
	assert (all(Lista[z].nota==Lista[z].P1+Lista[z].P2+Lista[z].P3 and Lista[z].prom==Lista[z].nota/3 for z in range(0,i)) and 0<=i<=num)
	assert(cota>=0)
	for i in range(num):
		#Verificacion de invariante y cota en cada iteracion
		assert (all(Lista[z].indice<=5 and Lista[z].nota<=100 and 0<len(Lista[z].nombre) for z in range(0,i)) and 0<=i<num)
		assert (all(Lista[z].nota==Lista[z].P1+Lista[z].P2+Lista[z].P3 and Lista[z].prom==Lista[z].nota/3 for z in range(0,i)) and 0<=i<num)
		Lista[i].nota=Lista[i].P1+Lista[i].P2+Lista[i].P3
		Lista[i].prom=Lista[i].nota/3
		
		if Lista[i].nota>=85:
			Lista[i].indice=5
		elif Lista[i].nota>=70:
			Lista[i].indice=4
		elif Lista[i].nota>=50:
			Lista[i].indice=3
		elif Lista[i].nota>=30:
			Lista[i].indice=2
		else:
			Lista[i].indice=1
	#PostCondicion
	assert (all(Lista[i].indice<=5 and Lista[i].nota<=100 and 0<len(Lista[i].nombre) for i in range(0,num)))
	assert (all(Lista[i].nota==Lista[i].P1+Lista[i].P2+Lista[i].P3 and Lista[i].prom==Lista[i].nota/3 for i in range(0,num)))
CalcularDatos(Clase,N)

for i in range(N):

	print(Clase[i].nombre)
	print("Parcial1 Parcial2 Parcial3 Prom Nota Indice ")
	print(Clase[i].P1,"\t",Clase[i].P2,"\t ",Clase[i].P3,"\t ",'%.2f'%Clase[i].prom," ",Clase[i].nota,"  ",Clase[i].indice)
