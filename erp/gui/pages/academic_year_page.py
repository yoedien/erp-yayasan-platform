from erp.gui.base.base_crud_page import BaseCrudPage

from erp.services.academic_year_service import (
    AcademicYearService,
)

from erp.gui.models.academic_year_table_model import (
    AcademicYearTableModel,
)

from erp.gui.dialogs.academic_year_dialog import (
    AcademicYearDialog,
)


class AcademicYearPage(BaseCrudPage):

    service_class = AcademicYearService

    table_model_class = AcademicYearTableModel

    dialog_class = AcademicYearDialog

    def __init__(self):

        super().__init__("Master Tahun Pelajaran")

        self.search.textChanged.connect(
            self.search_data
        )

        self.table.doubleClicked.connect(
            lambda _: self.edit_item()
        )

    # =====================================
    # Load Data
    # =====================================

    def load_data(self):

        items = self.service.get_academic_years()

        self.model.set_items(items)

        self.table.resizeColumnsToContents()

        self.selected_item = None

        self.table.horizontalHeader().setStretchLastSection(True)

        self.table.resizeColumnsToContents()

    # =====================================
    # Delete
    # =====================================

    def delete_item(self):

        if not self.selected_item:

            from PySide6.QtWidgets import QMessageBox

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih data terlebih dahulu.",
            )

            return

        from PySide6.QtWidgets import QMessageBox

        jawab = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Yakin menghapus Tahun Pelajaran '{self.selected_item.name}' ?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if jawab == QMessageBox.No:
            return

        try:

            self.service.delete_academic_year(self.selected_item.id)

            QMessageBox.information(
                self,
                "Berhasil",
                "Data berhasil dihapus.",
            )

            self.load_data()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )

    def search_data(self, text):

        if not text:

            self.load_data()

            return

        items = self.service.search(text)

        self.model.set_items(items)
