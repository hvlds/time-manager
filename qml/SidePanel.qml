import QtQuick 2.13
import QtQuick.Controls 2.13
import QtQuick.Controls.Material 2.13
import QtQuick.Layouts 1.13

ToolBar {
    id: toolBar
    width: 120
    x:0
    y:0
    height: applicationWindow.height
    Material.elevation: 1
    Material.background: Material.Grey
    Text{
        y: 10
        id:sidePanelTitel
        text: " Time \n Manager"
        font.family: "Roboto"
        font.pointSize: 17
        font.weight: Font.Light
    }
    ToolButton {
        id: toolButton1
        width: toolBar.width
        icon.source: "../img/svg/new.svg"
        icon.height: 15
        icon.width: 15
        text: qsTr("Timer")
        font.weight: Font.Light
        x:0
        y:sidePanelTitel.height + sidePanelTitel.y + 10
        Rectangle
        {
            id: background1
            anchors.fill: parent
            opacity: 0.4
            color: "grey"
        }
        contentItem: Item{
            Row{
                spacing: 10
                anchors.fill: parent
                Image{
                    source: toolButton1.icon.source
                    width: toolButton1.icon.width
                    height: toolButton1.icon.height
                    anchors.verticalCenter: parent.verticalCenter
                }
                Text{
                    text: toolButton1.text
                    font: toolButton1.font
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
        }
        onClicked: {
            timerView.visible = true;
            historyView.visible = false;
            pomodoroView.visible = false;
            background1.opacity = 0.4;
            background2.opacity = 0;
            background3.opacity = 0;
            background4.opacity = 0;
        }
    }
    ToolButton {
        id: toolButton2
        width: toolBar.width
        icon.source: "../img/svg/history.svg"
        icon.height: 15
        icon.width: 15
        text: qsTr("History")
        font.weight: Font.Light
        x:0
        y:toolButton1.y + toolButton1.height + 4
        Rectangle{
            id: background2
            anchors.fill: parent
            opacity: 0
            color: "grey"
        }
        onClicked:{
            timerView.visible = false;
            historyView.visible = true;
            pomodoroView.visible = false;
            background1.opacity = 0;
            background2.opacity = 0.4;
            background3.opacity = 0;
            background4.opacity = 0;
        }
        contentItem: Item{
            Row{
                anchors.fill: parent
                spacing: 10
                Image{
                    source: toolButton2.icon.source
                    width: toolButton2.icon.width
                    height: toolButton2.icon.height
                    anchors.verticalCenter: parent.verticalCenter
                }
                Text{
                    text: toolButton2.text
                    font: toolButton2.font
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
        }
    }
    ToolButton {
        id: toolButton3
        width: toolBar.width
        icon.source: "../img/svg/pomodoro.svg"
        icon.height: 15
        icon.width: 15
        text: qsTr("Pomodoro")
        font.weight: Font.Light
        x:0
        y:toolButton2.y + toolButton2.height + 4
        Rectangle{
            id: background3
            anchors.fill: parent
            opacity: 0
            color: "grey"
        }
        contentItem: Item{
            Row{
                anchors.fill: parent
                spacing: 10
                Image{
                    source: toolButton3.icon.source
                    width: toolButton3.icon.width
                    height: toolButton3.icon.height
                    anchors.verticalCenter: parent.verticalCenter
                }
                Text{
                    text: toolButton3.text
                    font: toolButton3.font
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
        }
        onClicked:{
            timerView.visible = false;
            historyView.visible = false;
            pomodoroView.visible = true;
            background1.opacity = 0;
            background2.opacity = 0;
            background3.opacity = 0.4;
            background4.opacity = 0;
        }
    }
    ToolButton {
        id: toolButton4
        width: toolBar.width
        icon.source: "../img/svg/about.svg"
        icon.height: 15
        icon.width: 15
        text: qsTr("About")
        font.weight: Font.Light
        x:0
        y:toolButton3.y + toolButton3.height + 4
        Rectangle {
            id: background4
            anchors.fill: parent
            opacity: 0
            color: "grey"
        }
        contentItem: Item{
            Row{
                anchors.fill: parent
                spacing: 10
                Image{
                    source: toolButton4.icon.source
                    width: toolButton4.icon.width
                    height: toolButton4.icon.height
                    anchors.verticalCenter: parent.verticalCenter
                }
                Text{
                    text: toolButton4.text
                    font: toolButton4.font
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
        }
        onClicked:{
            popupAbout.open();
        }
    }
}
