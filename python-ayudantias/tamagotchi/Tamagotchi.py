class Tamagotchi:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.salud = 50
        self.felicidad = 50
        self.energia = 50

    def jugar(self):
        #self.felicidad = self.felicidad + 10
        self.felicidad += 10
        # self.salud = self.salud - 5
        self.salud -= 5
        print(f"⚽ {self.nombre} jugo alegremente.")
        print(f"Felicidad:  {self.felicidad} (+10)")
        print(f"Salud:      {self.salud} (-5)")


    def comer(self):
        self.felicidad += 5
        self.salud += 10
        print(f"🍎 {self.nombre} se comio toda la comida.")
        print(f"Felicidad:  {self.felicidad} (+5)")
        print(f"Salud:      {self.salud} (+10)")


    def curar(self):
        self.salud += 20
        self.felicidad -= 5
        print(f"💉 {self.nombre} esta completamente curado.")
        print(f"Felicidad:  {self.felicidad} (-5)")
        print(f"Salud:      {self.salud} (+20)")

class TamagotchiCorredor(Tamagotchi):
    
    def correr_maxima_velocidad(self):
        self.energia -= 20
        self.felicidad += 5
        self.salud -=10
        print(f"🚄 {self.nombre} esta corriendo a máxima velocidad.")
        print(f"Felicidad:  {self.felicidad} (+5)")
        print(f"Salud:      {self.salud} (-10)")
        print(f"Energia:    {self.energia} (-20)")