from src.dominio.usuario import Usuario
from src.dominio.reserva import Reserva

class UsuarioExterno(Usuario):
    def __init__(self, id_usuario, nombre, institucion):
        super().__init__(id_usuario, nombre)
        self._institucion = institucion

    @property
    def institucion(self):
        return self._institucion

    def mostrar_informacion(self):
        print(f"Usuario Externo: {self.nombre} (ID: {self.id}) - Institución: {self.institucion}")

    def realizar_reserva(self, sala, fecha, hora_inicio, hora_fin):
        print(f"{self.nombre} (Externo) requiere validación para reservar.")
        return Reserva(4, self, sala, fecha, hora_inicio, hora_fin)
