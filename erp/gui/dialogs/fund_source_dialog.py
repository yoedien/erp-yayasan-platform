from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)

from erp.services.academic_year_service import AcademicYearService
from erp.services.unit_service import UnitService
from erp.services.fund_source_service import FundSourceService


class FundSourceDialog(QDialog):

    def __init__(self, parent=None, item=None):

        super().__init__(parent)

        self.item = item

        self.service = FundSourceService()

        self.academic_year_service = AcademicYearService()

        self.unit_service = UnitService()

        self.setWindowTitle("Sumber Dana")

        self.resize(500, 320)

        self.build_ui()

        self.load_combo()

        if self.item:

            self.load_data()

        else:

            self.code.setText(self.service.generate_code())

    # ==================================================

    def build_ui(self):

        layout = QVBoxLayout()

        form = QFormLayout()

        self.code = QLineEdit()
        self.code.setReadOnly(True)

        self.academic_year = QComboBox()

        self.unit = QComboBox()

        self.name = QLineEdit()

        self.description = QTextEdit()

        self.is_active = QCheckBox("Aktif")
        self.is_active.setChecked(True)

        form.addRow("Kode", self.code)
        form.addRow("Tahun Pelajaran", self.academic_year)
        form.addRow("Unit", self.unit)
        form.addRow("Nama", self.name)
        form.addRow("Keterangan", self.description)
        form.addRow("", self.is_active)

        tombol = QHBoxLayout()

        self.btn_save = QPushButton("Simpan")
        self.btn_cancel = QPushButton("Batal")

        tombol.addStretch()
        tombol.addWidget(self.btn_save)
        tombol.addWidget(self.btn_cancel)

        layout.addLayout(form)
        layout.addLayout(tombol)

        self.setLayout(layout)

        self.btn_save.clicked.connect(self.save)

        self.btn_cancel.clicked.connect(self.reject)

    # ==================================================

    def load_combo(self):

        self.academic_year.clear()

        for item in self.academic_year_service.get_academic_years():

            self.academic_year.addItem(
                item.name,
                item.id,
            )

        self.unit.clear()

        for item in self.unit_service.get_units():

            self.unit.addItem(
                item.name,
                item.id,
            )

    # ==================================================

    def load_data(self):

        self.code.setText(self.item.code)

        self.name.setText(self.item.name)

        self.description.setPlainText(self.item.description or "")

        self.is_active.setChecked(self.item.is_active)

        index = self.academic_year.findData(self.item.academic_year_id)

        if index >= 0:

            self.academic_year.setCurrentIndex(index)

        index = self.unit.findData(self.item.unit_id)

        if index >= 0:

            self.unit.setCurrentIndex(index)

    # ==================================================

    def save(self):

        if not self.name.text().strip():

            QMessageBox.warning(
                self,
                "Validasi",
                "Nama Sumber Dana wajib diisi.",
            )

            return

        data = {
            "code": self.code.text(),
            "academic_year_id": self.academic_year.currentData(),
            "unit_id": self.unit.currentData(),
            "name": self.name.text().strip(),
            "description": self.description.toPlainText().strip(),
            "is_active": self.is_active.isChecked(),
        }

        try:

            if self.item:

                self.service.update_fund_source(
                    self.item.id,
                    **data,
                )

            else:

                self.service.create_fund_source(
                    **data,
                )

            self.accept()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )
