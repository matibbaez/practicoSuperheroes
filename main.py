from superheroes.personajes import lista_personajes
from funciones.funciones import mostrar_menu, mostrar_superheroes, altura_superheroes, mas_alto, mas_bajo, promedio_altura, mas_pesado, menos_pesado

while True:
    mostrar_menu()
    opcion = input("Elija una opción (1-7, o 8 para salir): ")

    if opcion == '1':
        mostrar_superheroes(lista_personajes)
    elif opcion == '2':
        altura_superheroes(lista_personajes)
    elif opcion == '3':
        mas_alto(lista_personajes)
    elif opcion == '4':
        mas_bajo(lista_personajes)
    elif opcion == '5':
        promedio_altura(lista_personajes)
    elif opcion == '6':
        mas_pesado(lista_personajes)
    elif opcion == '7':
        menos_pesado(lista_personajes)
    elif opcion == '8':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Elija una opción del 1 al 8.")
        input("Presione Enter para continuar...")
