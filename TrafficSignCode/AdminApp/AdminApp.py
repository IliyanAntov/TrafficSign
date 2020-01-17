import socket
import time
import sys
import select
import struct
# from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot, Qt


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Login'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.defaultFont = ("Arial", 14)
        self.connection = Connection()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('./images/icon.png'))

        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.show()






class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Login'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.defaultFont = ("Arial", 14)
        self.connection = Connection()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('./images/icon.png'))

        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.usernameLabel = self.CreateLabel(10, 10, "Username:") #Create username label

        self.usernameTextBox = self.CreateTextBox(10, 35, 150, 40) #Create username textbox

        self.passwordLabel = self.CreateLabel(10, 85, "Password:") #Create password label

        self.passwordTextBox = self.CreateTextBox(10, 110, 150, 40) #Create password textbox
        self.passwordTextBox.setEchoMode(QLineEdit.Password) #Mask password input

        self.connectButton = self.CreateButton(20, 160, 100, 100, "Connect", self.ConnectionAttemptClick) #Create login button


        self.OrderLoginLayout()

        self.show()

    def OrderLoginLayout(self):
        windowVBox = QVBoxLayout()
        windowVBox.addStretch(1)

        # Username label and input box
        usernameHBox = QHBoxLayout()

        usernameHBox.addStretch(1)
        usernameHBox.addWidget(self.usernameLabel)
        usernameHBox.addStretch(1)

        windowVBox.addLayout(usernameHBox)

        usernameInputHBox = QHBoxLayout()

        usernameInputHBox.addStretch(1)
        self.usernameTextBox.setFixedHeight(40)
        usernameInputHBox.addWidget(self.usernameTextBox, 2)
        usernameInputHBox.addStretch(1)

        windowVBox.addLayout(usernameInputHBox)

        # Password label and input box
        passwordHBox = QHBoxLayout()

        passwordHBox.addStretch(1)
        passwordHBox.addWidget(self.passwordLabel)
        passwordHBox.addStretch(1)

        windowVBox.addLayout(passwordHBox)

        passwordInputHBox = QHBoxLayout()

        passwordInputHBox.addStretch(1)
        self.passwordTextBox.setFixedHeight(40)
        passwordInputHBox.addWidget(self.passwordTextBox, 2)
        passwordInputHBox.addStretch(1)

        windowVBox.addLayout(passwordInputHBox)

        # Connect button
        connectButtonHBox = QHBoxLayout()

        connectButtonHBox.addStretch(1)
        self.connectButton.setFixedHeight(40)
        connectButtonHBox.addWidget(self.connectButton, 2)
        connectButtonHBox.addStretch(1)

        windowVBox.addStretch(1)
        windowVBox.addLayout(connectButtonHBox, 2)
        self.setLayout(windowVBox)

    def CreateLabel(self, x, y, text):
        label = QLabel(self)
        label.setFont(QFont(*self.defaultFont))
        label.setText(text)
        label.move(x, y)
        return label
    
    def CreateTextBox(self, x, y, width, height):
        textbox = QLineEdit(self)
        textbox.setFont(QFont(*self.defaultFont))
        textbox.move(x, y)
        textbox.resize(width, height)
        return textbox

    def CreateButton(self, x, y, width, height, text, func):
        button = QPushButton(text, self)
        button.resize(width, height)
        button.setFont(QFont(*self.defaultFont))
        button.move(x, y)
        button.clicked.connect(func)
        return button

    def LaunchControlApp(self):
        appl = GUI(self)
        appl.show()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.connection.Close()
            self.close()
        if event.key() == Qt.Key_Enter:
            self.ConnectionAttemptClick()

    @pyqtSlot()
    def ConnectionAttemptClick(self):
        username = self.usernameTextBox.text()
        password = self.passwordTextBox.text()
        if(self.connection.AttemptConnect()):
            data = self.connection.AttemptLogin(username, password)
            print(data)
            if (data == 'auth'):
                self.accept()
            elif (data == 'nauth'):
                QMessageBox.warning(self, "Error", "Wrong username or password")
            else:
                print("Error")


class Connection():
    def __init__(self):
        super().__init__()
    
    def AttemptConnect(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(("localhost", 8220))
            print("Connection successful")
            return True
        except:
            print("Connection to server unsuccessful")
            return False

    def AttemptLogin(self, username, password):
        print("Attempting to log in...")
        self.SendMessage(str.encode(username))
        self.SendMessage(str.encode(password))
        data = self.WaitForData()
        if not data:
            self.Close()
        else:
            return data   

    def WaitForData(self):
        ready = select.select([self.client_socket], [], [], 2)
        if ready[0]:
            data = self.ReceiveMessage().decode('utf-8')
            return data
        else:
            print("Connection timeout")
            return None


    def SendMessage(self, data):
        length = len(data)
        self.client_socket.sendall(struct.pack('!I', length))
        self.client_socket.sendall(data)

    def ReceiveMessage(self):
        lengthbuf = self.ReceiveAll(4)
        length, = struct.unpack('!I', lengthbuf)
        return self.ReceiveAll(length)

    def ReceiveAll(self, count):
        buf = b''
        while count:
            newbuf = self.client_socket.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf






    def Close(self):
        print("Closing connection...")
        self.client_socket.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginWindow()
    if(login.exec_() ==  QDialog.Accepted):
        gui = GUI()
        gui.show()
    sys.exit(app.exec_())


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