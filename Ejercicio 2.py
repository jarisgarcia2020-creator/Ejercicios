pila = []


def agregar_nombre():
    nombre = input("Ingrese el nombre: ")
    pila.append(nombre)
    print("Nombre agregado correctamente.")


def eliminar_nombre():
    if pila:
        nombre = pila.pop()
        print("Nombre eliminado:", nombre)
    else:
        print("La pila está vacía.")


def mostrar_cima():
    if pila:
        print("Elemento en la cima:", pila[-1])
    else:
        print("La pila está vacía.")


def buscar_nombre():
    nombre = input("Ingrese el nombre que desea buscar: ")

    if nombre in pila:
        print("El nombre se encuentra en la pila.")
    else:
        print("El nombre no se encuentra en la pila.")


def contar_elementos():
    print("Cantidad de elementos:", len(pila))


def mostrar_elementos():
    if pila:
        print("Elementos de la pila:")
        for nombre in pila:
            print(nombre)
    else:
        print("La pila está vacía.")


def limpiar_pila():
    pila.clear()
    print("La pila ha sido limpiada.")


def menu():
    while True:
        print("\n*** MENÚ DE OPCIONES ***")
        print("1. Agregar un nombre a la Pila")
        print("2. Eliminar un nombre de la Pila")
        print("3. Mostrar el último elemento en la Cima")
        print("4. Buscar un elemento en la Pila")
        print("5. Contar cuantos elementos tiene la Pila")
        print("6. Mostrar todos los elementos de la pila")
        print("7. Limpiar la Pila")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_nombre()
        elif opcion == "2":
            eliminar_nombre()
        elif opcion == "3":
            mostrar_cima()
        elif opcion == "4":
            buscar_nombre()
        elif opcion == "5":
            contar_elementos()
        elif opcion == "6":
            mostrar_elementos()
        elif opcion == "7":
            limpiar_pila()
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")


menu()