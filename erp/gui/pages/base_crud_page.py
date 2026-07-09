from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QTableWidget,
    QHeaderView,
)


class BaseCrudPage(QWidget):

    def __init__(self, title="Master Data"):
        super().__init__()

        self.title = title

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        # ==========================
        # Title
        # ==========================

        lbl = QLabel(f"<h2>{self.title}</h2>")

        layout.addWidget(lbl)

        # ==========================
        # Toolbar
        # ==========================

        toolbar = QHBoxLayout()

        self.btn_add = QPushButton("Tambah")

        self.btn_edit = QPushButton("Edit")

        self.btn_delete = QPushButton("Hapus")

        self.btn_refresh = QPushButton("Refresh")

        self.txt_search = QLineEdit()

        self.txt_search.setPlaceholderText("Cari...")

        toolbar.addWidget(self.btn_add)

        toolbar.addWidget(self.btn_edit)

        toolbar.addWidget(self.btn_delete)

        toolbar.addWidget(self.btn_refresh)

        toolbar.addStretch()

        toolbar.addWidget(self.txt_search)

        layout.addLayout(toolbar)

        # ==========================
        # Table
        # ==========================

        self.table = QTableWidget()

        self.table.setSortingEnabled(True)

        self.table.horizontalHeader().setStretchLastSection(True)

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )

        layout.addWidget(self.table)
