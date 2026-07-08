from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QScrollArea,
    QGroupBox,
    QCheckBox,
    QPushButton,
    QMessageBox,
)

from erp.services.role_permission_service import (
    RolePermissionService,
)


class RolePermissionPage(QWidget):

    def __init__(self):
        super().__init__()

        self.service = RolePermissionService()

        self.roles = []
        self.permissions = []
        self.checkboxes = {}

        self.build_ui()

        self.load_roles()
        self.load_permissions()

    # ==================================================

    def build_ui(self):

        main_layout = QVBoxLayout()

        top = QHBoxLayout()

        top.addWidget(QLabel("Role"))

        self.cbo_role = QComboBox()

        top.addWidget(self.cbo_role)
        top.addStretch()

        main_layout.addLayout(top)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.container = QWidget()

        self.permission_layout = QVBoxLayout()

        self.container.setLayout(
            self.permission_layout
        )

        self.scroll.setWidget(
            self.container
        )

        main_layout.addWidget(
            self.scroll
        )

        bottom = QHBoxLayout()

        bottom.addStretch()

        self.btn_save = QPushButton(
            "Simpan"
        )

        bottom.addWidget(
            self.btn_save
        )

        main_layout.addLayout(
            bottom
        )

        self.setLayout(
            main_layout
        )

        self.cbo_role.currentIndexChanged.connect(
            self.load_role_permissions
        )

        self.btn_save.clicked.connect(
            self.save
        )

    # ==================================================

    def load_roles(self):

        self.roles = self.service.get_all_roles()

        self.cbo_role.clear()

        for role in self.roles:

            self.cbo_role.addItem(
                role.name,
                role.id,
            )

    # ==================================================

    def load_permissions(self):

        self.permissions = (
            self.service.get_all_permissions()
        )

        self.build_permission_widget()

        self.load_role_permissions()

    # ==================================================

    def build_permission_widget(self):

        while self.permission_layout.count():

            item = self.permission_layout.takeAt(0)

            if item.widget():
                item.widget().deleteLater()

        self.checkboxes.clear()

        modules = {}

        for permission in self.permissions:

            modules.setdefault(
                permission.module,
                []
            ).append(permission)

        for module_name in sorted(modules.keys()):

            group = QGroupBox(module_name)

            layout = QVBoxLayout()

            for permission in modules[module_name]:

                checkbox = QCheckBox(
                    permission.name
                )

                self.checkboxes[
                    permission.id
                ] = checkbox

                layout.addWidget(
                    checkbox
                )

            group.setLayout(layout)

            self.permission_layout.addWidget(
                group
            )

        self.permission_layout.addStretch()

    # ==================================================

    def load_role_permissions(self):

        role_id = self.cbo_role.currentData()

        if role_id is None:
            return

        for checkbox in self.checkboxes.values():
            checkbox.setChecked(False)

        role_permissions = (
            self.service.get_role_permissions(
                role_id
            )
        )

        for item in role_permissions:

            checkbox = self.checkboxes.get(
                item.permission_id
            )

            if checkbox:
                checkbox.setChecked(True)

    # ==================================================

    def save(self):

        role_id = self.cbo_role.currentData()

        if role_id is None:

            QMessageBox.warning(
                self,
                "Peringatan",
                "Role belum dipilih.",
            )

            return

        permission_ids = []

        for permission_id, checkbox in self.checkboxes.items():

            if checkbox.isChecked():

                permission_ids.append(
                    permission_id
                )

        try:

            self.service.save_permissions(
                role_id,
                permission_ids,
            )

            QMessageBox.information(
                self,
                "Berhasil",
                "Hak akses berhasil disimpan.",
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e),
            )