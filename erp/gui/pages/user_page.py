from PySide6.QtWidgets import (
    QPushButton,
    QHBoxLayout,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from erp.gui.models.user_table_model import UserTableModel
from erp.services.user_service import UserService


class UserPage(QWidget):

    def __init__(self):
        super().__init__()

        self.service = UserService()

        self.model = UserTableModel()

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

        layout.addLayout(button_layout)
        layout.addWidget(self.table)

        self.setLayout(layout)

        self.btn_refresh.clicked.connect(
            self.load_data
        )

    def load_data(self):

        users = self.service.get_all()

        self.model.set_users(users)

        self.table.resizeColumnsToContents()