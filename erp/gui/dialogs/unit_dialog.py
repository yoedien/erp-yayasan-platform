from PySide6.QtWidgets import (
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)

from erp.services.unit_service import UnitService


class UnitDialog(QDialog):

    def __init__(
        self,
        parent=None,
        unit=None,
    ):
        super().__init__(parent)

        self.service = UnitService()

        self.unit = unit

        self.setWindowTitle(
            "Tambah Unit"
            if unit is None
            else "Ubah Unit"
        )

        self.resize(400, 180)

        self.build_ui()

        if unit:
            self.load_data()

    def build_ui(self):

        layout = QVBoxLayout()

        form = QFormLayout()

        self.code = QLineEdit()

        self.name = QLineEdit()

        form.addRow(
            "Kode",
            self.code,
        )

        form.addRow(
            "Nama Unit",
            self.name,
        )

        layout.addLayout(form)

        buttons = QHBoxLayout()

        self.btn_save = QPushButton("Simpan")

        self.btn_cancel = QPushButton("Batal")

        buttons.addStretch()

        buttons.addWidget(self.btn_save)

        buttons.addWidget(self.btn_cancel)

        layout.addLayout(buttons)

        self.setLayout(layout)

        self.btn_cancel.clicked.connect(
            self.reject
        )

        self.btn_save.clicked.connect(
            self.save
        )

    def load_data(self):

        self.code.setText(
            self.unit.code
        )

        self.name.setText(
            self.unit.name
        )

    def save(self):

        code = self.code.text().strip()

        name = self.name.text().strip()

        if not code:

            QMessageBox.warning(
                self,
                "Peringatan",
                "Kode Unit wajib diisi.",
            )

            return

        if not name:

            QMessageBox.warning(
                self,
                "Peringatan",
                "Nama Unit wajib diisi.",
            )

            return

        try:

            if self.unit is None:

                self.service.create_unit(
                    code=code,
                    name=name,
                )

            else:

                self.service.update_unit(
                    unit_id=self.unit.id,
                    code=code,
                    name=name,
                )

            self.accept()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )