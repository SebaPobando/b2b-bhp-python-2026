#Declaración del tipo de colección
lista = []
tuplas = ()
diccionarios = {}

#LISTAS
lista_de_personas = ["Pedro", "Alvaro", "Matias", "Jose"]
#posicion               0       1           2       3
#print lista completa
print(lista_de_personas)
#print dato especifico
print(lista_de_personas[2])

#ejemplo de lista de compras
lista_de_compras = ["Manzanas","Naranjas","Platanos","Mandarinas"]
#posiciones inciales    0          1            2          3       4
print(lista_de_compras)

#Agregar nuevo valor (Pan)
lista_de_compras.append("Pan")
print(lista_de_compras)

#Ver tamaño de lista
tamano_lista = len(lista_de_compras)
print(f"El tamaño de la lista es de: {tamano_lista} elementos")

#Modificar un dato de la lista
#Cambiar mandarinas por duraznos
lista_de_compras[3] = "Duraznos"
print(lista_de_compras)

#Eliminar dato de una lista
#Eliminar Platanos y Manzanas
lista_de_compras.pop(0) #Manzanas
print(lista_de_compras)
lista_de_compras.pop(1) #Platanos, la posicion de platanos cambio al eliminar manzanas
print(lista_de_compras)
#Calcular el tamaño final de la lista
tamano_lista = len(lista_de_compras)
print(f"El tamaño de la lista es de: {tamano_lista} elementos")

#TUPLAS
personal = ("Jose", "Carlos", "Francisca")
print(personal)
print(personal[1])
#personal.append("Matias")
#personal[1] = "Matias"
#personal.pop()
