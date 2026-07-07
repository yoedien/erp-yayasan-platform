from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)

from erp.gui.themes import Theme


class DataTable(QTableView):

    def __init__(self):
        super().__init__()

        self.setAlternatingRowColors(True)

        self.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        self.setSortingEnabled(True)

        self.setShowGrid(False)

        self.verticalHeader().hide()

        self.horizontalHeader().setStretchLastSection(True)

        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )

        self.setStyleSheet(
            f"""
            QTableView {{
                background: white;
                border:1px solid {Theme.BORDER};
                border-radius:{Theme.RADIUS}px;
                alternate-background-color:#F9FAFB;
                selection-background-color:{Theme.PRIMARY};
                selection-color:white;
                gridline-color:{Theme.BORDER};
            }}

            QHeaderView::section {{
                background:#F3F4F6;
                padding:8px;
                border:none;
                border-bottom:1px solid {Theme.BORDER};
                font-weight:bold;
            }}
            """
        )