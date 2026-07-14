# diccionario_vacio = {}

# persona = {
#     'nombre': 'Carmen', 
#     'edad': 31, 
#     'altura': 1.71, 
#     'usa_lentes': False
#     }

# persona['nombre'] = 'Valeria'  # Actualiza si el valor de la llave existente

# persona['hobbies'] = ['jugar videojuegos', 'programación'] 

# # Agrega esa clave-valor si no existía previamente

# print(persona)

# # Imprime: {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']}

# altura = persona.pop('altura')  # Elimina la clave indicada y devuelve el valor

# print(altura)    # Imprime: 1.71
# print(persona)

# # salida: {'nombre': 'Carmen', 'edad': 31, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']} 


# # numero1 = "170.5"

# # print(float(numero1) + 10.2)

estudiante = {
    "nombre": "Gonzalo", 
    "curso": "Python"
    } #Notación Literal

paises = {} #Diccionario vacío

paises["MEX"] = "México" #Agregando valores

paises["COL"] = "Colombia"

paises["CHL"] = "Chile"

print(paises)

if "CRI" in paises: #Preguntamos si existe la clave en el diccionario

    print("¿Deseas reemplazar el valor?")

else: #No existe esa clave

    paises["CRI"] = "Costa Rica"