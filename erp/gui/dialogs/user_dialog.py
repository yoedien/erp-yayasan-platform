from erp.database.session import SessionLocal

from erp.services.role_service import RoleService
from erp.services.unit_service import UnitService
from erp.services.user_service import UserService

from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)


class UserDialog(QDialog):

    def __init__(self, parent=None, user=None):
        super().__init__(parent)

        self.user = user

        self.session = SessionLocal()

        self.role_service = RoleService()

        self.unit_service = UnitService()

        self.user_service = UserService()

        if self.user:
            self.setWindowTitle("Ubah User")
        else:
            self.setWindowTitle("Tambah User")

        self.resize(400, 250)

        self.build_ui()
        self.load_data()

        if self.user:
            self.load_user()

    def build_ui(self):

        layout = QVBoxLayout()

        form = QFormLayout()

        self.username = QLineEdit()
        self.full_name = QLineEdit()

        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)

        self.role = QComboBox()
        self.unit = QComboBox()

        form.addRow("Username", self.username)
        form.addRow("Nama", self.full_name)
        form.addRow("Password", self.password)
        form.addRow("Role", self.role)
        form.addRow("Unit", self.unit)

        layout.addLayout(form)

        buttons = QHBoxLayout()

        self.btn_save = QPushButton("Simpan")
        self.btn_cancel = QPushButton("Batal")

        buttons.addStretch()
        buttons.addWidget(self.btn_save)
        buttons.addWidget(self.btn_cancel)

        layout.addLayout(buttons)

        self.setLayout(layout)

        self.btn_cancel.clicked.connect(self.reject)
        self.btn_save.clicked.connect(self.save)

    def load_data(self):

        self.role.clear()
        self.unit.clear()

        for role in self.role_service.get_roles():
            self.role.addItem(role.name, role.id)

        for unit in self.unit_service.get_units():
            self.unit.addItem(unit.name, unit.id)

    def load_user(self):

        self.username.setText(self.user.username)
        self.full_name.setText(self.user.full_name)

        role_index = self.role.findData(self.user.role_id)
        if role_index >= 0:
            self.role.setCurrentIndex(role_index)

        unit_index = self.unit.findData(self.user.unit_id)
        if unit_index >= 0:
            self.unit.setCurrentIndex(unit_index)

    def save(self):

        try:

            if self.user:

                self.user_service.update_user(
                    user_id=self.user.id,
                    username=self.username.text(),
                    full_name=self.full_name.text(),
                    role_id=self.role.currentData(),
                    unit_id=self.unit.currentData(),
                )

                if self.password.text():
                    self.user_service.update_password(
                        self.user.id,
                        self.password.text(),
                    )

            else:

                self.user_service.create_user(
                    username=self.username.text(),
                    password=self.password.text(),
                    full_name=self.full_name.text(),
                    role_id=self.role.currentData(),
                    unit_id=self.unit.currentData(),
                )

            self.accept()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )

    def closeEvent(self, event):

        self.session.close()

        super().closeEvent(event)