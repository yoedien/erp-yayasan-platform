import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLabel


app = QApplication(sys.argv)

label = QLabel("ERP Yayasan")

label.resize(300, 100)
label.show()

app.exec()