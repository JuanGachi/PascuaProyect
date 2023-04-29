import os
import subprocess
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint
from ventanaregistro import RegistroVentana  # Asegúrate de que esta línea esté presente

import sys
sys.path.append(r'C:\Users\PC\Desktop\Py\Ventanas')

class VentanaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()

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

        ventana_registro = QtWidgets.QWidget()
        ventana_registro.setWindowTitle('Registro')
        ventana_registro.setGeometry(0, 0, 300, 500)
        ventana_registro.setWindowFlags(Qt.FramelessWindowHint)

        # Crear una etiqueta para la imagen de fondo
        label_fondo_registro = QtWidgets.QLabel(ventana_registro)
        label_fondo_registro.setGeometry(0, 0, 300, 500)
        label_fondo_registro.setScaledContents(True)
        label_fondo_registro.setPixmap(QtGui.QPixmap('C:/Users/PC/Desktop/Py/Ventanas/FondoRegistro.jpg'))

        # Crear elementos de la ventana
        boton_registrar = QtWidgets.QPushButton('Registrar', ventana_registro)
        boton_registrar.setGeometry(100, 250, 100, 50)
        boton_registrar.setStyleSheet("background-color: blue; color: white;")

        boton_volver = QtWidgets.QPushButton('Volver', ventana_registro)
        boton_volver.setGeometry(10, 10, 70, 30)
        boton_volver.setStyleSheet("background-color: red; color: white;")
        boton_volver.clicked.connect(self.mostrar_ventana_principal)
        
        # Crear el botón "Buscar"
        self.boton_buscar = QtWidgets.QPushButton('Buscar', self)
        self.boton_buscar.setGeometry(30, 390, 100, 100)  # Establecer posición y tamaño
        self.boton_buscar.setStyleSheet("border-radius: 50px; background-color: green; color: white;")  # Establecer estilo de botón redondeado y verde
        self.boton_buscar.clicked.connect(self.ejecutar_boton_reconocimiento)
        self.boton_buscar.setEnabled(False)  # Deshabilitar el botón "Buscar" al inicio
        
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def abrir_ventana_registro(self):
        self.hide()  # Ocultar la ventana principal
        self.ventana_registro = RegistroVentana()  # Crear una instancia de RegistroVentana
        self.ventana_registro.show()  # Mostrar la ventana de registro
        self.ventana_registro.setWindowTitle("Registro de Usuarios")
        self.ventana_registro.setFixedSize(400, 500)
        self.ventana_registro.boton_registro.clicked.connect(self.mostrar_ventana_principal)
        self.ventana_registro.boton_registro.clicked.connect(self.usuario_registrado)
    def usuario_registrado(self):
        self.ventana_registro.registrar_usuario()
        self.boton_buscar.setEnabled(True)  # Habilitar el botón "Buscar" después de que el usuario se haya registrado
        self.mostrar_ventana_principal()
    def mostrar_ventana_principal(self):
        self.ventana_registro.hide()  # Ocultar la ventana de registro
        self.show()  # Mostrar la ventana principal
    def ejecutar_boton_reconocimiento(self):
        script_path = os.path.join(os.getcwd(), "botonreconocimiento3.py")
        subprocess.run(["python", script_path])  # Ejecutar el script "botonreconocimiento3.py"


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ventana = VentanaPrincipal()

    # Centrar ventana en pantalla
    screen = QtWidgets.QDesktopWidget().screenGeometry()
    size = ventana.geometry()
    ventana.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))
    ventana.show()
    app.exec_()
