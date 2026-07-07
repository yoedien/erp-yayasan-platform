from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
)


class BaseCrudDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(420, 260)

        self.layout = QVBoxLayout()

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Save
            | QDialogButtonBox.Cancel
        )

        self.buttons.accepted.connect(
            self.accept
        )

        self.buttons.rejected.connect(
            self.reject
        )

        self.setLayout(self.layout)

        self.layout.addWidget(self.buttons)