from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)


class AcademicYearTableModel(QAbstractTableModel):

    headers = [
        "Kode",
        "Nama",
        "Mulai",
        "Selesai",
        "Status",
    ]

    def __init__(self):

        super().__init__()

        self.items = []

    def set_items(self, items):

        self.beginResetModel()

        self.items = items

        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):

        return len(self.items)

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

        item = self.items[index.row()]

        column = index.column()

        if column == 0:
            return item.code

        if column == 1:
            return item.name

        if column == 2:
            return item.start_date.strftime("%d-%m-%Y")

        if column == 3:
            return item.end_date.strftime("%d-%m-%Y")

        if column == 4:
            return "Aktif" if item.is_active else "Nonaktif"

        return None
