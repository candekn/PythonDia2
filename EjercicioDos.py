def sumar(a,b):
    return (a+b)

#####Main######
while(True):
    a = input("Ingrese numero 1: ")
    a = int(a)
    b= input("Ingrese numero 2: ")
    b= int(b)
    r = sumar(a,b)
    print("El resultado es: ",r)
    op = input("\nDesea Continuar? y/n: ")
    if(op=="s"):
        print("Adios.")
        break