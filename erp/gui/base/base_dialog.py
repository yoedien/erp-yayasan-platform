from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
)


class BaseDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(900, 600)

        self.main_layout = QVBoxLayout(self)

        self.content_layout = QVBoxLayout()

        self.main_layout.addLayout(self.content_layout)

        self.build_buttons()

    def build_buttons(self):

        button_layout = QHBoxLayout()

        button_layout.addStretch()

        self.btn_save = QPushButton("Simpan")

        self.btn_cancel = QPushButton("Batal")

        button_layout.addWidget(self.btn_save)

        button_layout.addWidget(self.btn_cancel)

        self.main_layout.addLayout(button_layout)

        self.btn_cancel.clicked.connect(self.reject)
