from PySide6.QtWidgets import QMessageBox

from erp.gui.base.base_master_page import BaseMasterPage
from erp.gui.dialogs.permission_dialog import PermissionDialog
from erp.gui.models.permission_table_model import PermissionTableModel
from erp.services.permission_service import PermissionService


class PermissionPage(BaseMasterPage):

    def __init__(self):
        super().__init__("Master Permission")

        self.service = PermissionService()

        self.model = PermissionTableModel()

        self.selected_permission = None

        self.table.setModel(self.model)

        self.table.clicked.connect(
            self.select_permission
        )

        self.on_add(
            self.add_permission
        )

        self.on_edit(
            self.edit_permission
        )

        self.on_delete(
            self.delete_permission
        )

        self.on_refresh(
            self.load_data
        )

        self.load_data()

    def load_data(self):

        permissions = self.service.get_permissions()

        self.model.set_permissions(
            permissions
        )

        self.table.resizeColumnsToContents()

        self.selected_permission = None

    def select_permission(
        self,
        index,
    ):

        self.selected_permission = (
            self.model.permissions[
                index.row()
            ]
        )

    def add_permission(self):

        dialog = PermissionDialog(self)

        if dialog.exec():

            self.load_data()

    def edit_permission(self):

        if not self.selected_permission:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih permission terlebih dahulu.",
            )

            return

        dialog = PermissionDialog(
            self,
            permission=self.selected_permission,
        )

        if dialog.exec():

            self.load_data()

    def delete_permission(self):

        if not self.selected_permission:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih permission terlebih dahulu.",
            )

            return

        jawab = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Yakin menghapus permission '{self.selected_permission.code}' ?",
            QMessageBox.Yes
            | QMessageBox.No,
        )

        if jawab == QMessageBox.No:
            return

        try:

            self.service.delete_permission(
                self.selected_permission.id
            )

            QMessageBox.information(
                self,
                "Berhasil",
                "Permission berhasil dihapus.",
            )

            self.load_data()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )