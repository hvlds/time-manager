import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.13
import QtQuick.Controls.Material 2.12

ApplicationWindow {
    id: applicationWindow
    visible: true
    width: 600
    height: 600
    title: "Time Manager"

    Row {
        id: row
        x: 0
        y: 0

        ToolBar {
            id: toolBar
            width: 120
            height: applicationWindow.height
            Material.elevation: 1
            Material.background: Material.Grey

            ToolButton {
                id: toolButton1
                width: toolBar.width
                icon.source: "./img/icons/svg/new.svg"
                text: qsTr("new Task")
                x:0
                y:10
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
            }

            ToolButton {
                id: toolButton2
                width: toolBar.width
                icon.source: "./img/icons/svg/history.svg"
                text: qsTr("History")
                x:0
                y:toolButton1.y + toolButton1.height + 4
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
        }

        ColumnLayout {
            id: columnLayout
            width: applicationWindow.width - toolBar.width
            height: applicationWindow.height

            Chronometer {
                visible: true
                Layout.fillHeight: false
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                transformOrigin: Item.Center
                spacing: 10
            }
        }


    }

}


