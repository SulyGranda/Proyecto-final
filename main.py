import sys
from PySide6.QtWidgets import QApplication
from src.UI.vtnPrincipal import VentanaPrincipal

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())

#Los departamentos que validan al usuario interno y pueden reservar cualquier horario son:
#gerencia
#marketing
#ventas
#recursos humanos
#administracion
#produccion