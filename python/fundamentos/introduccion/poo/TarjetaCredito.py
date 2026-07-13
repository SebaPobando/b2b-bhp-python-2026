class TarjetaCredito:
    banco = "Banco Internacional de Programadores"
    todas_las_tarjetas = []

    def __init__(self, limite_credito, saldo_pagar):
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar
        TarjetaCredito.todas_las_tarjetas.append(self)

    @classmethod
    def cambiar_banco(cls, nombre):
        cls.banco = nombre
        
    def todos_saldos(cls):
        total_saldos = 0
        for tarjeta in cls.todas_las_tarjetas: 
            total_saldos += tarjeta.saldo_pagar
        return total_saldos