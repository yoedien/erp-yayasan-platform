from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QSplitter,
    QStackedWidget,
    QStatusBar,
    QTreeWidget,
    QTreeWidgetItem,
)

from erp.gui.pages.dashboard_page import DashboardPage
from erp.gui.pages.user_page import UserPage
from erp.gui.pages.role_page import RolePage
from erp.gui.pages.unit_page import UnitPage

class MainWindow(QMainWindow):

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.setWindowTitle("ERP Yayasan")
        self.resize(1200, 700)

        self.build_ui()
        self.menu.itemClicked.connect(self.change_page)

    def build_ui(self):

        splitter = QSplitter(Qt.Horizontal)

        # ==========================
        # Sidebar
        # ==========================

        self.menu = QTreeWidget()

        self.menu.setHeaderHidden(True)

        dashboard = QTreeWidgetItem(["Dashboard"])

        master = QTreeWidgetItem(["Master Data"])
        QTreeWidgetItem(master, ["User"])
        QTreeWidgetItem(master, ["Role"])
        QTreeWidgetItem(master, ["Unit"])
        QTreeWidgetItem(master, ["Permission"])

        keuangan = QTreeWidgetItem(["Keuangan"])
        QTreeWidgetItem(keuangan, ["Pengajuan Belanja"])
        QTreeWidgetItem(keuangan, ["Approval"])
        QTreeWidgetItem(keuangan, ["Pembayaran"])

        laporan = QTreeWidgetItem(["Laporan"])

        pengaturan = QTreeWidgetItem(["Pengaturan"])

        self.menu.addTopLevelItem(dashboard)
        self.menu.addTopLevelItem(master)
        self.menu.addTopLevelItem(keuangan)
        self.menu.addTopLevelItem(laporan)
        self.menu.addTopLevelItem(pengaturan)

        self.menu.expandAll()

        # ==========================
        # Content
        # ==========================

        self.stack = QStackedWidget()

        self.dashboard_page = DashboardPage(self.user)
        self.user_page = UserPage()
        self.role_page = RolePage()
        self.unit_page = UnitPage()

        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.user_page)
        self.stack.addWidget(self.role_page)
        self.stack.addWidget(self.unit_page)

        splitter.addWidget(self.menu)
        splitter.addWidget(self.stack)

        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 4)

        self.setCentralWidget(splitter)

        status = QStatusBar()
        status.showMessage("Ready")

        self.setStatusBar(status)

    def change_page(self, item):

        text = item.text(0)

        if text == "Dashboard":
            self.stack.setCurrentWidget(
                self.dashboard_page
            )

        elif text == "User":
            self.stack.setCurrentWidget(
                self.user_page
            )

        elif text == "Role":
            self.stack.setCurrentWidget(
                self.role_page
            )

        elif text == "Unit":
            self.stack.setCurrentWidget(
                self.unit_page
            )