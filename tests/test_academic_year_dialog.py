from PySide6.QtWidgets import QApplication

from erp.gui.dialogs.academic_year_dialog import AcademicYearDialog

app = QApplication([])

dialog = AcademicYearDialog()

dialog.exec()

app.exec()
