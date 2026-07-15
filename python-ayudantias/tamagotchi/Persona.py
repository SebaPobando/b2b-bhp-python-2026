class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi # Asociación con la clase Tamagotchi

    def jugar_con_tamagotchi(self):
        print(f"{self.nombre} esta jugando con {self.tamagotchi.nombre}")
        self.tamagotchi.jugar()
    
    def darle_comida(self):
        print(f"{self.nombre} esta alimentando a {self.tamagotchi.nombre}")
        self.tamagotchi.comer()

    def curarlo(self):
        print(f"{self.nombre} ha curado a {self.tamagotchi.nombre}")
        self.tamagotchi.curar()

    def correr(self):
        print(f"{self.nombre} le ordeno a {self.tamagotchi.nombre} que corra a máxima velocidad.")
        self.tamagotchi.correr_maxima_velocidad()