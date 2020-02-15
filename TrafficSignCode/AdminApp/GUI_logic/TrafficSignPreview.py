from PyQt5.QtWidgets import QDialog

from PyQt5.QtGui import QIcon, QPixmap

from GUI.TrafficSignPreview.TrafficSignPreview import Ui_TrafficSignPreview


class TrafficSignPreview(QDialog):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.ui = Ui_TrafficSignPreview()
        self.ui.setupUi(self)
        self.SetupFunctionality()

    def SetupFunctionality(self):
        self.setWindowIcon(QIcon("./GUI/images/icon.png"))
        pixmap = QPixmap(self.image)
        self.ui.TrafficSignImage.setPixmap(pixmap)

    def QuitDialog(self):
        self.reject()
