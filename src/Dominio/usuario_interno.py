from src.dominio.usuario import Usuario
from src.dominio.reserva import Reserva

class UsuarioInterno(Usuario):
    def __init__(self, id_usuario, nombre, departamento):
        super().__init__(id_usuario, nombre)
        self._departamento = departamento

    @property
    def departamento(self):
        return self._departamento

    def mostrar_informacion(self):
        print(f"Usuario Interno: {self.nombre} (ID: {self.id}) - Departamento: {self.departamento}")

    def realizar_reserva(self, sala, fecha, hora_inicio, hora_fin):
        print(f"{self.nombre} (Interno) ha reservado la sala {sala.nombre}.")
        return Reserva(3, self, sala, fecha, hora_inicio, hora_fin)
