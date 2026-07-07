from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)


class RoleTableModel(QAbstractTableModel):

    HEADERS = [
        "ID",
        "Nama Role",
    ]

    def __init__(self, roles=None):
        super().__init__()

        self.roles = roles or []

    def rowCount(self, parent=QModelIndex()):
        return len(self.roles)

    def columnCount(self, parent=QModelIndex()):
        return len(self.HEADERS)

    def headerData(
        self,
        section,
        orientation,
        role,
    ):

        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self.HEADERS[section]

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

        item = self.roles[index.row()]

        values = [
            item.id,
            item.name,
        ]

        return values[index.column()]

    def set_roles(self, roles):

        self.beginResetModel()

        self.roles = roles

        self.endResetModel()