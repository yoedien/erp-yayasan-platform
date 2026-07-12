from PySide6.QtWidgets import QApplication

from erp.gui.pages.academic_year_page import AcademicYearPage

app = QApplication([])

page = AcademicYearPage()
page.resize(900, 600)
page.show()

app.exec()
