from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2 import QtGui
import sys

if __name__ == "__main__":
    sys.argv += ["--style", "material"]
    app = QtGui.QGuiApplication(sys.argv)

    #QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    #QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    engine = QQmlApplicationEngine("view.qml")

    sys.exit(app.exec_())
