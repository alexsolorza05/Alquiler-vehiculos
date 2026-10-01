class Vehiculo:
    def __init__(self, patente, marca, modelo, tarifa_base, estado):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.tarifa_base = tarifa_base
        self.estado = estado

@property
def tarifa_base(self):
    return self.__tarifa_base

@tarifa_base.setter
def tarifa_base(self, tarifa_nueva):
    if tarifa_nueva <= 0:
        print("La tarifa no puede cero ni negativa")
    else:
        self.__tarifa_hora = tarifa_nueva
#El auto utiliza la tarifa base por día; 
#la camioneta aplica un recargo del 20 % sobre ese valor y la moto un descuento del 15 %.
class Auto (Vehiculo):
    def __init__(self, patente, marca, modelo, tarifa_base, estado):
        super().__init__(patente, marca, modelo, tarifa_base, estado)

    def calculo_costo(self, dias):
        costo_base = self.tarifa_base * dias
        return costo_base

class Camioneta (Vehiculo):
    def __init__(self, patente, marca, modelo, tarifa_base, estado):
        super().__init__(patente, marca, modelo, tarifa_base, estado)

    def calculo_costo(self, dias):
            costo_base = self.tarifa_base * dias * 1.20
            return costo_base
            

class Moto (Vehiculo):
        def __init__(self, patente, marca, modelo, tarifa_base, estado):
            super().__init__(patente, marca, modelo, tarifa_base, estado)

        def calculo_costo(self, dias):
                costo_base = self.tarifa_base * dias * 0.85
                return costo_base