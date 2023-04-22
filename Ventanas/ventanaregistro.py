from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import sqlite3

class RegistroVentana(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Crear widgets
        self.label_nombre = QLabel("Nombre:")
        self.entry_nombre = QLineEdit()
        self.label_apellido = QLabel("Apellido:")
        self.entry_apellido = QLineEdit()
        self.label_correo = QLabel("Correo:")
        self.entry_correo = QLineEdit()
        self.label_contraseña = QLabel("Contraseña:")
        self.entry_contraseña = QLineEdit()
        self.entry_contraseña.setEchoMode(QLineEdit.Password)

        self.boton_registro = QPushButton("Registrarse")
        self.boton_registro.setObjectName("boton_registro")  # Asignar un nombre de objeto para aplicar el estilo
        self.boton_registro.clicked.connect(self.registrar_usuario)
        self.boton_registro.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

        self.label_registro = QLabel()
        self.label_registro.setStyleSheet("color: green; font-weight: bold;")

        # Crear diseño de la ventana
        layout = QGridLayout()
        layout.addWidget(self.label_nombre, 0, 0)
        layout.addWidget(self.entry_nombre, 1, 0)
        layout.addWidget(self.label_apellido, 2, 0)
        layout.addWidget(self.entry_apellido, 3, 0)
        layout.addWidget(self.label_correo, 4, 0)
        layout.addWidget(self.entry_correo, 5, 0)
        layout.addWidget(self.label_contraseña, 6, 0)
        layout.addWidget(self.entry_contraseña, 7, 0)
        layout.addWidget(self.boton_registro, 8, 0, 1, 2, alignment=Qt.AlignCenter)
        layout.addWidget(self.label_registro, 9, 0, 1, 2, alignment=Qt.AlignCenter)

        self.setLayout(layout)

        # Aplicar estilo con hoja de estilo en cascada (CSS)
        self.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #333333;
            }
            QLineEdit {
                font-size: 16px;
                padding: 5px;
                border: 1px solid #999999;
                border-radius: 5px;
            }
            QPushButton#boton_registro {
                font-size: 18px;
                padding: 10px;
                background-color: #1877F2;
                color: #FFFFFF;
                font-weight: bold;
                border-radius: 5px;
            }
            QLabel#label_registro {
                font-size: 16px;
                font-weight: bold;
                color: green;
            }
        """)

    def registrar_usuario(self):
        nombre = self.entry_nombre.text()
        apellido = self.entry_apellido.text()
        correo = self.entry_correo.text()
        contraseña = self.entry_contraseña.text()

        # Conexión a la base de datos
        conn = sqlite3.connect('Usuarios.db')
        cursor = conn.cursor()

        # Insertar registro en la tabla Usuarios
        cursor.execute("INSERT INTO usuarios (nombre, apellido, correo, contraseña) VALUES (?, ?, ?, ?)",
                       (nombre, apellido, correo, contraseña))

        # Guardar cambios y cerrar conexión a la base de datos
        conn.commit()
        conn.close()

        # Mostrar mensaje de registro exitoso
        self.label_registro.setText("¡Registro exitoso!")
        self.label_registro.setStyleSheet("color: green; font-weight: bold;")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ventana = RegistroVentana()
    ventana.setWindowTitle("Registro de Usuarios")
    ventana.setFixedSize(400, 500)
    ventana.show()
    app.exec_()
