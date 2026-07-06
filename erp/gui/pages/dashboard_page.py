from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class DashboardPage(QWidget):

    def __init__(self, user):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Dashboard"))
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

        layout.addStretch()

        self.setLayout(layout)