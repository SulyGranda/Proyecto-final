# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTimeEdit, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(728, 609)
        vtnPrincipal.setIconSize(QSize(26, 24))
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbNombre = QLabel(self.centralwidget)
        self.lbNombre.setObjectName(u"lbNombre")
        self.lbNombre.setGeometry(QRect(10, 150, 171, 31))
        font = QFont()
        font.setFamilies([u"Sitka Small Semibold"])
        font.setPointSize(12)
        font.setBold(True)
        self.lbNombre.setFont(font)
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(190, 150, 211, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.txtNombre.setFont(font1)
        self.txtNombre.setMaxLength(50)
        self.lbCedula = QLabel(self.centralwidget)
        self.lbCedula.setObjectName(u"lbCedula")
        self.lbCedula.setGeometry(QRect(50, 210, 100, 20))
        font2 = QFont()
        font2.setFamilies([u"Sitka Text Semibold"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.lbCedula.setFont(font2)
        self.txtCedula = QLineEdit(self.centralwidget)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setGeometry(QRect(190, 210, 211, 31))
        font3 = QFont()
        font3.setFamilies([u"Arial Black"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.txtCedula.setFont(font3)
        self.txtCedula.setMaxLength(10)
        self.lbDepartamento = QLabel(self.centralwidget)
        self.lbDepartamento.setObjectName(u"lbDepartamento")
        self.lbDepartamento.setGeometry(QRect(0, 280, 141, 20))
        self.lbDepartamento.setFont(font)
        self.txtDepartamento = QLineEdit(self.centralwidget)
        self.txtDepartamento.setObjectName(u"txtDepartamento")
        self.txtDepartamento.setGeometry(QRect(130, 280, 201, 31))
        self.txtDepartamento.setFont(font3)
        self.lbEmail = QLabel(self.centralwidget)
        self.lbEmail.setObjectName(u"lbEmail")
        self.lbEmail.setGeometry(QRect(370, 280, 71, 20))
        self.lbEmail.setFont(font)
        self.txtEmail = QLineEdit(self.centralwidget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(460, 280, 211, 31))
        self.txtEmail.setFont(font1)
        self.txtEmail.setMaxLength(100)
        self.lbSala = QLabel(self.centralwidget)
        self.lbSala.setObjectName(u"lbSala")
        self.lbSala.setGeometry(QRect(380, 340, 71, 20))
        self.lbSala.setFont(font)
        self.cbSala = QComboBox(self.centralwidget)
        self.cbSala.addItem("")
        self.cbSala.setObjectName(u"cbSala")
        self.cbSala.setGeometry(QRect(460, 340, 211, 31))
        self.cbSala.setFont(font3)
        self.lbFecha = QLabel(self.centralwidget)
        self.lbFecha.setObjectName(u"lbFecha")
        self.lbFecha.setGeometry(QRect(30, 350, 81, 20))
        self.lbFecha.setFont(font)
        self.dateReserva = QDateEdit(self.centralwidget)
        self.dateReserva.setObjectName(u"dateReserva")
        self.dateReserva.setGeometry(QRect(130, 340, 201, 31))
        self.dateReserva.setFont(font3)
        self.dateReserva.setCalendarPopup(True)
        self.lbHoraInicio = QLabel(self.centralwidget)
        self.lbHoraInicio.setObjectName(u"lbHoraInicio")
        self.lbHoraInicio.setGeometry(QRect(10, 410, 100, 20))
        self.lbHoraInicio.setFont(font)
        self.timeInicio = QTimeEdit(self.centralwidget)
        self.timeInicio.setObjectName(u"timeInicio")
        self.timeInicio.setGeometry(QRect(130, 400, 201, 31))
        self.timeInicio.setFont(font3)
        self.lbHoraFin = QLabel(self.centralwidget)
        self.lbHoraFin.setObjectName(u"lbHoraFin")
        self.lbHoraFin.setGeometry(QRect(370, 400, 91, 31))
        self.lbHoraFin.setFont(font)
        self.timeFin = QTimeEdit(self.centralwidget)
        self.timeFin.setObjectName(u"timeFin")
        self.timeFin.setGeometry(QRect(460, 400, 211, 31))
        self.timeFin.setFont(font3)
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(290, 470, 171, 61))
        font4 = QFont()
        font4.setFamilies([u"Arial Black"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.btnGuardar.setFont(font4)
        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(110, 470, 91, 30))
        self.btnLimpiar.setFont(font4)
        self.btnActualizar = QPushButton(self.centralwidget)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setGeometry(QRect(500, 180, 111, 30))
        self.btnActualizar.setFont(font4)
        self.btnBorrarRegistro = QPushButton(self.centralwidget)
        self.btnBorrarRegistro.setObjectName(u"btnBorrarRegistro")
        self.btnBorrarRegistro.setGeometry(QRect(520, 470, 151, 30))
        self.btnBorrarRegistro.setFont(font4)
        self.btnBuscar_ = QPushButton(self.centralwidget)
        self.btnBuscar_.setObjectName(u"btnBuscar_")
        self.btnBuscar_.setGeometry(QRect(420, 180, 51, 31))
        self.btnBuscar_.setMaximumSize(QSize(51, 31))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.btnBuscar_.setFont(font5)
        self.btnBuscar_.setCursor(QCursor(Qt.CursorShape.BusyCursor))
        self.btnBuscar_.setStyleSheet(u"blackground : transparent;")
        icon = QIcon()
        icon.addFile(u"../../../../yyyy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBuscar_.setIcon(icon)
        self.btnBuscar_.setIconSize(QSize(20, 20))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-190, 350, 120, 80))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 340, 21, 31))
        self.label_2.setPixmap(QPixmap(u"../../../../IMG_7520.png"))
        self.label_2.setScaledContents(True)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 10, 461, 51))
        self.lblTitulo = QLabel(self.centralwidget)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setGeometry(QRect(160, 20, 391, 31))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.lblTitulo.setFont(font6)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 728, 33))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"Sistema de Gesti\u00f3n de Reservas", None))
        self.lbNombre.setText(QCoreApplication.translate("vtnPrincipal", u"Nombre y Apellido:", None))
        self.lbCedula.setText(QCoreApplication.translate("vtnPrincipal", u"C\u00e9dula:", None))
        self.lbDepartamento.setText(QCoreApplication.translate("vtnPrincipal", u"Departamento:", None))
        self.lbEmail.setText(QCoreApplication.translate("vtnPrincipal", u"Email:", None))
        self.lbSala.setText(QCoreApplication.translate("vtnPrincipal", u"Sala:", None))
        self.cbSala.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Seleccionar", None))

        self.lbFecha.setText(QCoreApplication.translate("vtnPrincipal", u"Fecha:", None))
        self.lbHoraInicio.setText(QCoreApplication.translate("vtnPrincipal", u"Hora Inicio:", None))
        self.lbHoraFin.setText(QCoreApplication.translate("vtnPrincipal", u"Hora Fin:", None))
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"Guardar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("vtnPrincipal", u"Limpiar", None))
        self.btnActualizar.setText(QCoreApplication.translate("vtnPrincipal", u"Actualizar", None))
        self.btnBorrarRegistro.setText(QCoreApplication.translate("vtnPrincipal", u"Borrar Registro", None))
        self.btnBuscar_.setText(QCoreApplication.translate("vtnPrincipal", u"Buscar", None))
        self.label_2.setText("")
        self.lblTitulo.setText(QCoreApplication.translate("vtnPrincipal", u"SISTEMA DE REGISTRO DE SALAS COORPORATIVAS", None))
    # retranslateUi

from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QDate, QTime
from src.servicio.reserva_servicio import ReservaServicio

class VentanaPrincipal(QMainWindow, Ui_vtnPrincipal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.servicio = ReservaServicio()

        #Solo numeros y maximo 10 digitos en cédula
        self.txtCedula.setValidator(QIntValidator(0, 2147483647))
        self.txtCedula.setMaxLength(10)

        #Limpiar y agregar opciones correctas al ComboBox de Sala
        self.cbSala.clear()
        self.cbSala.addItem("Seleccionar")
        self.cbSala.addItem("Ejecutiva")
        self.cbSala.addItem("Conferencia")

        #Conectar botones a metodos
        self.btnGuardar.clicked.connect(self.guardar_reserva)
        self.btnLimpiar.clicked.connect(self.limpiar_campos)
        self.btnBuscar_.clicked.connect(self.buscar_reserva)
        self.btnActualizar.clicked.connect(self.actualizar_reserva)
        self.btnBorrarRegistro.clicked.connect(self.borrar_reserva)

    def guardar_reserva(self):
        try:
            cedula = self.txtCedula.text().strip()
            nombre = self.txtNombre.text().strip()
            departamento = self.txtDepartamento.text().strip().lower()
            email = self.txtEmail.text().strip()
            sala = self.cbSala.currentText()
            fecha = self.dateReserva.date().toString("yyyy-MM-dd")
            hora_inicio = self.timeInicio.time().toString("HH:mm")
            hora_fin = self.timeFin.time().toString("HH:mm")

            # Validar campos obligatorios
            if not all([cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin]):
                QMessageBox.warning(self, "Validación", "Completa todos los campos obligatorios.")
                return

            if sala == "Seleccionar":
                QMessageBox.warning(self, "Validación", "Debes seleccionar una sala.")
                return

            if "@" not in email:
                QMessageBox.warning(self, "Validación", "Ingresa un correo válido (debe contener '@').")
                return

            if len(cedula) != 10 or not cedula.isdigit():
                QMessageBox.warning(self, "Validación", "La cédula debe tener exactamente 10 dígitos numéricos.")
                return

            # Validar fecha y hora diferente a predeterminadas
            if fecha == "2000-01-01":
                QMessageBox.warning(self, "Validación", "Selecciona una fecha válida.")
                return

            if hora_inicio == "00:00" or hora_fin == "00:00":
                QMessageBox.warning(self, "Validación", "Debes seleccionar una hora válida diferente a 00:00.")
                return

            if hora_inicio >= hora_fin:
                QMessageBox.warning(self, "Validación", "La hora de inicio debe ser menor a la hora de fin.")
                return

            # Validar horario para usuarios externos
            DEPARTAMENTOS_INTERNOS = [
                "gerencia", "marketing", "ventas", "recursos humanos",
                "administracion", "produccion"
            ]
            if departamento not in DEPARTAMENTOS_INTERNOS:
                if hora_inicio < "08:00" or hora_fin > "17:00":
                    QMessageBox.warning(
                        self,
                        "Horario inválido",
                        "Usuarios externos solo pueden reservar entre 08:00 y 17:00."
                    )
                    return

            # Guardar reserva usando el servicio
            self.servicio.crear_reserva(
                cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin
            )
            QMessageBox.information(self, "Reserva", "Reserva registrada exitosamente.")
            self.limpiar_campos()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def buscar_reserva(self):
        cedula = self.txtCedula.text().strip()
        if not cedula or len(cedula) != 10:
            QMessageBox.warning(self, "Buscar", "Ingresa una cédula válida de 10 dígitos.")
            return

        reserva = self.servicio.buscar_reserva_por_cedula(cedula)
        if reserva:
            self.txtNombre.setText(reserva[2])
            self.txtDepartamento.setText(reserva[3] if reserva[3] else "")
            self.txtEmail.setText(reserva[4] if reserva[4] else "")
            self.cbSala.setCurrentText(reserva[5] if reserva[5] else "Seleccionar")
            #CORRECCION DE FECHA
            fecha_db = reserva[6]
            if not isinstance(fecha_db, str):
                fecha_str = fecha_db.strftime("%Y-%m-%d")
            else:
                fecha_str = fecha_db
            self.dateReserva.setDate(QDate.fromString(fecha_str, "yyyy-MM-dd"))
            # ---
            if reserva[7]:
                self.timeInicio.setTime(QTime.fromString(reserva[7], "HH:mm"))
            if reserva[8]:
                self.timeFin.setTime(QTime.fromString(reserva[8], "HH:mm"))
        else:
            QMessageBox.information(self, "Buscar", "No se encontró una reserva con esa cédula.")
            self.limpiar_campos()

    def actualizar_reserva(self):
        cedula = self.txtCedula.text().strip()
        nombre = self.txtNombre.text().strip()
        departamento = self.txtDepartamento.text().strip().lower()
        email = self.txtEmail.text().strip()
        sala = self.cbSala.currentText()
        fecha = self.dateReserva.date().toString("yyyy-MM-dd")
        hora_inicio = self.timeInicio.time().toString("HH:mm")
        hora_fin = self.timeFin.time().toString("HH:mm")

        #Validar campos obligatorios
        if not all([cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin]):
            QMessageBox.warning(self, "Validación", "Completa todos los campos obligatorios.")
            return

        if sala == "Seleccionar":
            QMessageBox.warning(self, "Validación", "Debes seleccionar una sala.")
            return

        if "@" not in email:
            QMessageBox.warning(self, "Validación", "Ingresa un correo válido (debe contener '@').")
            return

        if len(cedula) != 10 or not cedula.isdigit():
            QMessageBox.warning(self, "Validación", "La cédula debe tener exactamente 10 dígitos numéricos.")
            return

        #Departamentos internos permitidos
        DEPARTAMENTOS_INTERNOS = [
            "gerencia", "marketing", "ventas", "recursos humanos", "administracion", "produccion"
        ]

        #Validacion de horario para usuarios externos
        if departamento not in DEPARTAMENTOS_INTERNOS:
            if hora_inicio < "08:00" or hora_fin > "17:00":
                QMessageBox.warning(
                    self,
                    "Horario inválido",
                    "Usuarios externos solo pueden reservar entre 08:00 y 17:00."
                )
                return

        actualizado = self.servicio.actualizar_reserva(
            cedula, nombre, departamento, email, sala, fecha, hora_inicio, hora_fin
        )

        if actualizado:
            QMessageBox.information(self, "Actualizar", "Reserva actualizada correctamente.")
        else:
            QMessageBox.warning(self, "Actualizar", "No se encontró la reserva para actualizar.")

    def borrar_reserva(self):
        cedula = self.txtCedula.text().strip()
        if not cedula or len(cedula) != 10:
            QMessageBox.warning(self, "Eliminar", "Ingresa una cédula válida de 10 dígitos.")
            return

        confirmado = QMessageBox.question(
            self, "Eliminar", "¿Seguro que deseas borrar esta reserva?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirmado == QMessageBox.Yes:
            borrado = self.servicio.eliminar_reserva(cedula)
            if borrado:
                QMessageBox.information(self, "Eliminar", "Reserva eliminada.")
                self.limpiar_campos()
            else:
                QMessageBox.warning(self, "Eliminar", "No se encontró la reserva para eliminar.")

    def limpiar_campos(self):
        self.txtNombre.clear()
        self.txtCedula.clear()
        self.txtDepartamento.clear()
        self.txtEmail.clear()
        self.cbSala.setCurrentIndex(0)
        self.dateReserva.setDate(QDate.currentDate())
        self.timeInicio.setTime(QTime(0, 0))
        self.timeFin.setTime(QTime(0, 0))
