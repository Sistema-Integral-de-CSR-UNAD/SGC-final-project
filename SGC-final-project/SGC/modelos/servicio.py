from abc import ABC, abstractmethod

class Servicio(ABC):
    """Clase abstracta que represnta los servicios del Software FJ"""
    def __init__(self, id_servicio, nombre_servicio, precio_base):
        self._id_servicio = id_servicio
        self._nombre_servicio = nombre_servicio
        self._precio_base = precio_base
    
    @property
    def nombre_servicio(self):
        return self._nombre_servicio
    
    @property
    def calcular_costo(self, cantidad):
        """Método poliformico para calcular costos"""
        pass

    @abstractmethod
    def obtener_descripcion(self):
        pass

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias):
        return self._precio_base * dias
    
    def obtener_descripcion(self):
        return f"Alquiler de Equipo: {self.nombre_servicio}"

class ReservaAsesoria(Servicio):
    def calcular_costo(self, horas):
        #Con recargo administrativo fijo
        return (self._precio_base * horas) + 20000
    
    def obtener_descripcion(self):
        return f"Asesoría Técnica: {self.nombre_servicio}"
    