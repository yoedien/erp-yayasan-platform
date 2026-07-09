from datetime import datetime

from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QLabel,
    QLineEdit,
    QDateEdit,
    QComboBox,
    QTextEdit,
    QPushButton,
    QWidget,
)

from PySide6.QtCore import QDate

from erp.database.session import SessionLocal

from erp.repositories.unit_repository import UnitRepository
from erp.repositories.user_repository import UserRepository
from erp.repositories.partner_repository import PartnerRepository
from erp.repositories.category_repository import CategoryRepository

class ProposalDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Pengajuan Belanja")
        self.resize(1000, 700)

        self.session = SessionLocal()

        self.unit_repo = UnitRepository(self.session)
        self.user_repo = UserRepository(self.session)
        self.partner_repo = PartnerRepository(self.session)
        self.category_repo = CategoryRepository(self.session)

        self.build_ui()

        self.load_master_data()

    def build_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel(
            "<h2>Form Pengajuan Belanja</h2>"
        )

        layout.addWidget(title)

        form = QFormLayout()

        self.txt_number = QLineEdit()
        self.txt_number.setReadOnly(True)

        self.date = QDateEdit()

        self.date.setCalendarPopup(True)

        self.date.setDate(
            QDate.currentDate()
        )

        self.cmb_unit = QComboBox()

        self.cmb_requester = QComboBox()

        self.cmb_partner = QComboBox()

        self.cmb_category = QComboBox()

        self.cmb_priority = QComboBox()

        self.cmb_priority.addItems([
            "Rendah",
            "Normal",
            "Tinggi",
            "Darurat",
        ])

        self.cmb_status = QComboBox()

        self.cmb_status.addItems([
            "Draft",
            "Submit",
        ])

        form.addRow(
            "Nomor",
            self.txt_number,
        )

        form.addRow(
            "Tanggal",
            self.date,
        )

        form.addRow(
            "Unit",
            self.cmb_unit,
        )

        form.addRow(
            "Pemohon",
            self.cmb_requester,
        )

        form.addRow(
            "Supplier",
            self.cmb_partner,
        )

        form.addRow(
            "Kategori",
            self.cmb_category,
        )

        form.addRow(
            "Prioritas",
            self.cmb_priority,
        )

        form.addRow(
            "Status",
            self.cmb_status,
        )

        layout.addLayout(form)

        self.notes = QTextEdit()

        self.notes.setMinimumHeight(100)

        layout.addWidget(QLabel("Catatan"))

        layout.addWidget(self.notes)

        buttons = QHBoxLayout()

        self.btn_save = QPushButton("Simpan Draft")
        self.btn_submit = QPushButton("Submit")
        self.btn_cancel = QPushButton("Batal")

        buttons.addStretch()

        buttons.addWidget(self.btn_save)
        buttons.addWidget(self.btn_submit)
        buttons.addWidget(self.btn_cancel)

        layout.addLayout(buttons)

        self.btn_cancel.clicked.connect(self.reject)

    def load_master_data(self):

        self.cmb_unit.clear()

        for unit in self.unit_repo.get_all():
            self.cmb_unit.addItem(
                unit.name,
                unit.id,
            )

        self.cmb_requester.clear()

        for user in self.user_repo.get_all():
            self.cmb_requester.addItem(
                user.full_name,
                user.id,
            )

        self.cmb_partner.clear()

        for partner in self.partner_repo.get_all():
            self.cmb_partner.addItem(
                partner.name,
                partner.id,
            )

        self.cmb_category.clear()

        for category in self.category_repo.get_all():
            self.cmb_category.addItem(
                category.name,
                category.id,
            )
            
    def load_master_data(self):

        self.cmb_unit.clear()

        for unit in self.unit_repo.get_all():
            self.cmb_unit.addItem(
                unit.name,
                unit.id,
            )

        self.cmb_requester.clear()

        for user in self.user_repo.get_all():
            self.cmb_requester.addItem(
                user.full_name,
                user.id,
            )

            self.cmb_partner.clear()

        for partner in self.partner_repo.get_all():
            self.cmb_partner.addItem(
                partner.name,
                partner.id,
            )

            self.cmb_category.clear()

        for category in self.category_repo.get_all():
            self.cmb_category.addItem(
                category.name,
                category.id,
            )