from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)


class UnitTableModel(QAbstractTableModel):

    HEADERS = [
        "ID",
        "Kode",
        "Nama Unit",
    ]

    def __init__(self, units=None):
        super().__init__()

        self.units = units or []

    def rowCount(self, parent=QModelIndex()):
        return len(self.units)

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

    def data(self, index, role):

        if not index.isValid():
            return None

        if role != Qt.DisplayRole:
            return None

        unit = self.units[index.row()]

        values = [
            unit.id,
            unit.code,
            unit.name,
        ]

        return values[index.column()]

    def set_units(self, units):

        self.beginResetModel()

        self.units = units

        self.endResetModel()