from PySide6.QtWidgets import QMessageBox

from erp.gui.base import BaseMasterPage
from erp.gui.dialogs.unit_dialog import UnitDialog
from erp.gui.models.unit_table_model import UnitTableModel
from erp.services.unit_service import UnitService


class UnitPage(BaseMasterPage):

    def __init__(self):
        super().__init__("Master Unit")

        self.service = UnitService()

        self.model = UnitTableModel()

        self.selected_unit = None

        self.table.setModel(self.model)

        self.table.clicked.connect(
            self.select_unit
        )

        self.toolbar.add_clicked.connect(
            self.add_unit
        )

        self.toolbar.edit_clicked.connect(
            self.edit_unit
        )

        self.toolbar.delete_clicked.connect(
            self.delete_unit
        )

        self.toolbar.refresh_clicked.connect(
            self.load_data
        )

        self.load_data()

    def load_data(self):

        units = self.service.get_units()

        self.model.set_units(units)

        self.table.resizeColumnsToContents()

        self.selected_unit = None

    def select_unit(self, index):

        self.selected_unit = self.model.units[
            index.row()
        ]

    def add_unit(self):

        dialog = UnitDialog(self)

        if dialog.exec():
            self.load_data()

    def edit_unit(self):

        if not self.selected_unit:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih unit terlebih dahulu.",
            )

            return

        dialog = UnitDialog(
            self,
            unit=self.selected_unit,
        )

        if dialog.exec():
            self.load_data()

    def delete_unit(self):

        if not self.selected_unit:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih unit terlebih dahulu.",
            )

            return

        jawab = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Yakin menghapus unit '{self.selected_unit.name}'?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if jawab == QMessageBox.No:
            return

        try:

            self.service.delete_unit(
                self.selected_unit.id
            )

            QMessageBox.information(
                self,
                "Berhasil",
                "Unit berhasil dihapus.",
            )

            self.load_data()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )