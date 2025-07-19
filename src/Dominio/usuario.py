from abc import ABC, abstractmethod
from src.dominio.reserva import Reserva

class Usuario(ABC):
    def __init__(self, id_usuario, nombre):
        self._id = str(id_usuario).zfill(10)
        self._nombre = nombre

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def mostrar_informacion(self):
        pass

    @abstractmethod
    def realizar_reserva(self, sala, fecha, hora_inicio, hora_fin):
        pass


class Cliente(Usuario):
    def mostrar_informacion(self):
        print(f"Cliente: {self.nombre} (ID: {self.id})")

    def realizar_reserva(self, sala, fecha, hora_inicio, hora_fin):
        print(f"Reserva realizada por Cliente {self.nombre}.")
        return Reserva(1, self, sala, fecha, hora_inicio, hora_fin)


class Administrador(Usuario):
    def mostrar_informacion(self):
        print(f"Administrador: {self.nombre} (ID: {self.id})")

    def realizar_reserva(self, sala, fecha, hora_inicio, hora_fin):
        print(f"Reserva urgente por Administrador {self.nombre}.")
        return Reserva(2, self, sala, fecha, hora_inicio, hora_fin)
