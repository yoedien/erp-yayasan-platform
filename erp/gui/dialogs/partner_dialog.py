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

from erp.core.enums import PartnerType
from erp.services.partner_service import PartnerService


class PartnerDialog(QDialog):

    def __init__(self, parent=None, partner=None):
        super().__init__(parent)

        self.partner = partner
        self.service = PartnerService()

        self.setWindowTitle("Partner")
        self.resize(500, 550)

        self.build_ui()

        if self.partner:
            self.load_data()
        else:
            self.code.setText(
                self.service.generate_code()
            )

    def build_ui(self):

        layout = QVBoxLayout()

        form = QFormLayout()

        self.code = QLineEdit()
        self.code.setReadOnly(True)

        self.name = QLineEdit()

        self.partner_type = QComboBox()

        for item in PartnerType:
            self.partner_type.addItem(item.value)

        self.pic = QLineEdit()

        self.phone = QLineEdit()

        self.email = QLineEdit()

        self.city = QLineEdit()

        self.npwp = QLineEdit()

        self.address = QTextEdit()

        self.notes = QTextEdit()

        self.is_active = QCheckBox("Aktif")
        self.is_active.setChecked(True)

        form.addRow("Kode", self.code)
        form.addRow("Nama", self.name)
        form.addRow("Jenis", self.partner_type)
        form.addRow("PIC", self.pic)
        form.addRow("No. HP", self.phone)
        form.addRow("Email", self.email)
        form.addRow("Kota", self.city)
        form.addRow("NPWP", self.npwp)
        form.addRow("Alamat", self.address)
        form.addRow("Catatan", self.notes)
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

    def load_data(self):

        self.code.setText(self.partner.code)
        self.name.setText(self.partner.name)

        index = self.partner_type.findText(
            self.partner.partner_type
        )

        if index >= 0:
            self.partner_type.setCurrentIndex(index)

        self.pic.setText(self.partner.pic or "")
        self.phone.setText(self.partner.phone or "")
        self.email.setText(self.partner.email or "")
        self.city.setText(self.partner.city or "")
        self.npwp.setText(self.partner.npwp or "")
        self.address.setPlainText(self.partner.address or "")
        self.notes.setPlainText(self.partner.notes or "")

        self.is_active.setChecked(
            self.partner.is_active
        )

    def save(self):

        if not self.name.text().strip():

            QMessageBox.warning(
                self,
                "Validasi",
                "Nama Partner wajib diisi.",
            )

            return

        data = {

            "code": self.code.text(),

            "name": self.name.text().strip(),

            "partner_type": self.partner_type.currentText(),

            "pic": self.pic.text().strip(),

            "phone": self.phone.text().strip(),

            "email": self.email.text().strip(),

            "city": self.city.text().strip(),

            "npwp": self.npwp.text().strip(),

            "address": self.address.toPlainText().strip(),

            "notes": self.notes.toPlainText().strip(),

            "is_active": self.is_active.isChecked(),

        }

        try:

            if self.partner:

                self.service.update_partner(
                    self.partner.id,
                    **data,
                )

            else:

                self.service.create_partner(
                    **data,
                )

            self.accept()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )