from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
)


class MainWindow(QMainWindow):

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.setWindowTitle("ERP Yayasan")
        self.resize(1200, 700)

        label = QLabel(
            f"""
ERP Yayasan

Selamat Datang
{user.full_name}

Role : {user.role.name}

Unit : {user.unit.name}
"""
        )

        self.setCentralWidget(label)