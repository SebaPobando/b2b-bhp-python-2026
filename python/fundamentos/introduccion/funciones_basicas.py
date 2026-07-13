# Multiplica por 2: crea una función que reciba un número y devuelva una lista que contenga los números enteros multiplicados por dos, desde el 0 hasta el número proporcionado como entrada.
# Ejemplo: multiplica_por_2(5) debe regresar [0, 2, 4, 6, 7, 10]

def multiplica_por_2(numero):
    resultado = []

    for i in range(numero + 1):
        resultado.append(i * 2)

    return resultado

print(multiplica_por_2(5))
