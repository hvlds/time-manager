import sys
from PySide2.QtCore import QUrl
from PySide2.QtQml import QQmlApplicationEngine
from PySide2 import QtGui, QtWidgets
from timer import Timer
from pomodoro import Pomodoro
from history import TaskListModel

if __name__ == "__main__":
    sys.argv += ["--style", "material"]
    # app = QtGui.QGuiApplication(sys.argv)
    app = QtWidgets.QApplication(sys.argv)
    timer = Timer()
    pomodoro = Pomodoro()
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("timer", timer)
    engine.rootContext().setContextProperty("pomodoro", pomodoro)
    engine.rootContext().setContextProperty("taskListModel", TaskListModel(engine=engine))
    engine.load(QUrl("./qml/view.qml"))

    sys.exit(app.exec_())
