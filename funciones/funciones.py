from superheroes.personajes import *

# ---> Primera parte
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
        "\n   *** Primera parte: ***   \n"
        "1. Nombres de los superheroes\n"
        "2. Altura de los superheroes\n"
        "3. Superheroe mas alto\n"
        "4. Superheroe mas bajo\n"
        "5. Promedio de altura de los superheroes\n"
        "6. Superheroe mas pesado\n"
        "7. Superheroe menos pesado\n"
    )
    print(menu)
    
# ---> Segunda parte

def genero_m (lista_personajes):
    for personaje in lista_personajes:
        if personaje['genero'] == "M":
            print(f"Nombre: {personaje['nombre']}")
            

def genero_f (lista_personajes):
    for personaje in lista_personajes:
        if personaje['genero'] == "F":
            print(f"Nombre: {personaje['nombre']}")
            
def mas_alto_m (lista_personajes):
    altura_max_m = None
    nombre_mas_alto_m = ""
        
    for personaje in lista_personajes:
        if personaje['genero'] == "M":
            altura_actual = float(personaje['altura'])
            if altura_max_m is None or altura_actual > altura_max_m:
                altura_max_m = altura_actual
                nombre_mas_alto_m = personaje['nombre']
    
    if nombre_mas_alto_m:
        print(f"El personaje masculino más alto es: {nombre_mas_alto_m}, con una altura de: {altura_max_m} cm.")

def mas_alto_f (lista_personajes):
    altura_max_f = None
    nombre_mas_alto_f = ""
        
    for personaje in lista_personajes:
        if personaje['genero'] == "F":
            altura_actual = float(personaje['altura'])
            if altura_max_f is None or altura_actual > altura_max_f:
                altura_max_f = altura_actual
                nombre_mas_alto_f = personaje['nombre']
    
    if nombre_mas_alto_f:
        print(f"El personaje femenimo más alto es: {nombre_mas_alto_f}, con una altura de: {altura_max_f} cm.")
        
def mas_bajo_m (lista_personajes):
    altura_min_m = None
    nombre_mas_bajo_m = ""
        
    for personaje in lista_personajes:
        if personaje['genero'] == "M":
            altura_actual = float(personaje['altura'])
            if altura_min_m is None or altura_actual < altura_min_m:
                altura_min_m = altura_actual
                nombre_mas_bajo_m = personaje['nombre']
    
    if nombre_mas_bajo_m:
        print(f"El personaje masculino más bajo es: {nombre_mas_bajo_m}, con una altura de: {altura_min_m} cm.")

def mas_bajo_f (lista_personajes):
    altura_min_f = None
    nombre_mas_bajo_f = ""
        
    for personaje in lista_personajes:
        if personaje['genero'] == "F":
            altura_actual = float(personaje['altura'])
            if altura_min_f is None or altura_actual < altura_min_f:
                altura_min_f = altura_actual
                nombre_mas_bajo_f = personaje['nombre']
    
    if nombre_mas_bajo_f:
        print(f"El personaje femenino más bajo es: {nombre_mas_bajo_f}, con una altura de: {altura_min_f} cm.")

def promedio_m (lista_personajes):
    acumulador_altura_m = 0
    
    for personaje in lista_personajes:
        if personaje['genero'] == "M":
            acumulador_altura_m = acumulador_altura_m + float(personaje['altura'])
    promedio = acumulador_altura_m // len(lista_personajes)
    
    print(f"El promedio de altura masculino es: {promedio}cm")        

def promedio_f (lista_personajes):
    acumulador_altura_f = 0
    
    for personaje in lista_personajes:
        if personaje['genero'] == "F":
            acumulador_altura_f = acumulador_altura_f + float(personaje['altura'])
    promedio = acumulador_altura_f // len(lista_personajes)
    
    print(f"El promedio de altura femenino es: {promedio}cm")        

def contador_color_ojos(lista_personajes):
    contador_color_ojos = {}

    for personaje in lista_personajes:
        color_ojos = personaje['color_ojos']
        contador_color_ojos[color_ojos] = contador_color_ojos.get(color_ojos, 0) + 1

    print("Número de superhéroes por color de ojos:")
    for color in contador_color_ojos:
        count = contador_color_ojos[color]
        print(f"{color}: {count}")

def contador_color_pelo(lista_personajes):
    contador_color_pelo = {}

    for personaje in lista_personajes:
        color_pelo = personaje['color_pelo']
        if color_pelo: 
            contador_color_pelo[color_pelo] = contador_color_pelo.get(color_pelo, 0) + 1

    print("\nNúmero de superhéroes por color de pelo:")
    for color in contador_color_pelo:
        count = contador_color_pelo[color]
        print(f"{color}: {count}")

def contador_inteligencia(lista_personajes):
    contador_inteligencia = {}

    for personaje in lista_personajes:
        inteligencia = personaje.get('inteligencia', 'No Tiene')
        if inteligencia: 
            contador_inteligencia[inteligencia] = contador_inteligencia.get(inteligencia, 0) + 1

    print("\nNúmero de superhéroes por tipo de inteligencia:")
    for inteligencia, count in contador_inteligencia.items():
        print(f"{inteligencia}: {count}")
        
def mostrar_segundo_menu():
    menu = (
        "\n   *** Segunda parte: ***   \n"
        "1. Nombres de los superheroes masculinos\n"
        "2. Nombres de los superheroes femeninos\n"
        "3. Mas alto del genero masculino\n"
        "4. Mas alto del genero femenino\n"
        "5. Mas bajo del genero masculino\n"
        "6. Mas bajo del genero femenino\n"
        "7. Altura promedio genero masculino\n"
        "8. Altura promedio genero femenino\n"
        "9. Cantidad de colores de ojos\n"
        "10. Cantidad de colores de pelo\n"
        "11. Tipos y cantidad de inteligencia\n"
    )
    print(menu)