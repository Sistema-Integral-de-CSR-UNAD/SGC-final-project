from .entidad import Entidad

class Cliente(Entidad):
    """Clase que representa a un cliente en el sistema, hereda de Entidad, con encapsulamiento estricto."""

    def __init__(self, id_cliente, nombre, correo_electronico):
        super().__init__(id_cliente, nombre)
        self._correo_electronico = correo_electronico #Atributo privado 
    
    @property
    def correo_electronico(self):
        return self._correo_electronico
    
    @correo_electronico.setter
    def correo_electronico(self, valor):
        #Se agrega una validación simple para el correo electrónico
        if "@" not in valor:
            raise ValueError("Correo electrónico no válido")
        self._correo_electronico = valor

    def mostrar_informacion(self):
        """Implementación del método abstracto para mostrar la información del cliente."""
        return f"Cliente: {self.nombre} (ID: {self.id_entidad}) - Correo: {self.correo_electronico}"
    