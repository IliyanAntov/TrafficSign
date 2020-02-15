from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QIcon, QRegExpValidator, QPixmap
from PyQt5.QtCore import Qt, QRegExp

from GUI.SetWarningDialog.SetWarningDialog import Ui_SetWarningDialog

from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection

# This class is responsible for:
#  - Defining the logic behind the "Set warning" dialog window
#  - Displaying the GUI of the window
#  - Sending a request to the server if requested by the user
class SetWarningDialog(QDialog):

    # Constructor method
    def __init__(self, target):
        super().__init__()
        self.target = target  # Target device IMEI
        # Create a UI object
        self.ui = Ui_SetWarningDialog()
        # Setup and display the default GUI of the window
        self.ui.setupUi(self)
        # Create a DataExchange() object
        self.dataExchange = DataExchange()
        # Setup the custom functionality of this window
        self.SetupFunctionality()

    # Alters the required GUI elements and configures the button actions
    def SetupFunctionality(self):
        # Set the appropriate window icon
        self.setWindowIcon(QIcon("./GUI/images/icon.png"))
        # Set the focus on the cancel button
        self.ui.CancelButton.setFocus()
        # Display the initial preview image
        self.UpdateImage()
        # Connect the buttons to their appropriate methods
        self.ui.SelectionBox.currentTextChanged.connect(self.UpdateImage)
        self.ui.ConfirmButton.clicked.connect(self.SetWarning)
        self.ui.CancelButton.clicked.connect(self.QuitDialog)

    # Updates the image preview to show the currently selected traffic sign
    def UpdateImage(self):
        # Get the currently selected traffic sign name
        self.currentSelection = self.GetCurrentSelection()
        # If the selection is valid:
        if self.currentSelection:
            # Generate a path to the image of the selected traffic sign
            image = "./GUI/images/" + self.currentSelection + ".png"
            # Create a QPixmap() object with the image
            pixmap = QPixmap(image)
            # Display the image
            self.ui.ImageLabel.setPixmap(pixmap)

    # Returns the currently selected list item
    def GetCurrentSelection(self):
        # Get the currently selected item value
        selection = str(self.ui.SelectionBox.currentText())
        try:
            # Remove the spaces from the selected string
            # (Create a file-name-appropriate value)
            selection = selection.replace(" ", "")
            return selection
        except:
            return None

    # Sends a request to the web server with the warning sign selected by the user
    def SetWarning(self):
        # Call the SetWarning() method and save the response
        response = self.dataExchange.SetWarning(
            Connection().knownDevices[self.target], self.currentSelection
        )
        # Handle the received response
        result = self.HandleResponse(response)
        # If the response was valid:
        if result != None:
            # Return the QDialog.Accepted value and close the dialog window
            self.accept()
        # If the response was not valid:
        else:
            # Return the QDialog.Rejected value and close the dialog window
            self.reject()

    # Handles the response returned by the web server when calling the SetWarning() method
    def HandleResponse(self, response):
        # If there is a problem with the server connection:
        if response == "nocon" or response == "timeout":
            return None  # Response not valid
        # If there is a problem with the device connection:
        elif response == "nosend":
            # Display a warning message
            QMessageBox.warning(
                self, "Error", "Couldn't send message to device", QMessageBox.Ok
            )
            return False  # Response valid
        elif response == "notfound":
            # Display a warning message
            QMessageBox.warning(
                self, "Error", "Requested device not found", QMessageBox.Ok
            )
            return False  # Response valid
        elif response == "noresp":
            # Display a warning message
            QMessageBox.warning(self, "Error", "Device didn't respond", QMessageBox.Ok)
            return False  # Response valid
        elif response == "success":
            # Display a warning message
            QMessageBox.information(
                self, "Success", "Successfully sent request to device", QMessageBox.Ok
            )
            return True  # Response valid

    # Handles key press shortcuts
    def keyPressEvent(self, event):
        # If [ESC] is clicked -> close the window
        if event.key() == Qt.Key_Escape:
            # Close the dialog
            self.QuitDialog()

    # Handles the event that occurs when the dialog is closed
    def closeEvent(self, event):
        # Close the dialog
        self.QuitDialog()

    # Quits the dialog
    def QuitDialog(self):
        # Return the QDialog.Accepted value and close the dialog window
        self.accept()
