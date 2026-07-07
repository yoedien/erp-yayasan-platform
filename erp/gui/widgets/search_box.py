from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit

from erp.gui.themes import Theme


class SearchBox(QLineEdit):

    search_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.setPlaceholderText("🔍 Cari...")

        self.setStyleSheet(
            f"""
            QLineEdit {{
                border:1px solid {Theme.BORDER};
                border-radius:{Theme.RADIUS}px;
                padding:8px;
                font-family:"{Theme.FONT}";
                font-size:{Theme.FONT_SIZE}pt;
                background:white;
            }}
            """
        )

        self.textChanged.connect(
            self.search_changed.emit
        )