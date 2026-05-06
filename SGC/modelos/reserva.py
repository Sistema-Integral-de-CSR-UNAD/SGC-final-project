from excepciones.personalizadas import ReservaInvalidaError

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise ReservaInvalidaError("La duración de la reserva debe ser mayor a cero.")
        
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "PENDIENTE"
    
    def procesar(self):
        """Usa poliformismo para calcular el costo total."""
        total = self.servicio.calcular_costo(self.duracion)
        self.estado = "CONFIRMADA"
        return f"Reserva {self.estado} para {self.cliente.nombre}. Total: ${total:,.2f}"
    