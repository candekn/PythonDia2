import time

def sumar(a,b):
    return (a+b)

def restar(a,b):
    return (a-b)

def multiplicar(a,b):
    return (a*b)

def dividir(a,b):
    if(b==0):
        print("No se puede dividir por cero")
    else:
        return(a/b)

def menu():
    print("\nBienvenido a la calculadora. Seleccione lo que desea hacer: ")
    print("1-Sumar")
    print("2-Restar")
    print("3-Multiplicar")
    print("4-Dividir")
    print("5-Salir")
    return (input("\nIngrese opcion: "))

while True:
    op = menu()
    time.sleep(1)
    if(op=="5"):
        print("Adios.")
        break
    a = input("Ingrese numero 1: ")
    a = float(a)
    b = input("Ingrese numero 2: ")
    b = float(b)
    time.sleep(1)
    if(op=="1"):
        resultado = sumar(a,b)
    elif(op=="2"):
        resultado = restar(a,b)
    elif(op=="3"):
        resultado = multiplicar(a,b)
    elif(op=="4"):
        resultado = dividir(a,b)
    else:
        print("Opcion Incorrecta!")
    print("El resultado es: ",resultado,"\n\n")
    time.sleep(1)
    
    