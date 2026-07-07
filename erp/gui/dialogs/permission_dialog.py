from PySide6.QtWidgets import (
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)

from erp.services.permission_service import PermissionService


class PermissionDialog(QDialog):

    def __init__(
        self,
        parent=None,
        permission=None,
    ):
        super().__init__(parent)

        self.permission = permission

        self.service = PermissionService()

        self.setWindowTitle(
            "Ubah Permission"
            if permission
            else "Tambah Permission"
        )

        self.resize(450, 280)

        self.build_ui()

        if permission:
            self.load_data()

    def build_ui(self):

        layout = QVBoxLayout()

        form = QFormLayout()

        self.code = QLineEdit()

        self.name = QLineEdit()

        self.module = QLineEdit()

        self.description = QTextEdit()

        self.description.setMaximumHeight(80)

        form.addRow(
            "Code",
            self.code,
        )

        form.addRow(
            "Nama Permission",
            self.name,
        )

        form.addRow(
            "Module",
            self.module,
        )

        form.addRow(
            "Keterangan",
            self.description,
        )

        layout.addLayout(form)

        buttons = QHBoxLayout()

        self.btn_save = QPushButton(
            "Simpan"
        )

        self.btn_cancel = QPushButton(
            "Batal"
        )

        buttons.addStretch()

        buttons.addWidget(
            self.btn_save
        )

        buttons.addWidget(
            self.btn_cancel
        )

        layout.addLayout(buttons)

        self.setLayout(layout)

        self.btn_save.clicked.connect(
            self.save
        )

        self.btn_cancel.clicked.connect(
            self.reject
        )

    def load_data(self):

        self.code.setText(
            self.permission.code
        )

        self.name.setText(
            self.permission.name
        )

        self.module.setText(
            self.permission.module
        )

        self.description.setPlainText(
            self.permission.description or ""
        )

    def save(self):

        code = self.code.text().strip()

        name = self.name.text().strip()

        module = self.module.text().strip()

        description = (
            self.description
            .toPlainText()
            .strip()
        )

        if not code:

            QMessageBox.warning(
                self,
                "Validasi",
                "Code wajib diisi.",
            )

            return

        if not name:

            QMessageBox.warning(
                self,
                "Validasi",
                "Nama Permission wajib diisi.",
            )

            return

        if not module:

            QMessageBox.warning(
                self,
                "Validasi",
                "Module wajib diisi.",
            )

            return

        try:

            if self.permission:

                self.service.update_permission(
                    permission_id=self.permission.id,
                    code=code,
                    name=name,
                    module=module,
                    description=description,
                )

            else:

                self.service.create_permission(
                    code=code,
                    name=name,
                    module=module,
                    description=description,
                )

            self.accept()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )