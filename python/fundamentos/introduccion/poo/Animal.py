class Animal:
   def __init__(self, nombre, edad, color):
       self.nombre = nombre
       self.edad = edad
       self.color = color
       
   def hacer_truco(self):
       print(f"{self.nombre} realiza un truco")

class Gato(Animal):
   def __init__(self, nombre, edad, color, tipo_pelaje):
       super().__init__(nombre, edad, color)
       self.tipo_pelaje = tipo_pelaje

   def razcar_sofa(self):
       print(f'{self.nombre} está razcando el sofá de su casa')
       
   def hacer_truco(self):
       print(f"{self.nombre} te ignora un momento")
       print(f"{self.nombre} realiza un truco")
       
class Perro(Animal):
   pass