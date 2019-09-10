from PySide2.QtCore import QObject, Signal, Slot, QUrl, Property
from PySide2.QtQml import QQmlApplicationEngine
from PySide2 import QtGui
import sys

class Chronometer(QObject):
    def __init__(self):
        QObject.__init__(self)
        self._text = "00:00"
        self._start_visibility = True
        self._stop_visibility = False

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

    @Slot()
    def start_clock(self):
        self._set_text("Running!")
        self._set_start_visibility(False)
        self._set_stop_visibility(True)

    # Signal definition
    on_text = Signal()
    on_start_visibility = Signal()
    on_stop_visibility = Signal()

    # Property definition
    text = Property(str, _get_text, notify=on_text)
    start_visibility = Property(bool, _get_start_visibility, notify=on_start_visibility)
    stop_visibility = Property(bool, _get_stop_visibility, notify=on_stop_visibility)

if __name__ == "__main__":
    sys.argv += ["--style", "material"]
    app = QtGui.QGuiApplication(sys.argv)
    chronometer = Chronometer()
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("chronometer", chronometer)
    engine.load(QUrl("view.qml"))

    sys.exit(app.exec_())
