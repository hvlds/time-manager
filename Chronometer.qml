import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12

Column {
    Text {
        anchors.horizontalCenter: parent.horizontalCenter
        text: chronometer.text
        font.family: "Helvetica"
        font.pointSize: 55
        color:"black"
    }
    TextField {
        id: taskText
        selectByMouse: true
        anchors.horizontalCenter: parent.horizontalCenter
        width: (2/3) * applicationWindow.width
        placeholderText: qsTr("Enter task description")
    }
    Row {
        anchors.horizontalCenter: parent.horizontalCenter
        Button {
            objectName: "startButton"
            text: qsTr("start!")
            visible: chronometer.start_visibility
            onClicked: chronometer.start_clock()
            Material.background: Material.Red
        }
        Button {
            objectName: "stopButton"
            text: qsTr("stop!")
            visible: chronometer.stop_visibility
            onClicked: chronometer.stop_clock()
            Material.background: Material.Blue
        }
    }
}
