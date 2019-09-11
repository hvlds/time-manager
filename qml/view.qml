import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.13
import QtQuick.Controls.Material 2.12

ApplicationWindow {
    id: applicationWindow
    visible: true
    width: 600
    height: 600
    minimumWidth: 600
    minimumHeight: 300
    title: "Time Manager"

    Row {
        id: row
        x: 0
        y: 0

        SidePanel{
            id: sidePanel
            visible: true
        }

        ColumnLayout {
            id: columnLayout
            width: applicationWindow.width - sidePanel.width
            height: applicationWindow.height

            TimerView {
                id: timerView
                visible: true
                Layout.fillHeight: false
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                transformOrigin: Item.Center
                spacing: 10
            }

            HistoryView {
                id: historyView
                visible: false
                Layout.fillHeight: false
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                transformOrigin: Item.Center
                spacing: 10
            }
        }

    }

}


