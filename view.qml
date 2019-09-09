import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12

ApplicationWindow {
    visible: true
    minimumWidth: 600
    minimumHeight: 600
    Column {
        anchors.centerIn: parent
        RadioButton { text: qsTr("Small") }
        RadioButton { text: qsTr("Medium");  checked: true }
        RadioButton { text: qsTr("Large") }
		Button {
		    text: qsTr("Button")
		    highlighted: true
		    Material.background: Material.Red
		}
	    Pane {
		    width: 120
	    	height: 120
	    	Material.elevation: 6	
		    Label {
	    	    text: qsTr("I'm a card!")
	        	anchors.centerIn: parent
	    	}
		}
	}
}
