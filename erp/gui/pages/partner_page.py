from PySide6.QtWidgets import QMessageBox

from erp.gui.base.base_master_page import BaseMasterPage
from erp.gui.dialogs.partner_dialog import PartnerDialog
from erp.gui.models.partner_table_model import PartnerTableModel
from erp.services.partner_service import PartnerService


class PartnerPage(BaseMasterPage):

    def __init__(self):
        super().__init__("Master Partner")

        self.service = PartnerService()

        self.model = PartnerTableModel()

        self.selected_partner = None

        self.table.setModel(self.model)

        self.table.clicked.connect(
            self.select_partner
        )

        self.on_add(self.add_partner)
        self.on_edit(self.edit_partner)
        self.on_delete(self.delete_partner)
        self.on_refresh(self.load_data)

        self.load_data()

    def load_data(self):

        partners = self.service.get_partners()

        self.model.set_partners(partners)

        self.table.resizeColumnsToContents()

        self.selected_partner = None

    def select_partner(self, index):

        self.selected_partner = self.model.partners[
            index.row()
        ]

    def add_partner(self):

        dialog = PartnerDialog(self)

        if dialog.exec():
            self.load_data()

    def edit_partner(self):

        if not self.selected_partner:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih partner terlebih dahulu.",
            )

            return

        dialog = PartnerDialog(
            self,
            partner=self.selected_partner,
        )

        if dialog.exec():
            self.load_data()

    def delete_partner(self):

        if not self.selected_partner:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih partner terlebih dahulu.",
            )

            return

        jawab = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Yakin menghapus partner '{self.selected_partner.name}' ?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if jawab == QMessageBox.No:
            return

        try:

            self.service.delete_partner(
                self.selected_partner.id
            )

            QMessageBox.information(
                self,
                "Berhasil",
                "Partner berhasil dihapus.",
            )

            self.load_data()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )