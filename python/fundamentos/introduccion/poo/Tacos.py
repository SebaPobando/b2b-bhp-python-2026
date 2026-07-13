class Taco:
    def __init__(self, guiso):
        self.guiso = guiso
        self.tortilla = "maiz"

    def prepararlo(self):
        print(f"Haciendo un taco de {self.guiso}")
        print("¡Calentando el taquito!")

    def servir(self):
        print("Tomamos un plato plano y colocamos el platillo")
        

class Enchilada(Taco):
    def __init__(self, guiso):
        super().__init__(guiso)
        self.salsa = "verde"
  
    def hacer_enchilada(self):
        super().prepararlo()
        print("Agregamos la salsa a nuestro taco y ahora es enchilada")
        
    def servir(self):
        print("Tomamos un plato grande y colocamos el platillo y adornamos con cilantro")
        
class Comensal:
   def __init__(self, nombre):
       self.nombre = nombre
       self.taco = Taco("carne")

   def comer_taco(self):
       self.taco.prepararlo()
       self.taco.servir()
       print("Me como mi delicioso taco")