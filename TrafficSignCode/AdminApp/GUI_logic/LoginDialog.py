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
