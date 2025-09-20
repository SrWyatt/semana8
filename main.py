# Registro de Clientes

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QListWidget,
    QVBoxLayout, QHBoxLayout, QMessageBox, QDesktopWidget
)

class RegistroClientes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Clientes")
        self.setGeometry(100, 100, 500, 400)
        self._construir_ui()
        self.center_window() 

    def center_window(self):
        """Centrar ventana en la pantalla."""
        pantalla = QDesktopWidget().availableGeometry().center()
        frame = self.frameGeometry()
        frame.moveCenter(pantalla)
        self.move(frame.topLeft())

    def _construir_ui(self):
        # Widgets básicos
        self.lbl_nombre = QLabel("Nombre:")
        self.lbl_tel = QLabel("Teléfono:")
        self.lbl_correo = QLabel("Correo:")

        self.txt_nombre = QLineEdit()
        self.txt_tel = QLineEdit()
        self.txt_correo = QLineEdit()

        self.btn_agregar = QPushButton("Agregar")
        self.btn_guardar_csv = QPushButton("Guardar CSV")
        self.btn_limpiar = QPushButton("Limpiar")

        self.lista = QListWidget()

        # Conexiones
        self.btn_agregar.clicked.connect(self.agregar_cliente)
        self.btn_guardar_csv.clicked.connect(self.guardar_csv)
        self.btn_limpiar.clicked.connect(self.limpiar_campos)

        # Layouts 
        fila_nombre = QHBoxLayout()
        fila_nombre.addWidget(self.lbl_nombre)
        fila_nombre.addWidget(self.txt_nombre)

        fila_tel = QHBoxLayout()
        fila_tel.addWidget(self.lbl_tel)
        fila_tel.addWidget(self.txt_tel)

        fila_correo = QHBoxLayout()
        fila_correo.addWidget(self.lbl_correo)
        fila_correo.addWidget(self.txt_correo)

        fila_botones = QHBoxLayout()
        fila_botones.addWidget(self.btn_agregar)
        fila_botones.addWidget(self.btn_guardar_csv)
        fila_botones.addWidget(self.btn_limpiar)

        layout = QVBoxLayout()
        layout.addLayout(fila_nombre)
        layout.addLayout(fila_tel)
        layout.addLayout(fila_correo)
        layout.addLayout(fila_botones)
        layout.addWidget(self.lista)

        self.setLayout(layout)

    def agregar_cliente(self):
        """Agrega el cliente a la lista y lo guarda en un CSV."""
        nombre = self.txt_nombre.text()
        tel = self.txt_tel.text()
        correo = self.txt_correo.text()

        cliente = f"{nombre} | {tel} | {correo}"
        self.lista.addItem(cliente)

        try:
            with open("clientes.csv", "a", encoding="utf-8") as f:
                f.write(f"{nombre},{tel},{correo}\n")
        except:
            pass 

        self.limpiar_campos()

    def guardar_csv(self):
        """Guarda toda la lista en clientes.csv."""
        try:
            with open("clientes.csv", "w", encoding="utf-8") as f:
                for i in range(self.lista.count()):
                    texto = self.lista.item(i).text()
                    partes = [p.strip() for p in texto.split("|")]
                    if len(partes) == 3:
                        f.write(f"{partes[0]},{partes[1]},{partes[2]}\n")
            QMessageBox.information(self, "Registro", "Archivo guardado.")
        except:
            QMessageBox.warning(self, "Registro", "No se pudo guardar el registro.")

    def limpiar_campos(self):
        self.txt_nombre.clear()
        self.txt_tel.clear()
        self.txt_correo.clear()
        self.txt_nombre.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RegistroClientes()
    ventana.show()
    sys.exit(app.exec_())
