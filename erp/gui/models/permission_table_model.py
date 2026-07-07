from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)


class PermissionTableModel(QAbstractTableModel):

    HEADERS = [
        "ID",
        "Code",
        "Nama Permission",
        "Module",
        "Keterangan",
    ]

    def __init__(self, permissions=None):
        super().__init__()

        self.permissions = permissions or []

    def rowCount(
        self,
        parent=QModelIndex(),
    ):

        return len(self.permissions)

    def columnCount(
        self,
        parent=QModelIndex(),
    ):

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

        item = self.permissions[index.row()]

        values = [
            item.id,
            item.code,
            item.name,
            item.module,
            item.description or "",
        ]

        return values[index.column()]

    def set_permissions(
        self,
        permissions,
    ):

        self.beginResetModel()

        self.permissions = permissions

        self.endResetModel()