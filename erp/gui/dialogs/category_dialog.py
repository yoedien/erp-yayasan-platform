from PySide6.QtWidgets import (
    QCheckBox,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)

from erp.services.category_service import (
    CategoryService,
)


class CategoryDialog(QDialog):

    def __init__(
        self,
        parent=None,
        category=None,
    ):
        super().__init__(parent)

        self.category = category

        self.service = CategoryService()

        self.setWindowTitle(
            "Ubah Kategori"
            if category
            else "Tambah Kategori"
        )

        self.resize(420, 280)

        self.build_ui()

        if category:
            self.load_data()

    def build_ui(self):

        layout = QVBoxLayout()

        form = QFormLayout()

        self.code = QLineEdit()

        self.name = QLineEdit()

        self.description = QTextEdit()

        self.description.setFixedHeight(
            80
        )

        self.is_active = QCheckBox(
            "Aktif"
        )

        self.is_active.setChecked(True)

        form.addRow(
            "Kode",
            self.code,
        )

        form.addRow(
            "Nama",
            self.name,
        )

        form.addRow(
            "Keterangan",
            self.description,
        )

        form.addRow(
            "",
            self.is_active,
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

        layout.addLayout(
            buttons
        )

        self.setLayout(layout)

        self.btn_save.clicked.connect(
            self.save
        )

        self.btn_cancel.clicked.connect(
            self.reject
        )

    def load_data(self):

        self.code.setText(
            self.category.code
        )

        self.name.setText(
            self.category.name
        )

        self.description.setPlainText(
            self.category.description or ""
        )

        self.is_active.setChecked(
            self.category.is_active
        )

    def save(self):

        code = self.code.text().strip()

        name = self.name.text().strip()

        description = (
            self.description
            .toPlainText()
            .strip()
        )

        is_active = (
            self.is_active.isChecked()
        )

        if not code:

            QMessageBox.warning(
                self,
                "Validasi",
                "Kode wajib diisi.",
            )

            return

        if not name:

            QMessageBox.warning(
                self,
                "Validasi",
                "Nama wajib diisi.",
            )

            return

        try:

            if self.category:

                self.service.update_category(
                    category_id=self.category.id,
                    code=code,
                    name=name,
                    description=description,
                    is_active=is_active,
                )

            else:

                self.service.create_category(
                    code=code,
                    name=name,
                    description=description,
                    is_active=is_active,
                )

            self.accept()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )