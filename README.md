🏢 Sistema de Reservas de Salas

## 🧠 Propósito del Proyecto

Diseñar una solución que permita:
- Registrar reservas de salas por parte de diferentes tipos de usuarias/os.
- Aplicar reglas de validación horaria según el tipo de perfil.
- Conectarse a una base de datos en SQL Server para conservar la información.
- Presentar una interfaz visual intuitiva creada con PyQt5.
- Demostrar el uso de clases, herencia y encapsulamiento dentro del dominio del sistema.

## 📁 Estructura del Proyecto

src/
├── datos/
 ├── conexion.py # Conexión con SQL Server (ODBC)
 │
 └── reserva_dao.py # Consultas SQL: insertar, buscar, eliminar, actualizar
 │
 ├── dominio/
 │
 ├── sala.py # Clase Sala
 │
 ├── usuario.py # Clase base Usuario
 │
 ├── usuario_interno.py # Usuario con permisos extendidos
 │
 ├── usuario_externo.py # Usuario con restricciones de horario
 │
 └── reserva.py # Clase Reserva
  │
  ├── servicio/
  │
  └── reserva_servicio.py # Reglas de negocio y validación horaria
  │
  ├── UI/
  │
  ├── vtnPrincipal.ui # Interfaz creada en Qt Designer
  │
  └── vtnPrincipal.py # Código asociado a la UI
  │
└── main.py # Punto de entrada al sistema

## ⚙️ Tecnologías Utilizadas

- **Lenguaje: Python
- **Base de datos: SQL Server + ODBC
- **Interfaz gráfica: PyQt5
- **Librerías clave: `datetime`, `pyodbc`

## 🕐 Reglas de Horario por Usuario

| Tipo de usuario     | Horario permitido      |
|---------------------|------------------------|
| Usuario Interno     | Sin restricciones      |
| Usuario Externo     | De 08:00 a 17:00 solo  |

Estas reglas están codificadas en las clases específicas de cada usuario. Si se intenta reservar fuera de este rango, el sistema lanza una advertencia.

---

## 🧪 Ejemplo de Uso en Código

```python
from dominio.sala import Sala
from dominio.usuario_externo import UsuarioExterno

sala1 = Sala(101, "Sala Ejecutiva", 12)
persona = UsuarioExterno(172839456, "Ana López", "Marketing")
reserva = persona.realizar_reserva(sala1, "2025-07-20", "09:00", "10:00")

if reserva:
    reserva.mostrar_detalles()
else:
    print("La reserva no fue permitida por restricciones horarias.")
  -------------------------------------------------
🔗 Parámetros de Conexión
Archivo conexion.py usa los siguientes valores:

plaintext
DRIVER={ODBC Driver 17 for SQL Server};
SERVER=192.168.3.14;
DATABASE=reserva;
UID=sa;
PWD=sa;
TrustServerCertificate=yes

-------------------------------------------------
👭 Equipo de Desarrollo:

🌼 Estrella Quiroz Jose

🌼 Granda Cabrera Suly

🌼 Jama Lema Gina

🌼 Loor Toscano Lucia

🌼 Olaya Villafuerte Ammy

Agradecimientos especiales al Ing. Guillermo Valarezo, docente guía.
