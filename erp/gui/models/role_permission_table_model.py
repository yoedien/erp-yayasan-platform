from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)


class RolePermissionTableModel(QAbstractTableModel):

    headers = [
        "Permission",
        "Diizinkan",
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

    def headerData(self, section, orientation, role):

        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self.headers[section]

        return str(section + 1)

    def data(self, index, role):

        if not index.isValid():
            return None

        if role != Qt.DisplayRole:
            return None

        item = self.items[index.row()]

        if index.column() == 0:
            return item.name

        if index.column() == 1:
            return "Ya" if getattr(item, "checked", False) else "Tidak"

        return None
