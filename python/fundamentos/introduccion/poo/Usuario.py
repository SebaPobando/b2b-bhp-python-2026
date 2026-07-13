class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  
        self.saldo_pagar += monto   

    def pagar_tarjeta(self, monto):
        self.saldo_pagar -= monto

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.saldo_pagar}")

    def transferir_deuda(self, otro_usuario, monto):
        self.saldo_pagar -= monto
        otro_usuario.saldo_pagar += monto

# Creación de las 3 instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@skillnest.com")
daniel = Usuario("Daniel", "LaRusso", "daniel@skillnest.com")
donatello = Usuario("Donatello", "Donatellin", "donatello@skillnest.com")

# Miyagi realiza 2 compras y luego paga su tarjeta
miyagi.hacer_compra(10000)
miyagi.hacer_compra(5000)
miyagi.pagar_tarjeta(8000)
miyagi.mostrar_saldo_usuario()

# Daniel realiza 1 compra y luego paga 2 veces su tarjeta
daniel.hacer_compra(20000)
daniel.pagar_tarjeta(5000)
daniel.pagar_tarjeta(5000)
daniel.mostrar_saldo_usuario()

# Donatello realiza 3 compras y luego paga su tarjeta 4 veces
donatello.hacer_compra(2000)
donatello.hacer_compra(1500)
donatello.hacer_compra(6000)
donatello.pagar_tarjeta(1000)
donatello.pagar_tarjeta(1000)
donatello.pagar_tarjeta(1000)
donatello.pagar_tarjeta(1000)
donatello.mostrar_saldo_usuario()