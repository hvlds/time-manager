import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12
import QtQuick.Layouts 1.13

ListView {
    id: myListView
    width: parent.width
    height: parent.height
    focus: true
    Layout.topMargin: 20
    Layout.bottomMargin: 20
    model: taskListModel

    ScrollBar.vertical: ScrollBar {
        active: true
    }
    delegate: Pane {
        //width: parent.width * (2/3)
        anchors.horizontalCenter: parent.horizontalCenter
        Material.elevation: 4
        Layout.fillWidth: true
        RowLayout {
            anchors.fill: parent
            Column {
                Layout.rightMargin: 20
                spacing: 2
                Label {
                    text: description
                    font.weight: Font.Bold
                    wrapMode: Text.WordWrap
                    width: parent.width
                }
                Label {
                    text: "duration: " + duration;
                }
                Label {
                    text: "start: " + date_start;
                }
                Label {
                    text: "end: " + date_stop;
                }
            }

            Row {
                Layout.alignment:Qt.AlignRight;
                spacing:5
                Button {
                    //icon.color: "green"
                    icon.source: "../img/svg/edit.svg"
                    Material.background: Material.Green
                    onClicked: {
                        console.log(id);
                    }
                }
                Button {
                    //icon.color:"red"
                    icon.source: "../img/svg/delete.svg"
                    Material.background: Material.Red
                    onClicked: {
                        taskListModel.removeRow(id);
                    }
                }
            }
        }
    }
}
