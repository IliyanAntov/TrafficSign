# pyuic5 -x <ui_file>.ui -o <python_file>.py
import sys
import ctypes

from PyQt5.QtWidgets import QApplication, QDialog

from GUI_logic.MainWindow import MainWindow
from GUI_logic.LoginDialog import LoginDialog

# Main method of the application - executes first
if __name__ == "__main__":

    # Create an application information string
    # (Workaround to display the icon in the Windows taskbar)
    applicationInformation = u"TrafficSignAdminApp.TUES"
    # Setup the shell to recognize the application process
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        applicationInformation
    )

    # Create a QApplication() object
    app = QApplication(sys.argv)
    # Create a LoginDialog() object
    login = LoginDialog()
    # Display the login dialog and save the return result
    result = login.exec_()
    # If the login was successful:
    if result == QDialog.Accepted:
        # Create a MainWindow() object
        apl = MainWindow()
        # Display the main application window
        apl.show()
        # Exit the program
        sys.exit(app.exec_())
    # If the login was unsuccessful:
    elif result == QDialog.Rejected:
        # Exit the program
        sys.exit()
    # If something went wrong:
    else:
        print("Something went wrong")
        # Exit the program
        sys.exit()
