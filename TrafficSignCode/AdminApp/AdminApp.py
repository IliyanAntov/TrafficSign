import socket
import time
import sys
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

        self.connectButton = self.CreateButton(20, 160, 100, 100, "Connect", self.connection_attempt_click) #Create login button


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


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    @pyqtSlot()
    def connection_attempt_click(self):
        username = self.usernameTextBox.text()
        password = self.passwordTextBox.text()
        print(username)
        print(password)

    def on_click(self):
        print('Connection attempt')

class Connection():
    def __init__(self):
        super().__init__()
    

    def AttemptConnect(self):
        print("Connecting...")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
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