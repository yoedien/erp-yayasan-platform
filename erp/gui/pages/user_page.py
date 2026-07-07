from PySide6.QtWidgets import (
    QMessageBox,
    QPushButton,
    QHBoxLayout,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from erp.gui.models.user_table_model import UserTableModel
from erp.gui.dialogs.user_dialog import UserDialog
from erp.services.user_service import UserService


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

        self.table.clicked.connect(self.select_user)

        self.btn_add.clicked.connect(self.add_user)
        self.btn_edit.clicked.connect(self.edit_user)
        self.btn_delete.clicked.connect(self.delete_user)
        self.btn_refresh.clicked.connect(self.load_data)

        layout.addLayout(button_layout)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def load_data(self):

        users = self.service.get_users()

        self.model.set_users(users)

        self.table.resizeColumnsToContents()

        self.selected_user = None

    def select_user(self, index):

        self.selected_user = self.model.users[index.row()]

    def add_user(self):

        dialog = UserDialog(self)

        if dialog.exec():
            self.load_data()

    def edit_user(self):

        if not self.selected_user:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih user yang akan diubah.",
            )

            return

        dialog = UserDialog(
            self,
            user=self.selected_user,
        )

        if dialog.exec():
            self.load_data()

    def delete_user(self):

        if not self.selected_user:

            QMessageBox.information(
                self,
                "Informasi",
                "Silakan pilih user yang akan dihapus.",
            )
            return

        jawab = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Apakah Anda yakin ingin menghapus user '{self.selected_user.username}'?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if jawab != QMessageBox.Yes:
            return

        try:

            self.service.delete_user(
                self.selected_user.id
            )

            QMessageBox.information(
                self,
                "Berhasil",
                "User berhasil dihapus.",
            )

            self.load_data()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )