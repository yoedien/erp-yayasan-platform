from PySide6.QtCore import QAbstractTableModel
from PySide6.QtCore import QModelIndex
from PySide6.QtCore import Qt


class UserTableModel(QAbstractTableModel):

    HEADERS = [
        "ID",
        "Username",
        "Nama",
        "Role",
        "Unit",
    ]

    def __init__(self, users=None):
        super().__init__()

        self.users = users or []

    def rowCount(self, parent=QModelIndex()):

        return len(self.users)

    def columnCount(self, parent=QModelIndex()):

        return len(self.HEADERS)

    def headerData(self, section, orientation, role):

        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self.HEADERS[section]

        return str(section + 1)

    def data(self, index, role):

        if not index.isValid():
            return None

        if role != Qt.DisplayRole:
            return None

        user = self.users[index.row()]

        values = [
            user.id,
            user.username,
            user.full_name,
            user.role.name,
            user.unit.name,
        ]

        return values[index.column()]

    def set_users(self, users):

        self.beginResetModel()

        self.users = users

        self.endResetModel()