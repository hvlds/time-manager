from PySide2.QtCore import QObject, Signal, Slot
from models import Database, Task


class History(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.tasks = dict()
        self.update()

    def update(self):
        db = Database()
        task_query = db.session.query(Task).all()
        for task in task_query:
            self.tasks[str(task.id)] = {
                "description": task.description,
                "date_start": task.date_start,
                "date_stop": task.date_stop
            }

    @Slot(result='QVariant')
    def get_tasks(self):
        return self.tasks
