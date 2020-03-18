##Funcion Promedio
def promedio(lista):
    suma = 0
    for l in lista:
        suma = suma + l
    p = suma / len(lista)
    return p

####--Principal--####
alumnos = [[8,2,10],[3,7,9],[8,8,7],[4,6,10]]
i=1 #Esto es para que se diferencien los alumnos
notas = [] #lista de notas

for a in alumnos: #recorro alumno
    prom = promedio(a) 
    notas.append(prom)
    if(prom>=7):
        print("Alumno" , i,"Promedio:",prom, "Aprobado")
    else:
        print("Alumno" , i,"Promedio:",prom, "Desaprobado")
    i=i+1 #i= Alumno 1, Alumno 2... etc

promeNotas=0 #promedio de notas =0

promeNotas = promedio(notas) #promedio general

print("\n")

if(promeNotas>=7):
    print("Es un buen curso, su promedio de notas es de:",promeNotas)
else:
    print("El curso fue malo. Su promedio es de:",promeNotas)
