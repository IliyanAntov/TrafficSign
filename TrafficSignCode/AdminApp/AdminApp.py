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
        self.width = 200
        self.height = 400
        self.font = ("Arial", 14)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateLabel(10, 10, "Username:") #Create username label

        self.usernameTextBox = self.CreateTextBox(10, 35, 150, 40) #Create username textbox

        self.CreateLabel(10, 85, "Password:") #Create username label

        self.passwordTextBox = self.CreateTextBox(10, 110, 150, 40) #Create username textbox
        self.passwordTextBox.setEchoMode(QLineEdit.Password)

        self.CreateButton(20, 160, 100, 40, "Connect", self.connection_attempt_click) #Create login button

        self.show()


    def CreateLabel(self, x, y, text):
        label = QLabel(self)
        label.setFont(QFont(*self.font))
        label.setText(text)
        label.move(x, y)
    
    def CreateTextBox(self, x, y, width, height):
        textbox = QLineEdit(self)
        textbox.setFont(QFont(*self.font))
        textbox.move(x, y)
        textbox.resize(width, height)
        return textbox

    def CreateButton(self, x, y, width, height, text, func):
        button = QPushButton(text, self)
        button.resize(width, height)
        button.setFont(QFont(*self.font))
        button.move(x, y)
        button.clicked.connect(func)



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