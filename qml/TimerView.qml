import QtQuick 2.13
import QtQuick.Controls 2.13
import QtQuick.Controls.Material 2.13
import QtQuick.Layouts 1.13

Column {
    anchors.horizontalCenter: parent.horizontalCenter
    anchors.verticalCenter: parent.verticalCenter
    Text {
        anchors.horizontalCenter: parent.horizontalCenter
        text: timer.text
        font.family: "Helvetica"
        font.pointSize: 50
        color:"black"
    }
    TextField {
        id: taskText
        selectByMouse: true
        anchors.horizontalCenter: parent.horizontalCenter
        width: (2/3) * applicationWindow.width
        placeholderText: qsTr("Enter task description")
        Keys.onReturnPressed: {
            if(startButton.visible == true){
                timer.start_clock();
            } else if(stopButton.visible == true){
                timer.stop_clock(taskText.text);
                taskListModel.update();
            }
        }
    }
    Row {
        anchors.horizontalCenter: parent.horizontalCenter
        Button {
            id:"startButton"
            text: qsTr("start!")
            visible: timer.start_visibility
            onClicked: timer.start_clock()
            Material.background: Material.Red
        }
        Button {
            id: "stopButton"
            text: qsTr("stop!")
            visible: timer.stop_visibility
            onClicked: {
                timer.stop_clock(taskText.text);
                taskListModel.update()
            }
            Material.background: Material.Blue
        }
    }
}
