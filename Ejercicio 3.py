pila = []


def agregar_departamento():
    departamento = input("Ingrese el nombre del departamento: ")
    pila.append(departamento)
    print("Departamento agregado correctamente.")


def remover_departamento():
    if pila:
        departamento = pila.pop()
        print("Departamento removido:", departamento)
    else:
        print("La pila está vacía.")


def mostrar_departamentos():
    if pila:
        print("\nDepartamentos de la pila:")
        for departamento in pila:
            print(departamento)
    else:
        print("La pila está vacía.")


def menu():
    while True:
        print("\n*** PILA DE DEPARTAMENTOS ***")
        print("1. Agregar departamento")
        print("2. Remover departamento")
        print("3. Mostrar departamentos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_departamento()
        elif opcion == "2":
            remover_departamento()
        elif opcion == "3":
            mostrar_departamentos()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")


menu()