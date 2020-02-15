from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtCore import Qt, QRegExp

from GUI.SetAliasDialog.SetAliasDialog import Ui_SetAliasDialog

from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection

# This class is responsible for:
#  - Defining the logic behind the "Set alias" dialog window
#  - Displaying the GUI of the window
#  - Updating the device alias if requested by the user
class SetAliasDialog(QDialog):

    # Constructor method
    def __init__(self, target):
        super().__init__()
        self.target = target  # Target device current alias
        # Create a UI object
        self.ui = Ui_SetAliasDialog()
        # Setup and display the default GUI of the window
        self.ui.setupUi(self)
        # Setup the custom functionality of this window
        self.SetupFunctionality()

    # Alters the required GUI elements and configures the button actions
    def SetupFunctionality(self):
        # Set the appropriate window icon
        self.setWindowIcon(QIcon("./GUI/images/icon.png"))
        # Display the current device alias
        self.ui.CurrentNameTextBox.setText(self.target)
        # Set the focus on the input textbox
        self.ui.NewNameTextBox.setFocus()
        # Create a regular expression to prevent invalid data entry
        inputRegEx = QRegExp(
            "\S.*"  # First symbol not whitespace, any length, any character
        )
        # Create a validator object
        validator = QRegExpValidator(inputRegEx)
        # Attach the validator to the input textbox
        self.ui.NewNameTextBox.setValidator(validator)
        # Connect the buttons to their appropriate methods
        self.ui.ConfirmButton.clicked.connect(self.SetAlias)
        self.ui.CancelButton.clicked.connect(self.QuitDialog)

    # Updates the selected device alias
    def SetAlias(self):
        # Get the new name entered by the user
        newName = self.ui.NewNameTextBox.text()
        # If a name is entered:
        if newName != "":
            # If the alias already exists:
            if newName in Connection().knownDevices.keys():
                # Display a warning message
                QMessageBox.warning(
                    self,
                    "Error",
                    "Alias already exists, please enter a unique device alias",
                    QMessageBox.Ok,
                )
            # If the alias does not exist:
            else:
                # Get the device IMEI and remove the current alias from the dictionary
                IMEI = Connection().knownDevices.pop(self.target)
                # Add the new alias to the dictionary
                Connection().knownDevices[newName] = IMEI
                # Return the QDialog.Accepted value and close the dialog window
                self.accept()
        # If a name is not entered:
        else:
            # Display a warning message
            QMessageBox.warning(
                self, "Error", "Please enter device alias", QMessageBox.Ok
            )

    # Closes the dialog
    def QuitDialog(self):
        # Return the QDialog.Rejected value and close the dialog window
        self.reject()
