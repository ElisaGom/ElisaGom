import librarys.mixmodulo as cal

while True:

    print('1- Suma \n2- Resta \n3- Miltiplicacion \n4- Divicion \n0- Para salir')
    operacion = int(input("Ingrese el numero de la operacion: "))
    n1 = float(input('Ingresa el 1 numero: '))
    n2 = float(input('Ingresa el 1 numero: '))
    if operacion == 1:
        print(cal.suma(n1, n2))
        print("")
    elif operacion == 2:
        print(cal.resta(n1, n2))
        print("")
    elif operacion == 3:
        print(cal.multiplicacion(n1, n2))
        print("")
    elif operacion == 4:
        print(cal.divicion(n1, n2))
        print("")

    else:
        operacion == 0
        print('Gracias por usar la calculadora')
        break