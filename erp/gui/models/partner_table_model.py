from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)


class PartnerTableModel(QAbstractTableModel):

    headers = [
        "Kode",
        "Nama",
        "Jenis",
        "PIC",
        "HP",
        "Kota",
        "Status",
    ]

    def __init__(self):
        super().__init__()

        self.partners = []

    def set_partners(self, partners):

        self.beginResetModel()

        self.partners = partners

        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):

        return len(self.partners)

    def columnCount(self, parent=QModelIndex()):

        return len(self.headers)

    def headerData(
        self,
        section,
        orientation,
        role,
    ):

        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self.headers[section]

        return str(section + 1)

    def data(
        self,
        index,
        role,
    ):

        if not index.isValid():
            return None

        if role != Qt.DisplayRole:
            return None

        partner = self.partners[index.row()]

        column = index.column()

        if column == 0:
            return partner.code

        if column == 1:
            return partner.name

        if column == 2:
            return partner.partner_type

        if column == 3:
            return partner.pic

        if column == 4:
            return partner.phone

        if column == 5:
            return partner.city

        if column == 6:
            return "Aktif" if partner.is_active else "Nonaktif"

        return None