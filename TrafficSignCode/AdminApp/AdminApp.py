# pyuic5 -x SetSpeedLimitDialog.ui -o SetSpeedLimitDialog.py
import sys
import ctypes

from PyQt5.QtWidgets import QApplication, QDialog

from GUI_logic.MainWindow import MainWindow
from GUI_logic.LoginDialog import LoginDialog


if __name__ == "__main__":

    myappid = u"TrafficSignAppCompany.TrafficSignApp"  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)
    login = LoginDialog()
    result = login.exec_()
    if result == QDialog.Accepted:
        apl = MainWindow()
        apl.show()
        sys.exit(app.exec_())
    elif result == QDialog.Rejected:
        print("Rejected")
        sys.exit()
    else:
        print("Something went wrong")
        sys.exit()
