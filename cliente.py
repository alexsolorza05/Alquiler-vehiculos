class Cliente:
    def __init__(self, nombre, apellido, dni, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.email = email
        self.reservas = []

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        try:
            entero = int(valor)
        except (TypeError, ValueError):
            entero = 0
        if entero != valor or entero <= 0:
            raise ValueError("El DNI debe ser un numero")
        self._dni = entero

    def reservas_en_estado(self, estado):
        return [r for r in self.reservas if r.estado is estado]

 

