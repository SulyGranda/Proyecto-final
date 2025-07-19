import sys
import pyodbc as bd

class Conexion:
    #_SERVIDOR = 'DESKTOP-OT44207\\ESTRELLASQL'   #nombre de PC/servidor
    #_SERVIDOR = '192.168.3.14'  # IP José Estrella red local
    _SERVIDOR = 'VICENTE\\OLAYAVILLASQL'
    _BBDD = 'reserva'
    _USUARIO = 'sa'      #usuario
    _PASSWORD = 'Fghj1234'     #contraseña
    _conexion = None
    _cursor = None


    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    f'SERVER={cls._SERVIDOR};'
                    f'DATABASE={cls._BBDD};'
                    f'UID={cls._USUARIO};'
                    f'PWD={cls._PASSWORD};'
                    'TrustServerCertificate=yes'
                )
                return cls._conexion
            except Exception as e:
                print(e)
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                return cls._cursor
            except Exception as e:
                print(e)
                sys.exit()
        else:
            return cls._cursor

if __name__ == '__main__':
    print(Conexion.obtenerConexion())
    print(Conexion.obtenerCursor())
