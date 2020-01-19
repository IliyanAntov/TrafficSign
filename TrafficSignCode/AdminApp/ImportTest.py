#pyuic5 -x MainPage.ui -o GUITemp.py
#
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from GUITemp import Ui_MainWindow

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

ui.DetailsButton.setText("zdasti")

window.show()
sys.exit(app.exec_())