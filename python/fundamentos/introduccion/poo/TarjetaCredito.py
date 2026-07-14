class TarjetaCredito:
    def __init__(self, limite_credito, intereses):
        self.limite_credito = limite_credito
        self.intereses = intereses
        self.saldo_pagar = 0

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
            print("Compra realizada")
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: ${self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        if self.saldo_pagar > 0:
            self.saldo_pagar += self.saldo_pagar * self.intereses
        return self