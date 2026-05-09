from abc import ABC, abstractmethod

class Entidad(ABC):
    """Clase abstracta base que representa todas las entidades en el sistema."""

    def __init__(self, id_entidad, nombre):
        self._id_entidad = id_entidad # Identificador único de la entidad
        self._nombre = nombre
    
    @property
    def id_entidad(self):
        return self._id_entidad
    
    @property
    def nombre(self):
        return self._nombre
    
    @abstractmethod
    def mostrar_informacion(self):
        """Método abstracto que debe ser implementado por todas las entidades para mostrar su información."""
        pass