import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12

ListView {
    width: parent.width
    height: parent.height
    focus: true
    model: ListModel {
    id: listModel
        Component.onCompleted: {
            var tasks = history.get_tasks()
            for (var index in tasks) {
                var taskObj = {
                    "description": tasks[index]["description"],
                    "id": index
                };
                append(taskObj);
            }
        }
    }
    delegate: Rectangle {
        width: parent.width
        height: 20
        color: "transparent"
        Text {
            text: description
        }
    }
}
