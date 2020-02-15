from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon
from GUI.DetailsDialog.DetailsDialog import Ui_DetailsDialog

# This class is responsible for:
#  - Defining the logic behind the "Device details" dialog window
#  - Displaying the GUI of the window
class DetailsDialog(QDialog):

    # Constructor method
    def __init__(self, alias, IMEI, status, value):
        super().__init__()
        self.alias = alias  # The device's alias
        self.IMEI = IMEI  # The device's IMEI
        self.status = status  # The device's current display status
        self.value = value  # The device's current speed limit/warning value
        # Create a UI object
        self.ui = Ui_DetailsDialog()
        # Setup and display the default GUI of the window
        self.ui.setupUi(self)
        # Setup the custom functionality of this window
        self.SetupFunctionality()

    # Alters the required GUI elements and configures the button actions
    def SetupFunctionality(self):
        # Set the appropriate window icon
        self.setWindowIcon(QIcon("./GUI/images/icon.png"))
        # Set the label values to the ones of the current device
        self.ui.CurrentAliasLabel.setText(self.alias)
        self.ui.IMEILabel.setText(self.IMEI)
        self.ui.StatusLabel.setText(self.status)
        self.ui.ValueLabel.setText(self.value)
        # Connect the button to the appropriate method
        self.ui.CloseButton.clicked.connect(self.QuitDialog)

    # Closes the dialog
    def QuitDialog(self):
        # Return the QDialog.Accepted value and close the dialog window
        self.accept()
