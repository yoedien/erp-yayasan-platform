from PySide6.QtWidgets import (
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

from erp.services.role_service import RoleService


class RoleDialog(QDialog):

    def __init__(self, parent=None, role=None):
        super().__init__(parent)

        self.role = role
        self.service = RoleService()

        self.setWindowTitle(
            "Ubah Role" if role else "Tambah Role"
        )

        self.resize(350, 130)

        self.build_ui()

        if role:
            self.load_data()

    def build_ui(self):

        layout = QVBoxLayout()

        form = QFormLayout()

        self.name = QLineEdit()

        form.addRow("Nama Role", self.name)

        layout.addLayout(form)

        buttons = QHBoxLayout()

        self.btn_save = QPushButton("Simpan")
        self.btn_cancel = QPushButton("Batal")

        buttons.addStretch()
        buttons.addWidget(self.btn_save)
        buttons.addWidget(self.btn_cancel)

        layout.addLayout(buttons)

        self.setLayout(layout)

        self.btn_save.clicked.connect(self.save)
        self.btn_cancel.clicked.connect(self.reject)

    def load_data(self):
        self.name.setText(self.role.name)

    def save(self):

        name = self.name.text().strip()

        if not name:

            QMessageBox.warning(
                self,
                "Validasi",
                "Nama role wajib diisi."
            )
            return

        try:

            if self.role:

                self.service.update_role(
                    role_id=self.role.id,
                    name=name,
                )

            else:

                self.service.create_role(
                    name=name,
                )

            self.accept()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )