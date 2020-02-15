from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon
from GUI.DetailsDialog.DetailsDialog import Ui_DetailsDialog


class DetailsDialog(QDialog):
    def __init__(self, alias, IMEI, status, value):
        super().__init__()
        self.alias = alias
        self.IMEI = IMEI
        self.status = status
        self.value = value
        self.ui = Ui_DetailsDialog()
        self.ui.setupUi(self)
        self.SetupFunctionality()

    def SetupFunctionality(self):
        self.setWindowIcon(QIcon("./GUI/images/icon.png"))
        self.ui.CurrentAliasLabel.setText(self.alias)
        self.ui.IMEILabel.setText(self.IMEI)
        self.ui.StatusLabel.setText(self.status)
        self.ui.ValueLabel.setText(self.value)
        self.ui.CloseButton.clicked.connect(self.QuitDialog)

    def QuitDialog(self):
        self.reject()
