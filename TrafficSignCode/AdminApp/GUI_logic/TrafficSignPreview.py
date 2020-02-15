from PyQt5.QtWidgets import QDialog

from PyQt5.QtGui import QIcon, QPixmap

from GUI.TrafficSignPreview.TrafficSignPreview import Ui_TrafficSignPreview

# This class is responsible for:
#  - Defining the logic behind the "Traffic sign preview" dialog window
#  - Displaying the GUI of the window
class TrafficSignPreview(QDialog):

    # Constructor method
    def __init__(self, image):
        super().__init__()
        self.image = image  # Image to be displayed
        # Create a UI object
        self.ui = Ui_TrafficSignPreview()
        # Setup and display the default GUI of the window
        self.ui.setupUi(self)
        # Setup the custom functionality of this window
        self.SetupFunctionality()

    # Alters the required GUI elements and configures the button actions
    def SetupFunctionality(self):
        # Set the appropriate window icon
        self.setWindowIcon(QIcon("./GUI/images/icon.png"))
        # Create a QPixmap() object with the image
        pixmap = QPixmap(self.image)
        # Display the image
        self.ui.TrafficSignImage.setPixmap(pixmap)

    # Quits the dialog
    def QuitDialog(self):
        # Return the QDialog.Accepted value and close the dialog window
        self.accept()
