#pyuic5 -x SetSpeedLimitDialog.ui -o SetSpeedLimitDialog.py
import socket
import time
import sys
import select
import struct
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

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.connection = DataExchange()
        self.InitUI()
        self.TryConnect()
        
    def InitUI(self):
        self.ui.passwordTextBox.setEchoMode(QLineEdit.Password) #Mask password input
        self.DisableInput()
        self.ui.connectButton.clicked.connect(self.ConnectClick)  

        #DELETE LATER
        self.ui.usernameTextBox.setText('admin')
        self.ui.passwordTextBox.setText('1234')

    def EnableInput(self):
        self.ui.usernameTextBox.setDisabled(False)
        self.ui.passwordTextBox.setDisabled(False)
        self.ui.connectButton.setDisabled(False)

    def DisableInput(self):
        self.ui.usernameTextBox.setDisabled(True)
        self.ui.passwordTextBox.setDisabled(True)
        self.ui.connectButton.setDisabled(True)
    
    def KeyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.connection.Close()
            self.reject()
        if event.key() == Qt.Key_Enter:
            self.ConnectClick()

    @pyqtSlot()
    def ConnectClick(self):
        username = self.ui.usernameTextBox.text()
        password = self.ui.passwordTextBox.text()
        data = self.connection.AttemptLogin(username, password)
        print(data)
        if (data == 'auth'):
            self.accept()
        elif (data == 'nauth'):
            QMessageBox.warning(self, "Error", "Wrong username or password")
        else:
            print("Too many login attempts")
            QMessageBox.warning(self, "Error", "Too many login attempts", QMessageBox.Ok)
            self.reject()

    def TryConnect(self): #TODO: fix
        if not self.connection.AttemptConnect():
            reply = QMessageBox.question(self, "Error", "Could not connect to the server", QMessageBox.Retry | QMessageBox.Cancel)
            if(reply == QMessageBox.Retry):
                self.TryConnect()
            elif(reply == QMessageBox.Cancel):
                self.reject()
        else:
            self.EnableInput()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.SetupButtons()
        self.connection = DataExchange()
        threading.Thread(target = self.RequestDevices).start()

    def RequestDevices(self):
        while True:
            Connection().SendMessage(Connection().client_socket, str.encode("GetDevices"))
            deviceLen = Connection().ReceiveMessage(Connection().client_socket)
            for i in range (int(deviceLen)):
                print(Connection().ReceiveMessage(Connection().client_socket))
            time.sleep(2)


    def SetupButtons(self):
        self.ui.SetSpeedLimitButton.clicked.connect(self.ShowSetSpeedLimitDialog)

    @pyqtSlot()
    def ShowSetSpeedLimitDialog(self):
        deviceList = self.ui.DeviceList.selectedItems()
        if (len(deviceList) > 0):
            target = deviceList[0].text()
            self.setSpeedLimitDialog = SetSpeedLimitDialog(target)
            self.setSpeedLimitDialog.show()
        else:
            pass
        #self.setSpeedLimitDialog.setupUi(self)

class SetSpeedLimitDialog(QDialog):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self.ui = Ui_SetSpeedLimitDialog()
        self.ui.setupUi(self)
        self.SetupFunctionality()
        self.connection = DataExchange()
    
    def SetupFunctionality(self):
        inputRegEx = QRegExp("[1-9]\d{0,2}")
        validator = QRegExpValidator(inputRegEx)
        self.ui.SpeedLimitTextBox.setValidator(validator)
        self.ui.ConfirmButton.clicked.connect(self.SendSpeedLimit)
        self.ui.CancelButton.clicked.connect(self.QuitDialog)

    def SendSpeedLimit(self):
        speedLimit = self.ui.SpeedLimitTextBox.text()
        Connection().SendMessage(Connection().client_socket, str.encode("Target:" + self.target + " " "SpeedLim:" + speedLimit))
        self.accept()

    def QuitDialog(self):
        self.reject() 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginDialog()
    result = login.exec_()
    if(result ==  QDialog.Accepted):
        print('asd')
        apl = MainWindow()
        apl.show()
        sys.exit(app.exec_())
    elif(result == QDialog.Rejected):
        print("Rejected")
        sys.exit()
    else:
        print("Something went wrong")
        sys.exit()
