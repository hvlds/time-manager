from PySide2.QtCore import QUrl
from PySide2.QtQml import QQmlApplicationEngine
from PySide2 import QtGui
import sys
from timer import Timer
from pomodoro import Pomodoro
from history import History

if __name__ == "__main__":
    sys.argv += ["--style", "material"]
    app = QtGui.QGuiApplication(sys.argv)
    timer = Timer()
    pomodoro = Pomodoro()
    history = History()
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("timer", timer)
    engine.rootContext().setContextProperty("pomodoro", pomodoro)
    engine.rootContext().setContextProperty("history", history)
    engine.load(QUrl("./qml/view.qml"))

    sys.exit(app.exec_())
