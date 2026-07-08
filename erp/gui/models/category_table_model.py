from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)


class CategoryTableModel(QAbstractTableModel):

    HEADERS = [
        "Kode",
        "Nama",
        "Status",
    ]

    def __init__(self, categories=None):
        super().__init__()

        self.categories = categories or []

    def rowCount(self, parent=QModelIndex()):
        return len(self.categories)

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

        category = self.categories[
            index.row()
        ]

        values = [
            category.code,
            category.name,
            "Aktif"
            if category.is_active
            else "Non Aktif",
        ]

        return values[index.column()]

    def set_categories(
        self,
        categories,
    ):

        self.beginResetModel()

        self.categories = categories

        self.endResetModel()