from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtCore import Qt, QRegExp

from GUI.SetSpeedLimitDialog.SetSpeedLimitDialog import Ui_SetSpeedLimitDialog
from GUI_logic.TrafficSignPreview import TrafficSignPreview

from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection

# This class is responsible for:
#  - Defining the logic behind the "Set speed limit" dialog window
#  - Displaying the GUI of the window
#  - Sending a request to the server if requested by the user
class SetSpeedLimitDialog(QDialog):

    # Constructor method
    def __init__(self, target):
        super().__init__()
        self.target = target  # Target device IMEI
        # Create a UI object
        self.ui = Ui_SetSpeedLimitDialog()
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
        # Create a regular expression to prevent invalid data entry
        inputRegEx = QRegExp(
            "[1-9]\d{0,2}"  # Max 3 symbols
            # First symbol - digit between 1 and 9
            # Second/third symbol - any whole digit
        )
        #  Create a validator object
        validator = QRegExpValidator(inputRegEx)
        # Attach the validator to the input textbox
        self.ui.SpeedLimitTextBox.setValidator(validator)
        # Connect the buttons to their appropriate methods
        self.ui.ConfirmButton.clicked.connect(self.SetSpeedLimit)
        self.ui.CancelButton.clicked.connect(self.QuitDialog)
        self.ui.PreviewButton.clicked.connect(self.DisplayPreview)

    # Sends a request to the web server with the speed limit entered by the user
    def SetSpeedLimit(self):
        # Get the speed limit value entered by the user
        speedLimit = self.ui.SpeedLimitTextBox.text()
        # If a name is not entered:
        if speedLimit == "":
            # Display a warning message
            QMessageBox.warning(
                self, "Error", "Please input speed limit", QMessageBox.Ok
            )
        # If a name is entered:
        else:
            # Call the SetSpeedLimit() method and save the response
            response = self.dataExchange.SetSpeedLimit(
                Connection().knownDevices[self.target], speedLimit
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

    # Handles the response returned by the web server when calling the SetSpeedLimit() method
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

    # Displays the "Traffic sign preview" dialog window for speed limit signs
    def DisplayPreview(self):
        # Create a TrafficSignPreview() object
        self.previewDialog = TrafficSignPreview("./GUI/images/SpeedLimit.png")
        # Display the dialog
        self.previewDialog.exec_()

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
