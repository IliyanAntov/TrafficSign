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



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.SetupButtons()
        self.connection = Connection()
        threading.Thread(target = self.RequestDevices).start()

    def RequestDevices(self):
        while True:
            self.connection.SendMessage(str.encode("GetDevices"))
            deviceLen = self.connection.ReceiveMessage()
            for i in range (int(deviceLen)):
                print(self.connection.ReceiveMessage())
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

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.connection = Connection()
        self.InitUI()
        self.TryConnect()
        
    def InitUI(self):
        self.setWindowIcon(QIcon('./images/icon.png'))
        self.ui.passwordTextBox.setEchoMode(QLineEdit.Password) #Mask password input
        self.DisableInput()
        self.ui.connectButton.clicked.connect(self.AttemptConnect)  


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
            self.AttemptConnect()

    @pyqtSlot()
    def AttemptConnect(self):
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

class SetSpeedLimitDialog(QDialog):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self.ui = Ui_SetSpeedLimitDialog()
        self.ui.setupUi(self)
        self.SetupFunctionality()
        self.connection = Connection()
    
    def SetupFunctionality(self):
        inputRegEx = QRegExp("[1-9]\d{0,2}")
        validator = QRegExpValidator(inputRegEx)
        self.ui.SpeedLimitTextBox.setValidator(validator)
        self.ui.ConfirmButton.clicked.connect(self.SendSpeedLimit)
        self.ui.CancelButton.clicked.connect(self.QuitDialog)

    def SendSpeedLimit(self):
        speedLimit = self.ui.SpeedLimitTextBox.text()
        self.connection.SendMessage(str.encode("Target:" + self.target + " " "SpeedLim:" + speedLimit))
        self.accept()

    def QuitDialog(self):
        self.reject()

class Connection():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        super().__init__()
    
    def AttemptConnect(self):
        try:
            # self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            Connection.client_socket.connect(("localhost", 8220))
            print("Connection successful")
            return True
        except:
            print("Connection to server unsuccessful")
            return False

    def AttemptLogin(self, username, password):
        print("Attempting to log in...")
        try:
            self.SendMessage(str.encode(username))
        except:
            return None
        try:
            self.SendMessage(str.encode(password))
        except:
            return None
        data = self.WaitForData()
        if not data:
            self.Close()
        else:
            return data   

    def WaitForData(self):
        ready = select.select([Connection.client_socket], [], [], 2)
        if ready[0]:
            data = self.ReceiveMessage().decode('utf-8')
            return data
        else:
            print("Connection timeout")
            return None

    def SendMessage(self, data):
        length = len(data)
        Connection.client_socket.sendall(struct.pack('!I', length))
        Connection.client_socket.sendall(data)

    def ReceiveMessage(self):
        lengthbuf = self.ReceiveAll(4)
        length, = struct.unpack('!I', lengthbuf)
        return self.ReceiveAll(length)

    def ReceiveAll(self, count):
        buf = b''
        while count:
            newbuf = Connection.client_socket.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def Close(self):
        print("Closing connection...")
        Connection.client_socket.close()
  

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
    #sys.exit(app.exec_())


# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(("localhost", 8220))

# print("Waiting for input...")
# userMsg = input()

# while (userMsg != "end"):
#     client_socket.send(str.encode(userMsg))
#     userMsg = input()
                                                                                                                        
# print ("Disconnecting")
# client_socket.send(b'disconnect')

# client_socket.close()