from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)

from erp.core.enums import PartnerType


class PartnerDialog(QDialog):

    def __init__(self, parent=None, partner=None):
        super().__init__(parent)

        self.partner = partner

        self.setWindowTitle("Partner")

        self.resize(500, 500)

        self.build_ui()

        if self.partner:
            self.load_data()

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
        form.addRow("No HP", self.phone)
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

        self.btn_cancel.clicked.connect(self.reject)
        self.btn_save.clicked.connect(self.save)

    def load_data(self):

        self.code.setText(self.partner.code)
        self.name.setText(self.partner.name)

        index = self.partner_type.findText(
            self.partner.partner_type
        )

        if index >= 0:
            self.partner_type.setCurrentIndex(index)

        self.pic.setText(self.partner.pic)
        self.phone.setText(self.partner.phone)
        self.email.setText(self.partner.email)
        self.city.setText(self.partner.city)
        self.npwp.setText(self.partner.npwp)
        self.address.setPlainText(self.partner.address)
        self.notes.setPlainText(self.partner.notes)
        self.is_active.setChecked(
            self.partner.is_active
        )

    def save(self):

        QMessageBox.information(
            self,
            "Informasi",
            "Logika simpan akan kita hubungkan pada langkah berikutnya.",
        )