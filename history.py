from PySide2.QtCore import QObject, Signal, Slot, Property, QAbstractListModel, QByteArray, QModelIndex
from models import Database, Task


class TaskListModel(QAbstractListModel):
    def __init__(self, engine):
        QAbstractListModel.__init__(self, engine)
        self.engine = engine

        self._COLUMNS = (QByteArray(b'description'),
                         QByteArray(b'id'),
                         QByteArray(b'date_start'),
                         QByteArray(b'date_stop'),)
        self.db = Database()
        self.task_query = list(self.db.session.query(Task).all())

    def data(self, index, role):
        if role == self._COLUMNS.index('description'):
            return self.task_query[index.row()].description
        elif role == self._COLUMNS.index('id'):
            return self.task_query[index.row()].id
        elif role == self._COLUMNS.index('date_start'):
            date_formated = self.task_query[index.row()].date_start.strftime("%d/%m/%Y, %H:%M:%S")
            return date_formated
        elif role == self._COLUMNS.index('date_stop'):
            date_formated = self.task_query[index.row()].date_stop.strftime("%d/%m/%Y, %H:%M:%S")
            return date_formated
        return None

    @Slot(int)
    def delete_task(self, index):
        self.endResetModel()
        self.removeRow(index)

    def roleNames(self):
        a = dict(enumerate(self._COLUMNS))
        return a

    def rowCount(self, parent):
        return len(self.task_query)

    @Slot(int)
    def removeRow(self, index, parent=QModelIndex()):
        task = self.db.session.query(Task).filter_by(id=int(index))
        task.delete()
        self.db.session.commit()
        self.task_query = list(self.db.session.query(Task).all())
        self.dataChanged.emit(index, index, self.task_query)
        self.endResetModel()

    @Slot()
    def update(self):
        self.task_query = list(self.db.session.query(Task).all())
        index = self.rowCount(QModelIndex()) + 1
        self.dataChanged.emit(index, index, self.task_query)
        self.endResetModel()

    def setData(self, index, value, role):
        self.task_query = list(self.db.session.query(Task).all())
        self.dataChanged.emit(index, index, self.task_query)
        self.endResetModel()
        return True

