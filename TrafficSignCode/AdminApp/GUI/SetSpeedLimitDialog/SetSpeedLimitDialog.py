# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetSpeedLimitDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetSpeedLimitDialog(object):
    def setupUi(self, SetSpeedLimitDialog):
        SetSpeedLimitDialog.setObjectName("SetSpeedLimitDialog")
        SetSpeedLimitDialog.resize(262, 128)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SetSpeedLimitDialog.sizePolicy().hasHeightForWidth())
        SetSpeedLimitDialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        SetSpeedLimitDialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(SetSpeedLimitDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SpeedLimitLabel = QtWidgets.QLabel(SetSpeedLimitDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SpeedLimitLabel.setFont(font)
        self.SpeedLimitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SpeedLimitLabel.setObjectName("SpeedLimitLabel")
        self.horizontalLayout_3.addWidget(self.SpeedLimitLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SpeedLimitTextBox = QtWidgets.QLineEdit(SetSpeedLimitDialog)
        self.SpeedLimitTextBox.setObjectName("SpeedLimitTextBox")
        self.horizontalLayout_2.addWidget(self.SpeedLimitTextBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ConfirmButton = QtWidgets.QPushButton(SetSpeedLimitDialog)
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.horizontalLayout.addWidget(self.ConfirmButton)
        self.CancelButton = QtWidgets.QPushButton(SetSpeedLimitDialog)
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SetSpeedLimitDialog)
        QtCore.QMetaObject.connectSlotsByName(SetSpeedLimitDialog)

    def retranslateUi(self, SetSpeedLimitDialog):
        _translate = QtCore.QCoreApplication.translate
        SetSpeedLimitDialog.setWindowTitle(_translate("SetSpeedLimitDialog", "Set speed limit"))
        self.SpeedLimitLabel.setText(_translate("SetSpeedLimitDialog", "Set speed limit:"))
        self.ConfirmButton.setText(_translate("SetSpeedLimitDialog", "Confirm"))
        self.CancelButton.setText(_translate("SetSpeedLimitDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SetSpeedLimitDialog = QtWidgets.QWidget()
    ui = Ui_SetSpeedLimitDialog()
    ui.setupUi(SetSpeedLimitDialog)
    SetSpeedLimitDialog.show()
    sys.exit(app.exec_())
