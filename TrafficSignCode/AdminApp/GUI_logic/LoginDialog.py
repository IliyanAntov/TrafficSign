from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from GUI.LoginDialog.LoginDialog import Ui_LoginDialog
from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection

# This class is responsible for:
#  - Defining the logic behind the "Login" dialog window
#  - Displaying the GUI of the window
#  - Sending the appropriate requests to the web servers via the DataExchange() class
class LoginDialog(QDialog):

    # Constructor method
    def __init__(self):
        super().__init__()
        # Create a UI object
        self.ui = Ui_LoginDialog()
        # Setup and display the default GUI of the window
        self.ui.setupUi(self)
        # Create a DataExchange() object
        self.dataExchange = DataExchange()
        # Setup the custom functionality of this window
        self.SetupFunctionality()
        self.connected = False  # Current connection status

    # Alters the required GUI elements
    def SetupFunctionality(self):
        # Mask password input
        self.ui.passwordTextBox.setEchoMode(QLineEdit.Password)
        # Disable the username and password input
        self.DisableInput()
        # Connect the button to the appropriate method
        self.ui.connectButton.clicked.connect(self.ConnectClick)
        # Set the appropriate window icon
        self.setWindowIcon(QIcon("./GUI/images/icon.png"))

        # DELETE LATER
        self.ui.usernameTextBox.setText("admin")
        self.ui.passwordTextBox.setText("1234")

    # Enables the username and password input
    def EnableInput(self):
        # Enable the text boxes
        self.ui.usernameTextBox.setDisabled(False)
        self.ui.passwordTextBox.setDisabled(False)

    # Disables the username and password input
    def DisableInput(self):
        # Disable the text boxes
        self.ui.usernameTextBox.setDisabled(True)
        self.ui.passwordTextBox.setDisabled(True)

    # Handles key press shortcuts
    def keyPressEvent(self, event):
        # If [ESC] is clicked -> close the window
        if event.key() == Qt.Key_Escape:
            try:
                # Close the connection, if available
                Connection().Close()
            except:
                pass
            # Return the QDialog.Rejected value and close the dialog window
            self.reject()
        # If [ENTER] is clicked -> attempt to connect
        if event.key() == Qt.Key_Enter:
            # Try to connect/login to the server
            self.ConnectClick()

    # Tries to establish a connection to the web server
    def TryConnect(self):
        # Attempt to connect to the web server
        #
        # If the connection is unsuccessful:
        if not self.dataExchange.AttemptConnect():
            # Display an error message box
            reply = QMessageBox.critical(
                self,
                "Error",
                "Could not connect to the server",
                QMessageBox.Retry | QMessageBox.Cancel,
            )
            # Retry the connection if the retry button is clicked
            if reply == QMessageBox.Retry:
                return self.TryConnect()
            # Close the message box if the cancel button is clicked
            elif reply == QMessageBox.Cancel:
                return False

        # If the connection is successful:
        else:
            # Enable the username and password input
            self.EnableInput()
            # Change the connect button text
            self.ui.connectButton.setText("Login")
            return True

    # Attempts to connect to the web server if a connection is not established
    # Sends the entered login information if a connection is established
    def ConnectClick(self):
        # Not connected:
        if not self.connected:
            self.connected = self.TryConnect()
        # Connected:
        else:
            username = self.ui.usernameTextBox.text()  # Entered username
            password = self.ui.passwordTextBox.text()  # Entered password
            # Try to login with the given credentials
            data = self.dataExchange.AttemptLogin(username, password)

            # If the server accepted the login information:
            if data == "auth":
                # Return the QDialog.Accepted value and close the dialog window
                self.accept()

            # If the server did not accept the login information:
            elif data == "nauth":
                # Display a warning message box
                QMessageBox.warning(self, "Error", "Wrong username or password")

            # If the server refused the connection because of too many login attempts:
            elif data == "refuse":
                print("Too many login attempts")
                # Display an error message box
                QMessageBox.critical(
                    self, "Error", "Too many login attempts", QMessageBox.Ok
                )
                # Return the QDialog.Rejected value and close the dialog window
                self.reject()

            # If something went horribly wrong:
            else:
                # Display an error message box
                QMessageBox.critical(
                    self, "Error", "Something went wrong", QMessageBox.Ok
                )
                # Return the QDialog.Rejected value and close the dialog window
                self.reject()

