from PySide6.QtWidgets import (
    QMessageBox,
    QPushButton,
    QHBoxLayout,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from erp.gui.models.unit_table_model import UnitTableModel
from erp.gui.dialogs.unit_dialog import UnitDialog
from erp.services.unit_service import UnitService


class UnitPage(QWidget):

    def __init__(self):
        super().__init__()

        self.service = UnitService()

        self.model = UnitTableModel()

        self.selected_unit = None

        self.build_ui()

        self.load_data()

    def build_ui(self):

        layout = QVBoxLayout()

        button_layout = QHBoxLayout()

        self.btn_add = QPushButton("Tambah")
        self.btn_edit = QPushButton("Ubah")
        self.btn_delete = QPushButton("Hapus")
        self.btn_refresh = QPushButton("Refresh")

        button_layout.addWidget(self.btn_add)
        button_layout.addWidget(self.btn_edit)
        button_layout.addWidget(self.btn_delete)
        button_layout.addWidget(self.btn_refresh)
        button_layout.addStretch()

        self.table = QTableView()

        self.table.setModel(self.model)

        self.table.setSelectionBehavior(
            QTableView.SelectionBehavior.SelectRows
        )

        self.table.setSelectionMode(
            QTableView.SelectionMode.SingleSelection
        )

        self.table.clicked.connect(
            self.select_unit
        )

        self.btn_add.clicked.connect(
            self.add_unit
        )

        self.btn_edit.clicked.connect(
            self.edit_unit
        )

        self.btn_delete.clicked.connect(
            self.delete_unit
        )

        self.btn_refresh.clicked.connect(
            self.load_data
        )

        layout.addLayout(button_layout)

        layout.addWidget(self.table)

        self.setLayout(layout)

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