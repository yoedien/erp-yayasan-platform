from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
)

from erp.gui.widgets import (
    CrudToolbar,
    DataTable,
    PageTitle,
    SearchBox,
)


class BaseMasterPage(QWidget):

    def __init__(self, title: str):
        super().__init__()

        self.title = PageTitle(title)
        self.toolbar = CrudToolbar()
        self.search = SearchBox()
        self.table = DataTable()

        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.search)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def on_add(self, callback):
        self.toolbar.add_clicked.connect(callback)

    def on_edit(self, callback):
        self.toolbar.edit_clicked.connect(callback)

    def on_delete(self, callback):
        self.toolbar.delete_clicked.connect(callback)

    def on_refresh(self, callback):
        self.toolbar.refresh_clicked.connect(callback)