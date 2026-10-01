class ServicioNotificaciones:
    def notificar(self, cliente, mensaje):
        print(f"[Notificacion para {cliente.email}] {mensaje}")