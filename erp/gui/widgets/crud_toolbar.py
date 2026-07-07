from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
)

from erp.gui.themes import Theme


class CrudToolbar(QWidget):

    add_clicked = Signal()
    edit_clicked = Signal()
    delete_clicked = Signal()
    refresh_clicked = Signal()

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        self.btn_add = QPushButton("➕ Tambah")
        self.btn_edit = QPushButton("✏️ Ubah")
        self.btn_delete = QPushButton("🗑 Hapus")
        self.btn_refresh = QPushButton("🔄 Refresh")

        style = f"""
        QPushButton {{
            background: {Theme.PRIMARY};
            color: white;
            border: none;
            border-radius: {Theme.RADIUS}px;
            padding: 8px 16px;
            font-weight: bold;
        }}

        QPushButton:hover {{
            background: {Theme.PRIMARY_DARK};
        }}
        """

        self.btn_add.setStyleSheet(style)
        self.btn_edit.setStyleSheet(style)
        self.btn_delete.setStyleSheet(style)
        self.btn_refresh.setStyleSheet(style)

        layout.addWidget(self.btn_add)
        layout.addWidget(self.btn_edit)
        layout.addWidget(self.btn_delete)
        layout.addWidget(self.btn_refresh)
        layout.addStretch()

        self.setLayout(layout)

        self.btn_add.clicked.connect(self.add_clicked)
        self.btn_edit.clicked.connect(self.edit_clicked)
        self.btn_delete.clicked.connect(self.delete_clicked)
        self.btn_refresh.clicked.connect(self.refresh_clicked)