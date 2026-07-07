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
from erp.gui.pages.partner_page import PartnerPage
from erp.gui.pages.permission_page import PermissionPage

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
        QTreeWidgetItem(master, ["Partner"])
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

        self.pages = {
            "Dashboard":
        DashboardPage(self.user),
            "User": UserPage(),
            "Role": RolePage(),
            "Unit": UnitPage(),
            "Partner": PartnerPage(),
            "Permission": PermissionPage(),
        }

        for page in self.pages.values():
            self.stack.addWidget(page)

        splitter.addWidget(self.menu)
        splitter.addWidget(self.stack)

        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 4)

        self.setCentralWidget(splitter)

        status = QStatusBar()
        status.showMessage("Ready")

        self.setStatusBar(status)

    def change_page(self, item):

        page = self.pages.get(item.text(0))

        if page:
            self.stack.setCurrentWidget(page)