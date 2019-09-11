from PySide2.QtCore import QObject, Signal, Slot, Property, QThread
from time import sleep
from datetime import timedelta

class ChronoWorker(QThread):
    over = Signal(object)
    def __init__(self):
        QThread.__init__(self)
        self.running_flag = False
        self.seconds = 0

    def run(self):
        self.running_flag = True
        while self.running_flag:
            general_datetime = str(timedelta(seconds=self.seconds))
            self.over.emit(general_datetime)
            self.seconds += 1
            sleep(1)

    def stop(self):
        self.running_flag = False
        self.seconds = 0

class Chronometer(QObject):
    def __init__(self):
        QObject.__init__(self)
        self._text = "0:00:00"
        self._start_visibility = True
        self._stop_visibility = False
        self.thread = ChronoWorker()
        self.thread.over.connect(self.on_start)

    def _get_start_visibility(self):
        return self._start_visibility

    def _get_stop_visibility(self):
        return self._stop_visibility

    def _get_text(self):
        return self._text

    def _set_text(self, new_text):
        self._text = new_text
        self.on_text.emit()

    def _set_start_visibility(self, new_visibility):
        self._start_visibility = new_visibility
        self.on_start_visibility.emit()

    def _set_stop_visibility(self, new_visibility):
        self._stop_visibility = new_visibility
        self.on_stop_visibility.emit()

    @Slot(object)
    def on_start(self, value):
        self._set_text(str(value))

    @Slot()
    def start_clock(self):
        self._set_start_visibility(False)
        self._set_stop_visibility(True)
        self.thread.start()

    @Slot()
    def stop_clock(self):
        self._set_start_visibility(True)
        self._set_stop_visibility(False)
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