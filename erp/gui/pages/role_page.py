from PySide6.QtWidgets import (
    QMessageBox,
    QPushButton,
    QHBoxLayout,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from erp.gui.models.role_table_model import RoleTableModel
from erp.gui.dialogs.role_dialog import RoleDialog
from erp.services.role_service import RoleService


class RolePage(QWidget):

    def __init__(self):
        super().__init__()

        self.service = RoleService()

        self.model = RoleTableModel()

        self.selected_role = None

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
            self.select_role
        )

        self.btn_add.clicked.connect(
            self.add_role
        )

        self.btn_edit.clicked.connect(
            self.edit_role
        )

        self.btn_delete.clicked.connect(
            self.delete_role
        )

        self.btn_refresh.clicked.connect(
            self.load_data
        )

        layout.addLayout(button_layout)

        layout.addWidget(self.table)

        self.setLayout(layout)

    def load_data(self):

        roles = self.service.get_roles()

        self.model.set_roles(roles)

        self.table.resizeColumnsToContents()

        self.selected_role = None

    def select_role(self, index):

        self.selected_role = self.model.roles[
            index.row()
        ]

    def add_role(self):

        dialog = RoleDialog(self)

        if dialog.exec():
            self.load_data()

    def edit_role(self):

        if not self.selected_role:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih role terlebih dahulu.",
            )

            return

        dialog = RoleDialog(
            self,
            role=self.selected_role,
        )

        if dialog.exec():
            self.load_data()

    def delete_role(self):

        if not self.selected_role:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih role terlebih dahulu.",
            )

            return

        jawab = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Yakin menghapus role '{self.selected_role.name}'?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if jawab == QMessageBox.No:
            return

        try:

            self.service.delete_role(
                self.selected_role.id
            )

            QMessageBox.information(
                self,
                "Berhasil",
                "Role berhasil dihapus.",
            )

            self.load_data()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )