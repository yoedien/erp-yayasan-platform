from PySide6.QtWidgets import QMessageBox

from erp.gui.base.base_crud_page import BaseCrudPage

from erp.services.fund_source_service import (
    FundSourceService,
)

from erp.gui.models.fund_source_table_model import (
    FundSourceTableModel,
)

from erp.gui.dialogs.fund_source_dialog import (
    FundSourceDialog,
)


class FundSourcePage(BaseCrudPage):

    service_class = FundSourceService

    table_model_class = FundSourceTableModel

    dialog_class = FundSourceDialog

    def __init__(self):

        super().__init__("Master Sumber Dana")

    # ==========================================
    # LOAD DATA
    # ==========================================

    def load_data(self):

        items = self.service.get_fund_sources()

        self.model.set_items(items)

        self.table.resizeColumnsToContents()

        self.selected_item = None

    # ==========================================
    # DELETE
    # ==========================================

    def delete_item(self):

        if not self.selected_item:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih data terlebih dahulu.",
            )

            return

        jawab = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Yakin menghapus Sumber Dana '{self.selected_item.name}' ?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if jawab == QMessageBox.No:
            return

        try:

            self.service.delete_fund_source(self.selected_item.id)

            QMessageBox.information(self, "Berhasil", "Data berhasil dihapus.")

            self.load_data()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )

    # ==========================================
    # SEARCH
    # ==========================================

    def search(self, text):

        if not text.strip():

            self.load_data()

            return

        items = self.service.search(text)

        self.model.set_items(items)

        self.table.resizeColumnsToContents()
