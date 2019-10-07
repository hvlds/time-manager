from PySide2.QtCore import QObject, Signal, Slot, QThread, Property
from time import sleep
from datetime import timedelta, datetime
from models import Database, PomodoroTask


class PomodoroWorker(QThread):
    on_start = Signal(object)
    on_stop = Signal()
    on_completed = Signal(object)

    def __init__(self, minutes):
        QThread.__init__(self)
        self.running_flag = False
        self.minutes = minutes
        self.time = timedelta(minutes=self.minutes)

    def run(self):
        self.running_flag = True
        while self.running_flag:
            if self.time != timedelta(seconds=0):
                self.on_start.emit(self.time)
                self.time = self.time - timedelta(seconds=1)
                sleep(1)
            else:
                self.running_flag = False
                date = datetime.now()
                self.on_completed.emit(date)                
                break

    def stop(self):
        self.running_flag = False
        self.time = timedelta(minutes=self.minutes)        
        self.on_stop.emit()


class Pomodoro(QObject):
    def __init__(self):
        QObject.__init__(self)
        self._text = "0:25:00"
        self.minutes = 25
        self.db = Database()
        self.count_total = self.count()
        self.count_today = self.count(date=datetime.today())
        self.thread = PomodoroWorker(self.minutes)
        self.thread.on_start.connect(self.on_start)
        self.thread.on_stop.connect(self.on_stop)
        self.thread.on_completed.connect(self.on_completed)
        self._start_visibility = True
        self._stop_visibility = False
    
    def count(self, date=None):
        if date:
            count = self.db.session.query(PomodoroTask).filter_by(date=date).count()
        else:
            count = self.db.session.query(PomodoroTask).count()
        return count

    def _get_text(self):
        return self._text

    def _set_text(self,value):
        self._text = value
        self.on_text.emit()

    def _get_start_visibility(self):
        return self._start_visibility

    def _set_start_visibility(self, value):
        self._start_visibility = value
        self.on_start_visibility.emit()

    def _get_stop_visibility(self):
        return  self._stop_visibility

    def _set_stop_visibility(self, value):
        self._stop_visibility = value
        self.on_stop_visibility.emit()

    @Slot(object)
    def on_start(self, value):
        self._set_text(str(value))
    
    @Slot()
    def on_stop(self):
        self._set_text(str(timedelta(minutes=self.minutes)))

    @Slot(object)
    def on_completed(self, date):
        new_pomodoro = PomodoroTask(date=date)
        self.db.session.add(new_pomodoro)
        self.db.session.commit()                  

    @Slot()
    def start_clock(self):
        self._set_start_visibility(False)
        self._set_stop_visibility(True)
        self.thread.start()     

    @Slot()
    def stop_clock(self):
        self._set_start_visibility(True)
        self._set_stop_visibility(False)
        self._set_text(timedelta(minutes=self.minutes))
        self.thread.stop()
        self.thread.quit()

    on_start_visibility = Signal()
    on_stop_visibility = Signal()
    on_text = Signal()

    start_visibility = Property(bool, _get_start_visibility, notify=on_start_visibility)
    stop_visibility = Property(bool, _get_stop_visibility, notify=on_stop_visibility)
    text = Property(str, _get_text, notify=on_text)
