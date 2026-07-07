from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)

from erp.gui.themes import Theme


class Card(QFrame):

    def __init__(
        self,
        title: str,
        value: str = "",
    ):
        super().__init__()

        self.setStyleSheet(
            f"""
            QFrame {{
                background:{Theme.SURFACE};
                border:1px solid {Theme.BORDER};
                border-radius:{Theme.RADIUS}px;
            }}
            """
        )

        layout = QVBoxLayout()

        layout.setContentsMargins(16, 16, 16, 16)

        self.title = QLabel(title)

        self.title.setStyleSheet(
            f"""
            color:{Theme.TEXT_SECONDARY};
            font-size:10pt;
            """
        )

        self.value = QLabel(value)

        self.value.setStyleSheet(
            f"""
            color:{Theme.TEXT};
            font-size:22pt;
            font-weight:bold;
            """
        )

        layout.addWidget(self.title)
        layout.addWidget(self.value)

        self.setLayout(layout)

    def set_value(self, value):

        self.value.setText(str(value))