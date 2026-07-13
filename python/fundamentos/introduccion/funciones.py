# def multiplicacion(num1, num2):
#     resultado = num1 * num2
#     return resultado

# resultado_multiplicacion = multiplicacion(5, 5)
# print(resultado_multiplicacion)


# print(multiplicacion(5, 6))

# def buenos_dias(nombre):
#     print("Buenos días "+nombre)
    
# buenos_dias("alegría")
# buenos_dias("al amor")
# buenos_dias("a la vida")
# buenos_dias("señor Sol")

# def buenos_dias(nombre):
#     return "Buenos días "+nombre

# #El valor de retorno de la función es "Buenos días Python", por lo que el valor de mi variable frase será ese
# frase = buenos_dias("Python")
# print(frase) #Imprime: Buenos días Python

def buenos_dias(nombre="alegría", cantidad=1):
   print(("Buenos días "+nombre) * cantidad)

buenos_dias()           #Imprime: "Buenos días alegría" una sola vez

buenos_dias("al amor")  #Imprime: "Buenos días al amor" una sola vez

buenos_dias(nombre="a la vida")  #Imprime: "Buenos días a la vida" una sola vez

buenos_dias(cantidad=3)  #Imprime: "Buenos días alegría" 3 veces

buenos_dias(nombre="señor Sol", cantidad=2)  #Imprime: "Buenos días señor Sol" 2 veces

#El orden de los argumentos no importa siempre y cuando especifiquemos el parámetro

buenos_dias(cantidad=3, nombre="para vos")  #Imprime: "Buenos días para vos" 3 veces