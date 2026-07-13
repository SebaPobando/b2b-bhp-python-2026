def cantidad_de_vocales():
   return 5

print(cantidad_de_vocales()) # output: 5

def cantidad_de_glaciares_argentina():
   return 16968

print(cantidad_de_glaciares_argentina()) # output: 16968

def anio_independencia_chile():
   return 1810
   return 1851

print(anio_independencia_chile()) # output: 1810

def cantidad_de_departamentos_colombia():
    return(32)
    print(33)

print(cantidad_de_departamentos_colombia()) # output: 32


def altura_machu_picchu():
    print(2438)

x = altura_machu_picchu() # output: 2438
print(x) # output: None


def suma(a, b):
   print(a+b)

print(suma(10, 5) + suma(4, 3)) # output seria error porque no se puede sumar los None
#probar cambiando suma de print a return para ver la diferencia


def concatenar(a, b):

   return str(b) + str(a)

print(concatenar(7, 15)) #output: 157
print(concatenar(" Mundo", "Hola"))