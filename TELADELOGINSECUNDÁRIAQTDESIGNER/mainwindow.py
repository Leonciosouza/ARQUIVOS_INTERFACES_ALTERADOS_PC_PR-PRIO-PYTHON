# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from Tela_sec_Login import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # classe Ui_MainWindow deve estar contida dentro do arquivo (login.py)
        # gerado depois de compilada a interface gráfica 
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
