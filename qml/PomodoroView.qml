import QtQuick 2.13
import QtQuick.Controls 2.13
import QtQuick.Controls.Material 2.13
import QtQuick.Layouts 1.13

Column {
    anchors.horizontalCenter: parent.horizontalCenter
    anchors.verticalCenter: parent.verticalCenter
    Text{
        text: pomodoro.text
        font.family: "Helvetica"
        font.pointSize: 50
        color:"black"
    }
    Row {
        anchors.horizontalCenter: parent.horizontalCenter
        Button {
            id:"startPomodoro"
            text: qsTr("start!")
            visible: pomodoro.start_visibility
            onClicked: {
                pomodoro.start_clock();
            }
            Material.background: Material.Red
        }
        Button {
            id: "stopPomodoro"
            text: qsTr("stop!")
            visible: pomodoro.stop_visibility
            onClicked: {
                pomodoro.stop_clock();
            }
            Material.background: Material.Blue
        }
    }

}