import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.13
import QtQuick.Controls.Material 2.12

ToolBar {
    id: toolBar
    width: 130
    height: applicationWindow.height
    Material.elevation: 1
    Material.background: Material.Lime

    ToolButton {
        id: toolButton1
        width: toolBar.width
        icon.source: "../img/svg/new.svg"
        text: qsTr("new Task")
        x:0
        y:10
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
            chronometerView.visible = true;
            background1.opacity = 0.4;
            background2.opacity = 0;
            background3.opacity = 0;
        }
    }
    ToolButton {
        id: toolButton2
        width: toolBar.width
        icon.source: "../img/svg/history.svg"
        text: qsTr("History")
        x:0
        y:toolButton1.y + toolButton1.height + 4
        Rectangle
        {
            id: background2
            anchors.fill: parent
            opacity: 0
            color: "grey"
        }
        onClicked:{
            chronometerView.visible = false;
            background1.opacity = 0;
            background2.opacity = 0.4;
            background3.opacity = 0;
        }
        contentItem: Item{
            Row{
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
        text: qsTr("Pomodoro")
        x:0
        y:toolButton2.y + toolButton2.height + 4
        Rectangle
        {
            id: background3
            anchors.fill: parent
            opacity: 0
            color: "grey"
        }
        contentItem: Item{
            Row{
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
            chronometerView.visible = false;
            background1.opacity = 0;
            background2.opacity = 0;
            background3.opacity = 0.4;
        }
    }
}