# for i in range(2, 10, 3):
#     print(i)

# for letra in 'Python':
#     print(letra)

# #Imprime: 'P', 'y', 't', 'h', 'o', 'n'

# lista = ['brócoli', 'pepino', 'pimiento']

# for i in range( len(lista) ):
#     print(i, lista[i])
# #Imprime: 0 brócoli, 1 pepino, 2 pimiento

# for verdura in lista:
#     print(verdura)
# #Imprime: brócoli, pepino, pimiento

# estudiante = {
#     "nombre": "Gonzalo", 
#     "curso": "Python"
#     }

# for clave in estudiante:
#     print(clave)
# #Imprime: nombre, curso


# for valor in estudiante:
#     print(estudiante[valor])
#Imprime: Gonzalo, Python

# num = 0

# while num < 4:
#     print("bucle while -", num)
#     num += 1
# else:
#     print("Acabamos de salir del bucle")


#Imprime: bucle while - 0, bucle while - 1, bucle while - 2, bucle while - 3

for letra in "detente":
    if letra == "n":
        break
    print(letra)
#Imprime: d, e, t, e

for letra in "detente":
    if letra == "n":
        continue
    print(letra)
#Imprime: d, e, t, e, t, e