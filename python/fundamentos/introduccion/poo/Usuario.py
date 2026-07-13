from TarjetaCredito import TarjetaCredito

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjeta = TarjetaCredito(5000, 0.02)

    def hacer_compra(self, monto):
        self.tarjeta.compra(monto)
        return self

    def pagar_tarjeta(self, monto):
        self.tarjeta.pago(monto)
        return self

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}")
        print(f"Saldo a pagar: ${self.tarjeta.saldo_pagar}")
        return self
    
seba = Usuario("Sebastián", "seba@gmail.com")

seba.hacer_compra(1000, 0).hacer_compra(2500, 1).hacer_compra(300, 2).mostrar_saldo_usuario()

seba.pagar_tarjeta(500, 1).mostrar_saldo_usuario()