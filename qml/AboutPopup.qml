import QtQuick 2.13
import QtQuick.Controls 2.13
import QtQuick.Controls.Material 2.13
import QtQuick.Layouts 1.13

Popup {   
    modal: true
    focus: true    
    // parent: Overlay.overlay
    // x: Math.round((parent.width - width) / 2)
    // y: Math.round((parent.height - height) / 2)
    anchors.centerIn: Overlay.overlay
    closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent
    Pane {
        Material.elevation: 1
        ColumnLayout {
            Text{
                text:qsTr("About")
                font.weight: Font.DemiBold
                font.pointSize: 17
            }
            Text {
                text: qsTr("Licence: GNU General Public License v3.0")
            }
            Text {
                text:"<a href='http://github.com/hfvaldesg/time-manager'>GitHub repository: hfvaldesg/time-manager</a>"
                onLinkActivated: Qt.openUrlExternally(link)
                MouseArea {
                    anchors.fill: parent
                    acceptedButtons: Qt.NoButton // we don't want to eat clicks on the Text
                    cursorShape: parent.hoveredLink ? Qt.PointingHandCursor : Qt.ArrowCursor
                }
            }
        }        
    }
}