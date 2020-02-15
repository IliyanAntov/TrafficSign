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
        # Alter the GUI as needed
        self.AlterGUI()
        self.connected = False  # Current connection status

    # Alters the required GUI elements
    def AlterGUI(self):
        # Mask password input
        self.ui.passwordTextBox.setEchoMode(QLineEdit.Password)
        # Disable the username and password input
        self.DisableInput()
        # Connect the connect button to the ConnectClick() method
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
        # Attempt to connect
        if not self.dataExchange.AttemptConnect():
            # Display an error if the connection was unsuccessful
            reply = QMessageBox.critical(
                self,
                "Error",
                "Could not connect to the server",
                QMessageBox.Retry | QMessageBox.Cancel,
            )
            if reply == QMessageBox.Retry:
                return self.TryConnect()
            elif reply == QMessageBox.Cancel:
                return False
        else:
            self.EnableInput()
            self.ui.connectButton.setText("Login")
            return True

    def ConnectClick(self):
        if not self.connected:
            self.connected = self.TryConnect()
        else:
            username = self.ui.usernameTextBox.text()
            password = self.ui.passwordTextBox.text()
            data = self.dataExchange.AttemptLogin(username, password)
            print(data)
            if data == "auth":
                self.accept()
            elif data == "nauth":
                QMessageBox.warning(self, "Error", "Wrong username or password")
            elif data == "refuse":
                print("Too many login attempts")
                QMessageBox.warning(
                    self, "Error", "Too many login attempts", QMessageBox.Ok
                )
                self.reject()
            else:
                QMessageBox.warning(
                    self, "Error", "Something went wrong", QMessageBox.Ok
                )
                self.reject()

