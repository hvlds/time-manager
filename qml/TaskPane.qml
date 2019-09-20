import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12
import QtQuick.Layouts 1.13

Pane {
    //width: parent.width * (2/3)
    anchors.horizontalCenter: parent.horizontalCenter
    Material.elevation: 3
    Layout.fillWidth: true
    z: -1
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