from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

from erp.gui.themes import Theme


class PageTitle(QLabel):

    def __init__(self, title: str):
        super().__init__(title)

        self.setAlignment(
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignVCenter
        )

        self.setStyleSheet(
            f"""
            QLabel {{
                color: {Theme.TEXT};
                font-family: "{Theme.FONT}";
                font-size: 20px;
                font-weight: bold;
                padding-bottom: 8px;
            }}
            """
        )