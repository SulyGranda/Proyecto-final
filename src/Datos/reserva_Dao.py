from src.datos.conexion import Conexion

class ReservaDAO:
    @classmethod
    def existe_reserva_en_horario(cls, sala, fecha, hora_inicio, hora_fin):
        with Conexion.obtenerCursor() as cursor:
            consulta = """
            SELECT COUNT(*) FROM reservas
            WHERE sala = ? AND fecha = ?
            AND (
                (hora_inicio < ? AND hora_fin > ?) OR
                (hora_inicio < ? AND hora_fin > ?) OR
                (hora_inicio >= ? AND hora_fin <= ?)
            )
            """
            datos = (
                sala, fecha,
                hora_fin, hora_inicio,
                hora_inicio, hora_fin,
                hora_inicio, hora_fin
            )
            cursor.execute(consulta, datos)
            resultado = cursor.fetchone()
            cantidad = resultado[0] if resultado else 0
            return cantidad > 0

    @classmethod
    def insertar_reserva(cls, cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin):
        try:
            with Conexion.obtenerCursor() as cursor:
                consulta = """
                INSERT INTO reservas (cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """
                datos = (cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin)
                cursor.execute(consulta, datos)
                cursor.connection.commit()
            return True
        except Exception as e:
            #Si el error es por duplicado de cédula
            if 'UNIQUE' in str(e).upper():
                raise Exception("Ya existe una reserva registrada con esa cédula.")
            else:
                raise Exception(f"Error al guardar reserva: {e}")

    @classmethod
    def buscar_por_cedula(cls, cedula):
        with Conexion.obtenerCursor() as cursor:
            consulta = """
            SELECT id, cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin
            FROM reservas
            WHERE cedula = ?
            """
            cursor.execute(consulta, (cedula,))
            return cursor.fetchone()

    @classmethod
    def actualizar_reserva(cls, cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin):
        with Conexion.obtenerCursor() as cursor:
            consulta = """
            UPDATE reservas
            SET nombre = ?, departamento = ?, email = ?, sala = ?, fecha = ?, hora_inicio = ?, hora_fin = ?
            WHERE cedula = ?
            """
            datos = (nombre, departamento, email, sala, fecha, hora_inicio, hora_fin, cedula)
            cursor.execute(consulta, datos)
            cursor.connection.commit()
            return cursor.rowcount > 0

    @classmethod
    def eliminar_reserva(cls, cedula):
        with Conexion.obtenerCursor() as cursor:
            consulta = """
            DELETE FROM reservas WHERE cedula = ?
            """
            cursor.execute(consulta, (cedula,))
            cursor.connection.commit()
            return cursor.rowcount > 0

    @classmethod
    def listar_reservas(cls):
        with Conexion.obtenerCursor() as cursor:
            consulta = """
            SELECT id, cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin
            FROM reservas
            """
            cursor.execute(consulta)
            return cursor.fetchall()
