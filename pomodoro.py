from PySide2.QtCore import QObject, Signal, QThread
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
