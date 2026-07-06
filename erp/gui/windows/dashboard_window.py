from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class DashboardWindow(QWidget):

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.setWindowTitle("ERP Yayasan")
        self.resize(700, 450)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("ERP Yayasan"))
        layout.addWidget(QLabel(""))

        layout.addWidget(
            QLabel(f"Selamat datang, {user.full_name}")
        )

        layout.addWidget(
            QLabel(f"Role : {user.role.name}")
        )

        layout.addWidget(
            QLabel(f"Unit : {user.unit.name}")
        )

        layout.addWidget(QLabel(""))

        self.logout_button = QPushButton("Logout")

        layout.addWidget(self.logout_button)

        self.setLayout(layout)