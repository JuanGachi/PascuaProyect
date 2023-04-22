from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint
from ventanaregistro import RegistroVentana  # Importar la clase RegistroVentana desde el archivo ventanaregistro.py

import sys
sys.path.append(r'C:\Users\PC\Desktop\Py\Ventanas')

class PrincipalVentana(QtWidgets.QWidget):
    def __init__(self):
        super(PrincipalVentana, self).__init__()

        # Configurar la ventana
        self.setWindowTitle('Aplicación Móvil')
        self.setGeometry(0, 0, 300, 500)  # Establecer tamaño de ventana
        self.setWindowFlags(Qt.FramelessWindowHint)  # Quitar borde de la ventana

        # Crear una etiqueta para la imagen de fondo
        self.label_fondo = QtWidgets.QLabel(self)
        self.label_fondo.setGeometry(0, 0, 300, 500)  # Establecer tamaño de la etiqueta
        self.label_fondo.setScaledContents(True)  # Escalar imagen para ajustarse a la etiqueta
        self.label_fondo.setPixmap(QtGui.QPixmap('C:/Users/PC/Desktop/Py/Ventanas/Tratamientos.png'))
          # Establecer imagen de fondo

        # Crear elementos de la ventana
        self.boton_comenzar = QtWidgets.QPushButton('Comenzar', self)
        self.boton_comenzar.setGeometry(170, 390, 100, 100)  # Establecer posición y tamaño
        self.boton_comenzar.setStyleSheet("border-radius: 50px; background-color: blue; color: white;")  # Establecer estilo de botón redondeado y azul
        self.boton_comenzar.clicked.connect(self.abrir_ventana_registro)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def abrir_ventana_registro(self):
        self.hide()  # Ocultar la ventana principal
        ventana_registro = RegistroVentana()
        ventana_registro.show()  # Mostrar la ventana de registro

class RegistroVentana(QtWidgets.QWidget):
    def __init__(self):
        super(RegistroVentana, self).__init__()

        # Crear widgets
        self.label_nombre = QtWidgets.QLabel("Nombre:")
        self.entry_nombre = QtWidgets.QLineEdit()
        self.label_apellido = QtWidgets.QLabel("Apellido:")
        self.entry_apellido = QtWidgets.QLineEdit()
        self.label_correo = QtWidgets.QLabel("Correo:")
        self.entry_correo = QtWidgets.QLineEdit()
        self.label_contraseña = QtWidgets.QLabel("Contraseña:")
        self.entry_contraseña = QtWidgets.QLineEdit()
        self.entry_contraseña.setEchoMode(QtWidgets.QLineEdit.Password)

        self.boton_registro = QtWidgets.QPushButton("Registrarse")
        self.boton_registro.setObjectName("boton_registro")  # Asignar un nombre de objeto para aplicar el estilo
        self.boton_registro.clicked
        self.setLayout(layout)

    # Establecer estilo para la ventana
    self.setStyleSheet("""
        background-color: white;
        border: 1px solid black;
        padding: 10px;
    """)

    # Conectar a la base de datos
    self.conexion = sqlite3.connect('usuarios.db')
    self.cursor = self.conexion.cursor()

    # Crear tabla de usuarios si no existe
    self.cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, apellido TEXT, correo TEXT, contraseña TEXT)")

def registrar_usuario(self):
    # Obtener los valores ingresados por el usuario
    nombre = self.entry_nombre.text()
    apellido = self.entry_apellido.text()
    correo = self.entry_correo.text()
    contraseña = self.entry_contraseña.text()

    # Verificar si los campos están vacíos
    if nombre == "" or apellido == "" or correo == "" or contraseña == "":
        self.label_registro.setText("Error: Todos los campos son requeridos.")
        return

    # Verificar si el correo ya está registrado
    self.cursor.execute("SELECT * FROM usuarios WHERE correo=?", (correo,))
    usuario = self.cursor.fetchone()
    if usuario:
        self.label_registro.setText("Error: Este correo ya está registrado.")
        return

    # Insertar el nuevo usuario en la base de datos
    self.cursor.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?)", (nombre, apellido, correo, contraseña))
    self.conexion.commit()

    # Limpiar los campos
    self.entry_nombre.setText("")
    self.entry_apellido.setText("")
    self.entry_correo.setText("")
    self.entry_contraseña.setText("")

    # Mostrar mensaje de registro exitoso
    self.label_registro.setText("Registro exitoso.")

