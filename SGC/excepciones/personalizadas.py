class SoftwareFJError(Exception):
    """Clase base para todas las excepciones personalizadas del software FJ."""
    def __init__(self, mensaje, codigo_error=None):
        super().__init__(mensaje)
        self.codigo_error = codigo_error

class ReservaInvalidaError(SoftwareFJError):
    """Aparece cuando los datos de una reserva (fechas, duración), son invalidos."""
    pass

class ServicioNoDisponileError(SoftwareFJError):
    """Aparece cuando se intenta reservar un servicio que no está disponible o no existe."""
    pass