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
        anchors.fill: parent

        ToolBar {
            id: toolBar
            width: 100
            height: applicationWindow.height
            Material.elevation: 1
        }

        ColumnLayout {
            id: columnLayout
            width: applicationWindow.width - 100
            height: applicationWindow.height

            Chronometer {
                Layout.alignment: Qt.AlignHCenter
                transformOrigin: Item.Center
                spacing: 10
            }
        }


    }

}
