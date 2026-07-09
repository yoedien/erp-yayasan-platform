from PySide6.QtWidgets import (
    QLabel,
    QFormLayout,
    QLineEdit,
    QDateEdit,
    QCheckBox,
)

from PySide6.QtCore import QDate

from erp.gui.base import BaseDialog


class AcademicYearDialog(BaseDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Tahun Pelajaran")

        self.build_form()

    def build_form(self):

        title = QLabel("<h2>Tahun Pelajaran</h2>")

        self.content_layout.addWidget(title)

        form = QFormLayout()

        self.txt_code = QLineEdit()

        self.txt_name = QLineEdit()

        self.date_start = QDateEdit()

        self.date_start.setCalendarPopup(True)

        self.date_start.setDate(QDate.currentDate())

        self.date_end = QDateEdit()

        self.date_end.setCalendarPopup(True)

        self.date_end.setDate(QDate.currentDate())

        self.chk_active = QCheckBox("Tahun Pelajaran Aktif")

        form.addRow("Kode", self.txt_code)

        form.addRow("Nama", self.txt_name)

        form.addRow("Tanggal Mulai", self.date_start)

        form.addRow("Tanggal Selesai", self.date_end)

        form.addRow("", self.chk_active)

        self.content_layout.addLayout(form)
