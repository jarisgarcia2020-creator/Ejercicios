pila = []

def agregar_numero():
    numero = int(input("Ingrese un número entero: "))
    pila.append(numero)
    print("Número agregado correctamente.")



def contar_elementos():
    cantidad = len(pila)
    print("Cantidad de elementos:", cantidad)



def mostrar_elementos():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("Elementos de la pila:")
        for numero in pila:
            print(numero)



def calcular_promedio():
    if len(pila) == 0:
        print("No hay números para calcular el promedio.")
    else:
        suma = sum(pila)
        promedio = suma / len(pila)
        print("El promedio es:", promedio)


# Programa principal
while True:

    print("\n*** MENÚ DE OPCIONES ***")
    print("1. Agregar números")
    print("2. Contar elementos")
    print("3. Mostrar todos los elementos")
    print("4. Promedio de todos los números")
    print("5. Salir del sistema")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        agregar_numero()

    elif opcion == 2:
        contar_elementos()

    elif opcion == 3:
        mostrar_elementos()

    elif opcion == 4:
        calcular_promedio()

    elif opcion == 5:
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")