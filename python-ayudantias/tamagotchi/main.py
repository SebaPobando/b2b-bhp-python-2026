from Persona import Persona
from Tamagotchi import Tamagotchi, TamagotchiCorredor

mi_mascota = Tamagotchi(nombre="Tama", color="Verde")
tamagotchi_corredor = TamagotchiCorredor("carrerin", "Morado")



dueno = Persona("Matías", "Aguilar", tamagotchi_corredor)
dueno.jugar_con_tamagotchi()
print("#####################################")
dueno.darle_comida()
print("#####################################")
dueno.curarlo()
print("#####################################")
dueno.correr()

dueno2 = Persona("Perico", "Los palotes", mi_mascota)
dueno2.jugar_con_tamagotchi()
print("#####################################")
dueno2.darle_comida()
print("#####################################")
dueno2.curarlo()
print("#####################################")