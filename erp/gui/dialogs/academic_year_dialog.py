from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QCheckBox,
    QDateEdit,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

from erp.services.academic_year_service import AcademicYearService


class AcademicYearDialog(QDialog):

    def __init__(self, parent=None, item=None):

        super().__init__(parent)

        self.item = item

        self.service = AcademicYearService()

        self.setWindowTitle("Tahun Pelajaran")

        self.resize(450, 250)

        self.build_ui()

        if self.item:

            self.load_data()

        else:

            self.code.setText(self.service.generate_code())

    # ==========================================
    # UI
    # ==========================================

    def build_ui(self):

        layout = QVBoxLayout()

        form = QFormLayout()

        self.code = QLineEdit()
        self.code.setReadOnly(True)

        self.name = QLineEdit()

        self.start_date = QDateEdit()
        self.start_date.setCalendarPopup(True)
        self.start_date.setDate(QDate.currentDate())

        self.end_date = QDateEdit()
        self.end_date.setCalendarPopup(True)
        self.end_date.setDate(QDate.currentDate())

        self.is_active = QCheckBox("Tahun Aktif")

        form.addRow("Kode", self.code)
        form.addRow("Nama", self.name)
        form.addRow("Tanggal Mulai", self.start_date)
        form.addRow("Tanggal Selesai", self.end_date)
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

    # ==========================================
    # LOAD
    # ==========================================

    def load_data(self):

        self.code.setText(self.item.code)

        self.name.setText(self.item.name)

        self.start_date.setDate(
            QDate(
                self.item.start_date.year,
                self.item.start_date.month,
                self.item.start_date.day,
            )
        )

        self.end_date.setDate(
            QDate(
                self.item.end_date.year,
                self.item.end_date.month,
                self.item.end_date.day,
            )
        )

        self.is_active.setChecked(self.item.is_active)

    # ==========================================
    # SAVE
    # ==========================================

    def save(self):

        if not self.name.text().strip():

            QMessageBox.warning(
                self,
                "Validasi",
                "Nama Tahun Pelajaran wajib diisi.",
            )

            return

        if self.start_date.date() >= self.end_date.date():

            QMessageBox.warning(
                self,
                "Validasi",
                "Tanggal selesai harus lebih besar dari tanggal mulai.",
            )

            return

        data = {
            "code": self.code.text(),
            "name": self.name.text().strip(),
            "start_date": self.start_date.date().toPython(),
            "end_date": self.end_date.date().toPython(),
            "is_active": self.is_active.isChecked(),
        }

        try:

            if self.item:

                self.service.update_academic_year(
                    self.item.id,
                    **data,
                )

            else:

                self.service.create_academic_year(
                    **data,
                )

            self.accept()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )
