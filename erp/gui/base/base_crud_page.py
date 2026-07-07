from PySide6.QtWidgets import QMessageBox

from erp.gui.base.base_master_page import BaseMasterPage


class BaseCrudPage(BaseMasterPage):

    service_class = None
    table_model_class = None
    dialog_class = None

    def __init__(self, title):

        super().__init__(title)

        self.service = self.service_class()

        self.model = self.table_model_class()

        self.table.setModel(self.model)

        self.selected_item = None

        self.table.clicked.connect(
            self.select_item
        )

        self.on_add(self.add_item)

        self.on_edit(self.edit_item)

        self.on_delete(self.delete_item)

        self.on_refresh(self.load_data)

        self.load_data()

    # ==========================
    # Load
    # ==========================

    def load_data(self):

        raise NotImplementedError

    # ==========================
    # Select
    # ==========================

    def select_item(self, index):

        self.selected_item = self.model.items[
            index.row()
        ]

    # ==========================
    # Add
    # ==========================

    def add_item(self):

        dialog = self.dialog_class(self)

        if dialog.exec():

            self.load_data()

    # ==========================
    # Edit
    # ==========================

    def edit_item(self):

        if not self.selected_item:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih data terlebih dahulu.",
            )

            return

        dialog = self.dialog_class(
            self,
            item=self.selected_item,
        )

        if dialog.exec():

            self.load_data()

    # ==========================
    # Delete
    # ==========================

    def delete_item(self):

        raise NotImplementedError