from PySide6.QtWidgets import QMessageBox

from erp.gui.base import BaseMasterPage
from erp.gui.dialogs.category_dialog import CategoryDialog
from erp.gui.models.category_table_model import (
    CategoryTableModel,
)
from erp.services.category_service import (
    CategoryService,
)


class CategoryPage(BaseMasterPage):

    def __init__(self):
        super().__init__(
            "Master Kategori Belanja"
        )

        self.service = CategoryService()

        self.model = CategoryTableModel()

        self.selected_category = None

        self.table.setModel(
            self.model
        )

        self.table.clicked.connect(
            self.select_category
        )

        self.on_add(
            self.add_category
        )

        self.on_edit(
            self.edit_category
        )

        self.on_delete(
            self.delete_category
        )

        self.on_refresh(
            self.load_data
        )

        self.load_data()

    def load_data(self):

        categories = (
            self.service.get_categories()
        )

        self.model.set_categories(
            categories
        )

        self.table.resizeColumnsToContents()

        self.selected_category = None

    def select_category(
        self,
        index,
    ):

        self.selected_category = (
            self.model.categories[
                index.row()
            ]
        )

    def add_category(self):

        dialog = CategoryDialog(
            self
        )

        if dialog.exec():

            self.load_data()

    def edit_category(self):

        if not self.selected_category:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih kategori terlebih dahulu.",
            )

            return

        dialog = CategoryDialog(
            self,
            category=self.selected_category,
        )

        if dialog.exec():

            self.load_data()

    def delete_category(self):

        if not self.selected_category:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih kategori terlebih dahulu.",
            )

            return

        jawab = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Yakin menghapus kategori '{self.selected_category.name}' ?",
            QMessageBox.Yes
            | QMessageBox.No,
        )

        if jawab == QMessageBox.No:

            return

        try:

            self.service.delete_category(
                self.selected_category.id
            )

            QMessageBox.information(
                self,
                "Berhasil",
                "Kategori berhasil dihapus.",
            )

            self.load_data()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )