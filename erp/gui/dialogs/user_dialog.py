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

from erp.services.role_service import RoleService
from erp.services.unit_service import UnitService
from erp.services.user_service import UserService


class UserDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.role_service = RoleService()
        self.unit_service = UnitService()
        self.user_service = UserService()

        self.setWindowTitle("Tambah User")
        self.resize(400, 250)

        self.build_ui()
        self.load_data()

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
        self.btn_save.clicked.connect(self.save_user)

    def load_data(self):

        self.role.clear()
        self.unit.clear()

        for role in self.role_service.get_roles():
            self.role.addItem(role.name, role.id)

        for unit in self.unit_service.get_units():
            self.unit.addItem(unit.name, unit.id)

    def save_user(self):

        username = self.username.text().strip()
        full_name = self.full_name.text().strip()
        password = self.password.text()
        role_id = self.role.currentData()
        unit_id = self.unit.currentData()

        if not username:
            QMessageBox.warning(
                self,
                "Peringatan",
                "Username harus diisi."
            )
            return

        if not full_name:
            QMessageBox.warning(
                self,
                "Peringatan",
                "Nama harus diisi."
            )
            return

        if not password:
            QMessageBox.warning(
                self,
                "Peringatan",
                "Password harus diisi."
            )
            return

        try:

            self.user_service.create_user(
                username=username,
                password=password,
                full_name=full_name,
                role_id=role_id,
                unit_id=unit_id,
            )

            QMessageBox.information(
                self,
                "Sukses",
                "User berhasil ditambahkan."
            )

            self.accept()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )