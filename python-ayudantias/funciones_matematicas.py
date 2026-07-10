#Codigo secuencial
# numero1 = int(input("Ingrese un numero: "))
# numero2 = int(input("Ingrese otro numero: "))

# resultado = numero1 + numero2
# print(f"El resultado es: {resultado}")

#codigo como función
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

suma_final = sumar(numero1, numero2)
print(f"El resultado de la suma es: {suma_final}")

def saludar(nombre):
    print(f"Buenas noches, {nombre}")

saludar("Matías")
saludar("Luis")
saludar("Maria")
saludar("")