from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHBoxLayout,
)

from erp.database.session import SessionLocal
from erp.gui.dialogs.proposal_dialog import ProposalDialog
from erp.repositories.proposal_repository import (
    ProposalRepository,
)


class ProposalPage(QWidget):

    def __init__(self):
        super().__init__()

        self.session = SessionLocal()

        self.repository = ProposalRepository(self.session)

        self.build_ui()

        self.load_data()

    def build_ui(self):

        layout = QVBoxLayout(self)

        toolbar = QHBoxLayout()

        self.btn_add = QPushButton("Tambah Pengajuan")

        self.btn_refresh = QPushButton("Refresh")

        toolbar.addWidget(self.btn_add)
        toolbar.addWidget(self.btn_refresh)
        toolbar.addStretch()

        layout.addLayout(toolbar)

        self.table = QTableWidget()

        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels(
            [
                "Nomor",
                "Tanggal",
                "Unit",
                "Pemohon",
                "Status",
                "Total",
            ]
        )

        layout.addWidget(self.table)

        self.btn_refresh.clicked.connect(self.load_data)

        self.btn_add.clicked.connect(
            self.open_dialog
)

    def load_data(self):

        proposals = self.repository.get_all()

        self.table.setRowCount(len(proposals))

        for row, proposal in enumerate(proposals):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(proposal.number),
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(proposal.proposal_date.strftime("%d-%m-%Y")),
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(proposal.unit.name),
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(proposal.requester.full_name),
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(proposal.status),
            )

            self.table.setItem(
                row,
                5,
                QTableWidgetItem(f"{proposal.total:,.0f}"),
            )

    def open_dialog(self):

        dialog = ProposalDialog(self)

        result = dialog.exec()

        if result:
            self.load_data()

    def closeEvent(
        self,
        event,
    ):

        self.session.close()

        super().closeEvent(event)
