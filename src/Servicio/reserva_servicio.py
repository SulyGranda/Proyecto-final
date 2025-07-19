from src.datos.reserva_dao import ReservaDAO


class ReservaServicio:
    def crear_reserva(self, cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin):
        #Validación para que no haya chooque en la misma sala, fecha y horario
        if ReservaDAO.existe_reserva_en_horario(sala, fecha, hora_inicio, hora_fin):
            raise Exception("Ya existe una reserva para esa sala, fecha y horario.")

        #Intenta insertar la reserva y maneja unicidad de cédula
        return ReservaDAO.insertar_reserva(
            cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin
        )

    def buscar_reserva_por_cedula(self, cedula):
        return ReservaDAO.buscar_por_cedula(cedula)

    def actualizar_reserva(self, cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin):
        return ReservaDAO.actualizar_reserva(cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin)

    def eliminar_reserva(self, cedula):
        return ReservaDAO.eliminar_reserva(cedula)

    def listar_reservas(self):
        return ReservaDAO.listar_reservas()


