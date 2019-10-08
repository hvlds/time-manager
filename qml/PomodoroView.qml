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
                popupPomodoroSettings.open();
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
    Popup {
        id: popupPomodoroSettings
        modal: true
        focus: true
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent
        Pane {
            Material.elevation: 1
            ColumnLayout{
                RowLayout{
                    Layout.alignment: Qt.AlignLeft
                    Text{
                        text: qsTr("Pomodoro: ")
                    } 
                    TextField {
                        inputMethodHints: Qt.ImhDigitsOnly
                    }
                }
                RowLayout{
                    Layout.alignment: Qt.AlignLeft
                    Text{
                        text: qsTr("Pause: ")
                    } 
                    TextField {
                        inputMethodHints: Qt.ImhDigitsOnly
                    }
                }
                CheckBox {
                    Layout.alignment: Qt.AlignLeft
                    text: qsTr("auto Pause")
                    checked: true
                }            
            }        
        }
    }
    


}