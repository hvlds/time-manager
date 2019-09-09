import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12

ApplicationWindow {
    id: applicationWindow
    visible: true
    width: 600
    height: 600
    Column {
        spacing: 10
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            text:"00:00"
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
        Column {
            anchors.horizontalCenter: parent.horizontalCenter
            Button {
                id: startButton
                text: qsTr("start!")
                Material.background: Material.Red
            }	    
        }
    }
}
