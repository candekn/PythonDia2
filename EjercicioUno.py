alumnos = []
while(True):
    print ("\n\n\nBienvenido. Seleccione lo que desea realizar: ")
    print ("1. Mostrar lista de alumnos")
    print ("2. Agregar nuevo alumno")
    print ("3. Alumnos con más de 3 cursos")
    print ("4. Salir")
    op = input("Ingrese seleccion: ")
    if (op=="1"):
        for a in alumnos:
            print(a)
    elif(op=="2"):
        nombre = input("Ingrese nombre del alumno: ")
        curso = input("Ingrese cantidad de cursos: ")
        curso = int(curso)
        alumnos.append([nombre,curso])
    elif(op=="3"):
        for a in alumnos:
            if(a[1]>3):
                print(a[0])
    elif(op=="4"):
        print("Adios. Que tenga un buen día")
        break
    else:
        print("La opción ingresada es inválida")
        

        
    