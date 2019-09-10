from PySide2.QtCore import QUrl
from PySide2.QtQml import QQmlApplicationEngine
from PySide2 import QtGui
import sys
from chronometer import Chronometer

if __name__ == "__main__":
    sys.argv += ["--style", "material"]
    app = QtGui.QGuiApplication(sys.argv)
    chronometer = Chronometer()
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("chronometer", chronometer)
    engine.load(QUrl("view.qml"))

    sys.exit(app.exec_())
