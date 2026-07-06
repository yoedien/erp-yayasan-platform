from tkinter import dialog

from PySide6.QtWidgets import (
    QPushButton,
    QHBoxLayout,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from erp.gui.models.user_table_model import UserTableModel
from erp.services.user_service import UserService
from erp.gui.dialogs.user_dialog import UserDialog


class UserPage(QWidget):

    def __init__(self):
        super().__init__()

        self.service = UserService()

        self.model = UserTableModel()

        self.selected_user = None

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
            self.select_user
        )

        self.btn_add.clicked.connect(
            self.add_user
        )

        layout.addLayout(button_layout)
        layout.addWidget(self.table)

        self.setLayout(layout)

        self.btn_refresh.clicked.connect(
            self.load_data
        )

    def load_data(self):

        users = self.service.get_users()

        self.model.set_users(users)

        self.table.resizeColumnsToContents()

    def select_user(self, index):

        self.selected_user = self.model.users[
            index.row()
        ]

        print(
            self.selected_user.username
        )

    def add_user(self):

        dialog = UserDialog(self)

        if dialog.exec():

            self.load_data()