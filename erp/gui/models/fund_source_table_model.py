from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)


class FundSourceTableModel(QAbstractTableModel):

    headers = [
        "Kode",
        "Tahun Pelajaran",
        "Unit",
        "Nama",
        "Status",
    ]

    def __init__(self):

        super().__init__()

        self.items = []

    # ==========================================
    # SET DATA
    # ==========================================

    def set_items(self, items):

        self.beginResetModel()

        self.items = items

        self.endResetModel()

    # ==========================================
    # ROW
    # ==========================================

    def rowCount(self, parent=QModelIndex()):

        return len(self.items)

    # ==========================================
    # COLUMN
    # ==========================================

    def columnCount(self, parent=QModelIndex()):

        return len(self.headers)

    # ==========================================
    # HEADER
    # ==========================================

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

    # ==========================================
    # DATA
    # ==========================================

    def data(
        self,
        index,
        role,
    ):

        if not index.isValid():
            return None

        if role != Qt.DisplayRole:
            return None

        item = self.items[index.row()]

        column = index.column()

        if column == 0:
            return item.code

        if column == 1:
            return item.academic_year.name

        if column == 2:
            return item.unit.name

        if column == 3:
            return item.name

        if column == 4:
            return "Aktif" if item.is_active else "Nonaktif"

        return None
