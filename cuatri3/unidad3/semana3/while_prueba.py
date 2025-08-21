def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Saludar")
    print("2. Mostrar número")
    print("3. Salir")

opcion = 0
while opcion != 3:
    mostrar_menu()
    try:
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            print("¡Hola, Alan!")
        elif opcion == 2:
            print("Tu número favorito es el 42.")
        elif opcion == 3:
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")