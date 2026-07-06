from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class UnitPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Master Data"))
        layout.addWidget(QLabel(""))
        layout.addWidget(QLabel("Halaman Unit"))

        layout.addStretch()

        self.setLayout(layout)