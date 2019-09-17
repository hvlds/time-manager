from PySide2.QtCore import QObject, Signal, QThread, Property
from time import sleep
from datetime import timedelta


class PomodoroWorker(QThread):
    on_start = Signal(object)
    on_stop = Signal(object)

    def __init__(self, minutes):
        QThread.__init__(self)
        self.running_flag = False
        self.minutes = minutes
        self.time = timedelta(minutes=minutes)

    def run(self):
        self.running_flag = True
        while self.running_flag:
            if self.time != timedelta(seconds=0):
                self.on_start.emit(self.time)
                self.time = self.time - timedelta(seconds=1)
                sleep(1)
            else:
                self.running_flag = False
                break

    def stop(self):
        self.running_flag = False
        self.time = timedelta(minutes=self.minutes)


class Pomodoro(QObject):
    def __init__(self):
        QObject.__init__(self)
        self._text = "0:25:00"
        self.minutes = 25
        self.thread = PomodoroWorker(self.minutes)
        self._start_visibility = True
        self._stop_visibility = False

    def _get_text(self):
        return self._text

    def _set_text(self,value):
        self._text = value

    def _get_start_visibility(self):
        return self._start_visibility

    def _set_start_visibility(self, value):
        self._start_visibility = value

    def _get_stop_visibility(self):
        return  self._stop_visibility

    def _set_stop_visibility(self, value):
        self._stop_visibility = value

    on_start_visibility = Signal()
    on_stop_visibility = Signal()
    on_text = Signal()

    start_visibility = Property(bool, _get_start_visibility, notify=on_start_visibility)
    stop_visibility = Property(bool, _get_stop_visibility, notify=on_stop_visibility)
    text = Property(str, _get_text, notify=on_text)
