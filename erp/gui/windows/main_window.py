from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QSplitter,
    QStackedWidget,
    QStatusBar,
    QTreeWidget,
    QTreeWidgetItem,
)

from erp.database.session import SessionLocal
from erp.services.authorization_service import AuthorizationService
from erp.core.permission import Permission

from erp.gui.pages.dashboard_page import DashboardPage
from erp.gui.pages.user_page import UserPage
from erp.gui.pages.role_page import RolePage
from erp.gui.pages.unit_page import UnitPage
from erp.gui.pages.partner_page import PartnerPage
from erp.gui.pages.permission_page import PermissionPage
from erp.gui.pages.role_permission_page import RolePermissionPage
from erp.gui.pages.category_page import CategoryPage
from erp.gui.pages.proposal_page import ProposalPage
from erp.gui.pages.academic_year_page import AcademicYearPage
from erp.gui.pages.fund_source_page import FundSourcePage

class MainWindow(QMainWindow):

    def __init__(self, user):

        super().__init__()

        self.user = user

        self.session = SessionLocal()

        self.auth = AuthorizationService(
            self.session
        )

        self.permissions = self.auth.get_permissions(
            self.user.role_id
        )

        self.setWindowTitle("ERP Yayasan")
        self.resize(1200, 700)

        self.build_ui()

        self.menu.itemClicked.connect(
            self.change_page
        )

    def build_ui(self):

        splitter = QSplitter(Qt.Horizontal)

        self.menu = QTreeWidget()
        self.menu.setHeaderHidden(True)

        dashboard = QTreeWidgetItem(
            ["Dashboard"]
        )

        master = QTreeWidgetItem(
            ["Master Data"]
        )

        self.menu_user = QTreeWidgetItem(
            master,
            ["User"],
        )

        self.menu_role = QTreeWidgetItem(
            master,
            ["Role"],
        )

        self.menu_permission = QTreeWidgetItem(
            master,
            ["Permission"],
        )

        self.menu_role_permission = QTreeWidgetItem(
            master,
            ["Role Permission"],
        )

        self.menu_unit = QTreeWidgetItem(
            master,
            ["Unit"],
        )

        self.menu_partner = QTreeWidgetItem(
            master,
            ["Partner"],
        )

        self.menu_category = QTreeWidgetItem(
            master,
            ["Kategori Belanja"],
        )

        self.menu_academic_year = QTreeWidgetItem(
            master,
            ["Tahun Pelajaran"],
        )

        self.menu_academic_year = QTreeWidgetItem(
            master,
            ["Sumber Dana"],
        )

        keuangan = QTreeWidgetItem(
            ["Keuangan"]
        )

        self.menu_proposal = QTreeWidgetItem(
            keuangan,
            ["Pengajuan Belanja"],
        )

        self.menu_approval = QTreeWidgetItem(
            keuangan,
            ["Approval"],
        )

        self.menu_payment = QTreeWidgetItem(
            keuangan,
            ["Pembayaran"],
        )

        laporan = QTreeWidgetItem(
            ["Laporan"]
        )

        pengaturan = QTreeWidgetItem(
            ["Pengaturan"]
        )

        self.menu.addTopLevelItem(
            dashboard
        )

        self.menu.addTopLevelItem(
            master
        )

        self.menu.addTopLevelItem(
            keuangan
        )

        self.menu.addTopLevelItem(
            laporan
        )

        self.menu.addTopLevelItem(
            pengaturan
        )

        self.menu.expandAll()

        self.stack = QStackedWidget()

        self.pages = {
            "Dashboard": DashboardPage(self.user),
            "User": UserPage(),
            "Role": RolePage(),
            "Role Permission": RolePermissionPage(),
            "Unit": UnitPage(),
            "Partner": PartnerPage(),
            "Permission": PermissionPage(),
            "Kategori Belanja": CategoryPage(),
            "Pengajuan Belanja": ProposalPage(),
            "Tahun Pelajaran": AcademicYearPage(),
            "Partner": PartnerPage(),
            "Tahun Pelajaran": AcademicYearPage(),
            "Sumber Dana": FundSourcePage(),
            "Kategori Belanja": CategoryPage(),
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

        self.apply_permissions()

    def can(
        self,
        permission: str,
    ) -> bool:

        return permission in self.permissions

    def apply_permissions(self):

        self.menu_user.setHidden(
            not self.can(
                Permission.USER_VIEW
            )
        )

        self.menu_role.setHidden(
            not self.can(
                Permission.ROLE_VIEW
            )
        )

        self.menu_role_permission.setHidden(
            not self.can(
                Permission.ROLE_VIEW
            )
        )

        self.menu_unit.setHidden(
            not self.can(
                Permission.UNIT_VIEW
            )
        )

        self.menu_partner.setHidden(
            not self.can(
                Permission.PARTNER_VIEW
            )
        )

        self.menu_permission.setHidden(
            not self.can(
                Permission.SETTING_MANAGE
            )
        )

        self.menu_category.setHidden(
            not self.can(
                Permission.SETTING_MANAGE
            )
        )

        self.menu_academic_year.setHidden(
            not self.can(
                Permission.ACADEMIC_YEAR_VIEW)
        )

    def change_page(
        self,
        item,
    ):

        page = self.pages.get(
            item.text(0)
        )

        if page:
            self.stack.setCurrentWidget(
                page
            )

    def closeEvent(
        self,
        event,
    ):

        self.session.close()

        super().closeEvent(event)
