class Reserva:
    def __init__(self, id_reserva, usuario, sala, fecha, hora_inicio, hora_fin):
        self._id = id_reserva
        self._usuario = usuario
        self._sala = sala
        self._fecha = fecha
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin

    @property
    def id(self):
        return self._id

    @property
    def usuario(self):
        return self._usuario

    @property
    def sala(self):
        return self._sala

    @property
    def fecha(self):
        return self._fecha

    @property
    def hora_inicio(self):
        return self._hora_inicio

    @property
    def hora_fin(self):
        return self._hora_fin

    def mostrar_detalles(self):
        print(f"\nReserva ID: {self.id}")
        self.usuario.mostrar_informacion()
        print(f"Sala: {self.sala.nombre} (Capacidad: {self.sala.capacidad})")
        print(f"Fecha: {self.fecha}, Hora: {self.hora_inicio} - {self.hora_fin}")
