import QtQuick 2.13
import QtQuick.Controls 2.13
import QtQuick.Controls.Material 2.13
import QtQuick.Layouts 1.13

Column {
    anchors.horizontalCenter: parent.horizontalCenter
    anchors.verticalCenter: parent.verticalCenter
    spacing: 15
    Text{
        anchors.horizontalCenter: parent.horizontalCenter
        text: pomodoro.text
        font.family: "Helvetica"
        font.pointSize: 50
        color:"black"
    }
    Row {
        anchors.horizontalCenter: parent.horizontalCenter
        padding: 10 
        spacing: 15      
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
        Button {
            icon.source: "../img/svg/settings.svg"
            // Material.background: Material.Grey
            background: Rectangle {
                color: "transparent"
            }
            
            onClicked: {
                popupPomodoroSettings.open();
            }
        }        
    }
    Pane {
        id: pomodoroSummary
        Material.elevation: 3
        ColumnLayout {
            Text {
                text: qsTr("Summary of my Pomodoros")
                font.weight: Font.DemiBold
                font.pointSize: 17
            }
            RowLayout {
                Text {
                    text: qsTr("#Pomodoros today: ")
                }
                Text {
                    text: pomodoro.count_today
                }
            }
            RowLayout {
                Text {
                    text: qsTr("#Pomodoros in total: ")
                }
                Text {
                    text: pomodoro.count_total
                }
            }
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
                Text {
                    text: qsTr("Settings")
                    font.weight: Font.DemiBold
                    font.pointSize: 17
                }
                RowLayout{
                    Layout.alignment: Qt.AlignLeft
                    Text{
                        text: qsTr("Pomodoro length: ")
                    } 
                    TextField {
                        id: "pomodoroLength"
                        text: pomodoro.pomodoro_length
                        inputMethodHints: Qt.ImhDigitsOnly
                        validator: IntValidator { 
                                bottom:0; top: 120
                            }
                    }
                }
                RowLayout{
                    Layout.alignment: Qt.AlignLeft
                    Text{
                        text: qsTr("Pause length: ")
                    } 
                    TextField {
                        id: "pauseLength"
                        text: pomodoro.pause_length
                        inputMethodHints: Qt.ImhDigitsOnly
                        validator: IntValidator { 
                                bottom:0; top: 120
                            }
                    }
                }
                CheckBox {
                    id: "hasAutoPause"
                    Layout.alignment: Qt.AlignLeft
                    text: qsTr("auto Pause")
                    checked: pomodoro.has_auto_pause
                } 
                Button {
                    text: qsTr("save")
                    Layout.alignment: Qt.AlignHCenter
                    Material.background: Material.Cyan
                    onClicked: {
                        var pomodoroLengthTemp = pomodoroLength.text;
                        var pauseLengthTemp = pauseLength.text;
                        var hasAutoPauseTemp = hasAutoPause.checked;
                        if(pomodoroLengthTemp === ""){
                            pomodoroLengthTemp = 25;
                        } 
                        if(pauseLengthTemp === ""){
                            pauseLengthTemp = 5;
                        }
                        pomodoro.save_settings(pomodoroLengthTemp, pauseLengthTemp, hasAutoPauseTemp);
                        popupPomodoroSettings.close();
                    }
                }           
            }        
        }
    }  
}