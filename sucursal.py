from enums import EstadoVehiculo

class Sucursal:
    def __init__(self, codigo, ciudad, direccion):
        self.codigo = codigo
        self.ciudad = ciudad
        self.direccion = direccion
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        for v in self.vehiculos:
            if v.patente == vehiculo.patente:
                raise ValueError(f"La patente {vehiculo.patente} ya existe en la sucursal {self.codigo}")
        self.vehiculos.append(vehiculo)

    def trasladar_vehiculo(self, vehiculo, destino):
        if vehiculo not in self.vehiculos:
            raise ValueError(
                f"{vehiculo.patente} no existe en la sucursal {self.codigo}")
        destino.agregar_vehiculo(vehiculo)
        self.vehiculos.remove(vehiculo)

    def vehiculos_disponibles(self):
        return [v for v in self.vehiculos if v.estado is EstadoVehiculo.DISPONIBLE]