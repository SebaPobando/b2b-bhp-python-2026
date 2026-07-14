class TarjetaCredito:
   
   def __init__(self, numero_tarjeta, limite_credito, intereses, saldo_pagar=0):
      self.numero_tarjeta = numero_tarjeta
      self.limite_credito = limite_credito
      self.intereses = intereses
      self.saldo_pagar = saldo_pagar

   # Métodos
   def compra(self, monto):
      if self.saldo_pagar + monto <= self.limite_credito:
         self.saldo_pagar += monto
         print(f"Compra realizada exitosamente por: ${monto}")
      else:
         print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
      
      return self
      

   def pago(self, monto):
      #self.saldo_pagar = self.saldo_pagar - monto
      self.saldo_pagar -= monto

      return self
   
   def mostrar_info_tarjeta(self):
      print("######### DATOS DE TARJETA #########")
      print(f"N° Tarjeta: {self.numero_tarjeta}")
      print(f"Saldo a pagar: ${self.saldo_pagar}")
      print(f"Interes: {self.intereses * 100}%")
      print("####################################")
  
   def cobrar_interes(self):
      self.saldo_pagar *= (1 + self.intereses)
      return self
   

cmr = TarjetaCredito(numero_tarjeta=2910292838291, limite_credito=1000000, intereses=0.028, saldo_pagar=500000)
santader = TarjetaCredito(numero_tarjeta=23813891, limite_credito=300000, intereses=0.05)

cmr.mostrar_info_tarjeta()
cmr.compra(350000)
cmr.mostrar_info_tarjeta()
print(f"Intento de compra por $400.000")
print("..........")
cmr.compra(400000)
cmr.pago(400000)
print("Se pagaron exitosamente $400.000")
cmr.mostrar_info_tarjeta()
print("Se realizo un cobro de interes")
cmr.cobrar_interes()
cmr.mostrar_info_tarjeta()

