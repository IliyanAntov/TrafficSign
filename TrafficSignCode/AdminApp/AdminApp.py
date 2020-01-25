#pyuic5 -x SetSpeedLimitDialog.ui -o SetSpeedLimitDialog.py
import time
import sys
import threading
# from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtCore import pyqtSlot, Qt, QRegExp
from GUI.MainWindow.MainWindow import Ui_MainWindow
from GUI.SetSpeedLimitDialog.SetSpeedLimitDialog import Ui_SetSpeedLimitDialog
from GUI.LoginDialog.LoginDialog import Ui_LoginDialog
from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection
from GUI_logic.MainWindow import MainWindow
from GUI_logic.LoginDialog import LoginDialog
from GUI_logic.SetSpeedLimitDialog import SetSpeedLimitDialog


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginDialog()
    result = login.exec_()
    if(result ==  QDialog.Accepted):
        apl = MainWindow()
        apl.show()
        sys.exit(app.exec_())
    elif(result == QDialog.Rejected):
        print("Rejected")
        sys.exit()
    else:
        print("Something went wrong")
        sys.exit()
