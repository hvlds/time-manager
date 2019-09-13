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
    model: taskListModel
    delegate: Pane {
        width: parent.width * (2/3)
        anchors.horizontalCenter: parent.horizontalCenter
        Material.elevation: 4
        RowLayout {
            anchors.fill: parent
            Label {
                text: name
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
