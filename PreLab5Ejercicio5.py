#Abel Zavaleta
#15-11574
 
class Estudiante:
	nombre=""
	edad=0
	indice=0
	
N=(int(input("Ingrese en numero de Estudiantes a ingresar"))) 
grupo=[Estudiante() for x in range(0,N)]

for i in range(0,N):
	print("Estudiante", i+1)
	grupo[i].nombre=(input("Ingrese nombre del Estudiante "))
	grupo[i].edad=(int(input("Ingrese la edad del Estudiante ")))
	grupo[i].indice=(int(input("Ingrese el indice del Estudiante ")))	

PromE,PromI=0,0
assert (all(0<grupo[i].indice<=5 for i in range(0,N)) and  all(0<len(grupo[i].nombre) for i in range (0,N)))
for i in range(0,N):
	PromE=PromE+grupo[i].edad
	PromI=PromI+grupo[i].indice
print("El promedio de edad es ",PromE/N,"Y el de indice es ",PromI/N)
