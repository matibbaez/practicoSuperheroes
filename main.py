from superheroes.personajes import lista_personajes
from funciones.funciones import *

menu = input("Elija un menu (1 o 2): ")
if menu == "1":
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
else:
    while True:
        mostrar_segundo_menu()
        opcion = input("Elija una opción (1-11, o 12 para salir): ")

        if opcion == '1':
            genero_m(lista_personajes)
        elif opcion == '2':
            genero_f(lista_personajes)
        elif opcion == '3':
            mas_alto_m(lista_personajes)
        elif opcion == '4':
            mas_alto_f(lista_personajes)
        elif opcion == '5':
            mas_bajo_m(lista_personajes)
        elif opcion == '6':
            mas_bajo_f(lista_personajes)
        elif opcion == '7':
            promedio_m(lista_personajes)
        elif opcion == '8':
            promedio_f(lista_personajes)
        elif opcion == '9':
            contador_color_ojos(lista_personajes)
        elif opcion == '10':
            contador_color_pelo(lista_personajes)
        elif opcion == '11':
            contador_inteligencia(lista_personajes)
        elif opcion == '12':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Elija una opción del 1 al 8.")
            input("Presione Enter para continuar...")
