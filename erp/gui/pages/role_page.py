from PySide6.QtWidgets import QMessageBox

from erp.gui.base import BaseMasterPage
from erp.gui.dialogs.role_dialog import RoleDialog
from erp.gui.models.role_table_model import RoleTableModel
from erp.services.role_service import RoleService


class RolePage(BaseMasterPage):

    def __init__(self):
        super().__init__("Master Role")

        self.service = RoleService()

        self.model = RoleTableModel()

        self.selected_role = None

        self.table.setModel(self.model)

        self.table.clicked.connect(
            self.select_role
        )

        self.on_add(self.add_role)
        self.on_edit(self.edit_role)
        self.on_delete(self.delete_role)
        self.on_refresh(self.load_data)

        self.load_data()

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