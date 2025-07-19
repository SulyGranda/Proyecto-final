class Sala:
    def __init__(self, id_sala, nombre, capacidad):
        self._id = id_sala
        self._nombre = nombre
        self._capacidad = capacidad

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def capacidad(self):
        return self._capacidad
