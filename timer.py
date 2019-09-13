from PySide2.QtCore import QObject, Signal, Slot, Property, QThread
from time import sleep
from datetime import timedelta, datetime
from models import Database, Task


class TimerWorker(QThread):
    on_start = Signal(object)
    on_stop = Signal(object)

    def __init__(self):
        QThread.__init__(self)
        self.running_flag = False
        self.seconds = 0
        self.date_start = datetime.now()
        self.date_stop = datetime.now()

    def run(self):
        self.running_flag = True
        self.date_start = datetime.now()
        while self.running_flag:
            general_datetime = str(timedelta(seconds=self.seconds))
            self.on_start.emit(general_datetime)
            self.seconds += 1
            sleep(1)

    def stop(self):
        self.running_flag = False
        self.seconds = 0
        self.date_stop = datetime.now()
        dates = {
            "start": self.date_start,
            "stop": self.date_stop
        }
        self.on_stop.emit(dates)


class Timer(QObject):
    def __init__(self):
        QObject.__init__(self)
        self._text = "0:00:00"
        self._description = "No Description"
        self._start_visibility = True
        self._stop_visibility = False
        self.thread = TimerWorker()
        self.thread.on_start.connect(self.on_start)
        self.thread.on_stop.connect(self.on_stop)

    def _get_start_visibility(self):
        return self._start_visibility

    def _get_stop_visibility(self):
        return self._stop_visibility

    def _get_text(self):
        return self._text

    def _get_description(self):
        return self._description

    def _set_text(self, new_text):
        self._text = new_text
        self.on_text.emit()

    def _set_description(self, new_description):
        self._description = new_description

    def _set_start_visibility(self, new_visibility):
        self._start_visibility = new_visibility
        self.on_start_visibility.emit()

    def _set_stop_visibility(self, new_visibility):
        self._stop_visibility = new_visibility
        self.on_stop_visibility.emit()

    @Slot(object)
    def on_start(self, value):
        self._set_text(str(value))

    @Slot(object)
    def on_stop(self, dates):
        db = Database()
        new_task = Task(description=self._get_description(),
                        date_start=dates["start"],
                        date_stop=dates["stop"])
        db.session.add(new_task)
        db.session.commit()

    @Slot()
    def start_clock(self):
        self._set_start_visibility(False)
        self._set_stop_visibility(True)
        self.thread.start()

    @Slot(str)
    def stop_clock(self, description):
        self._set_start_visibility(True)
        self._set_stop_visibility(False)
        self._set_description(description)
        self.thread.stop()
        self.thread.quit()

    # Signal definition
    on_text = Signal()
    on_start_visibility = Signal()
    on_stop_visibility = Signal()

    # Property definition
    text = Property(str, _get_text, notify=on_text)
    start_visibility = Property(bool, _get_start_visibility, notify=on_start_visibility)
    stop_visibility = Property(bool, _get_stop_visibility, notify=on_stop_visibility)
