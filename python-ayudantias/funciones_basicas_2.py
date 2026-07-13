def multiplica_por_2(numero):
    lista = []
    for i in range(0,numero+1):
        lista.append(i*2)
    
    return lista

resultado = multiplica_por_2(3)
print(resultado)