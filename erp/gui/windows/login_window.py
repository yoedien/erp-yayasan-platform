from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QFormLayout,
    QMessageBox,
)

from erp.controllers import LoginController
from erp.database.session import SessionLocal
from erp.gui.windows.main_window import MainWindow


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ERP Yayasan")
        self.resize(420, 220)

        self.session = SessionLocal()
        self.controller = LoginController(self.session)

        self.label_title = QLabel("ERP Yayasan")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Masukkan username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Masukkan password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        form = QFormLayout()
        form.addRow("Username", self.username_input)
        form.addRow("Password", self.password_input)

        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addLayout(form)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):

        username = self.username_input.text().strip()
        password = self.password_input.text()

        success = self.controller.login(
            username,
            password,
        )

        if success:
            self.main_window = MainWindow(
                self.controller.current_user
        )

            self.main_window.show()

            self.close()

            QMessageBox.information(
                self,
                "Sukses",
                f"Selamat datang\n{self.controller.current_user.full_name}",
            )

        else:

            QMessageBox.warning(
                self,
                "Login Gagal",
                "Username atau password salah.",
            )

    def closeEvent(self, event):
        self.session.close()
        super().closeEvent(event)