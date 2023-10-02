from superheroes.personajes import *

def mostrar_superheroes(lista_personajes):
    for personaje in lista_personajes:
        print(f"Nombre: {personaje['nombre']}")    

def altura_superheroes(lista_personajes):
    for personaje in lista_personajes:
        print(f"Nombre: {personaje['nombre']} y su altura: {personaje['altura']}")     

def mas_alto(lista_personajes):
    altura_max = None
    nombre_mas_alto = ""
    
    for personaje in lista_personajes:
        altura_actual = float(personaje['altura'])
        if altura_max is None or altura_actual > altura_max:
            altura_max = altura_actual
            nombre_mas_alto = personaje['nombre']
    
    print(f"El personaje mas alto es: {nombre_mas_alto}, con una altura de: {altura_max} cm.")

def mas_bajo(lista_personajes):
    altura_min = None
    nombre_mas_bajo = ""
    
    for personaje in lista_personajes:
        altura_actual = float(personaje['altura'])
        if altura_min is None or altura_actual < altura_min:
            altura_min = altura_actual
            nombre_mas_bajo = personaje['nombre']
    
    print(f"El personaje mas bajo es: {nombre_mas_bajo}, con una altura de: {altura_min} cm.")

def promedio_altura(lista_personajes):
    acumulador_altura = 0
    
    for personaje in lista_personajes:
        acumulador_altura = acumulador_altura + float(personaje['altura'])
    promedio = acumulador_altura // len(lista_personajes)
    
    print(f"El promedio de altura es: {promedio}cm")        

def mas_pesado (lista_personajes):
    peso_max = None
    nombre_mas_peso = ""
    
    for personaje in lista_personajes:
        peso_actual = float(personaje['peso'])
        if peso_max is None or peso_actual > peso_max:
            peso_max = peso_actual
            nombre_mas_peso = personaje['nombre']
    
    print(f"El personaje mas pesado es: {nombre_mas_peso}, con un peso de: {peso_max} kilos.")
    
def menos_pesado (lista_personajes):
    peso_min = None
    nombre_menos_peso = ""
    
    for personaje in lista_personajes:
        peso_actual = float(personaje['peso'])
        if peso_min is None or peso_actual < peso_min:
            peso_min = peso_actual
            nombre_menos_peso = personaje['nombre']
    
    print(f"El personaje menos pesado es: {nombre_menos_peso}, con un peso de: {peso_min} kilos.")
    

def mostrar_menu ():
    menu = (
        "\n   *** Menu de opciones: ***   \n"
        "1. Nombres de los superheroes\n"
        "2. Altura de los superheroes\n"
        "3. Superheroe mas alto\n"
        "4. Superheroe mas bajo\n"
        "5. Promedio de altura de los superheroes\n"
        "6. Superheroe mas pesado\n"
        "7. Superheroe menos pesado\n"
    )
    print(menu)