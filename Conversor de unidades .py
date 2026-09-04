# ============================================
# MINI CONVERSOR DE UNIDADES CON PILAS
# ============================================

# Pila para almacenar las conversiones
pila_conversiones = []

def guardar_conversion(conversion):
    pila_conversiones.append(conversion)
    print("Conversión guardada en la pila.")


def celsius_a_fahrenheit():
    celsius = float(input("Ingrese la temperatura en Celsius: "))

    resultado = (celsius * 9 / 5) + 32

    conversion = f"{celsius} °C = {resultado:.2f} °F"

    print("Resultado:", conversion)

    guardar_conversion(conversion)


def kilogramos_a_libras():
    kilogramos = float(input("Ingrese el peso en kilogramos: "))

    resultado = kilogramos * 2.20462

    conversion = f"{kilogramos} kg = {resultado:.2f} lb"

    print("Resultado:", conversion)

    guardar_conversion(conversion)


def kilometros_a_millas():
    kilometros = float(input("Ingrese la distancia en kilómetros: "))

    resultado = kilometros * 0.621371

    conversion = f"{kilometros} km = {resultado:.2f} mi"

    print("Resultado:", conversion)

    guardar_conversion(conversion)


def ver_historial():

    if len(pila_conversiones) == 0:
        print("La pila está vacía.")

    else:
        print("\n===== HISTORIAL DE CONVERSIONES =====")

        for i in range(len(pila_conversiones) - 1, -1, -1):
            print(pila_conversiones[i])


def ver_ultima_conversion():

    if len(pila_conversiones) == 0:
        print("La pila está vacía.")

    else:
        print("\nÚltima conversión:")
        print(pila_conversiones[-1])


def deshacer_conversion():

    if len(pila_conversiones) == 0:
        print("No hay conversiones para eliminar.")

    else:
        conversion = pila_conversiones.pop()

        print("\nSe eliminó la última conversión:")
        print(conversion)


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

while True:

    print("\n===================================")
    print("       CONVERSOR DE UNIDADES")
    print("===================================")
    print("1. Celsius a Fahrenheit")
    print("2. Kilogramos a Libras")
    print("3. Kilómetros a Millas")
    print("4. Ver historial")
    print("5. Ver última conversión")
    print("6. Deshacer última conversión")
    print("7. Salir")
    print("===================================")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        celsius_a_fahrenheit()

    elif opcion == "2":
        kilogramos_a_libras()

    elif opcion == "3":
        kilometros_a_millas()

    elif opcion == "4":
        ver_historial()

    elif opcion == "5":
        ver_ultima_conversion()

    elif opcion == "6":
        deshacer_conversion()

    elif opcion == "7":
        print("Gracias por utilizar el conversor.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")