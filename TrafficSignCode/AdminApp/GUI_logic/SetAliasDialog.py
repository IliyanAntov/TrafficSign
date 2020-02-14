from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtCore import Qt, QRegExp

from GUI.SetAliasDialog.SetAliasDialog import Ui_SetAliasDialog

from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection

class SetAliasDialog(QDialog):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self.ui = Ui_SetAliasDialog()
        self.ui.setupUi(self)
        self.connection = DataExchange()
        self.SetupFunctionality()
    
    def SetupFunctionality(self):
        self.setWindowIcon(QIcon('./GUI/images/icon.png'))
        self.ui.CurrentNameTextBox.setText(self.target)
        self.ui.NewNameTextBox.setFocus()
        inputRegEx = QRegExp("\S.*")
        validator = QRegExpValidator(inputRegEx)
        self.ui.NewNameTextBox.setValidator(validator)
        self.ui.ConfirmButton.clicked.connect(self.SetAlias)
        self.ui.CancelButton.clicked.connect(self.QuitDialog)
 
    def SetAlias(self):
        newName = self.ui.NewNameTextBox.text()
        if(newName != ""):
            IMEI = Connection().knownDevices.pop(self.target)
            Connection().knownDevices[newName] = IMEI
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Please enter device alias", QMessageBox.Ok)

    def QuitDialog(self):
        self.reject() 
