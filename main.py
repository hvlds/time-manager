from PySide2.QtCore import QUrl
from PySide2.QtQml import QQmlApplicationEngine
from PySide2 import QtGui
import sys
from timer import Timer

if __name__ == "__main__":
    sys.argv += ["--style", "material"]
    app = QtGui.QGuiApplication(sys.argv)
    timer = Timer()
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("timer", timer)
    engine.load(QUrl("./qml/view.qml"))

    sys.exit(app.exec_())
