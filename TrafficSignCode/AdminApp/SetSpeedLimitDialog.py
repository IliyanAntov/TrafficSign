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
        SetSpeedLimitDialog.resize(204, 114)
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
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SpeedLimitLabel = QtWidgets.QLabel(SetSpeedLimitDialog)
        self.SpeedLimitLabel.setObjectName("SpeedLimitLabel")
        self.verticalLayout.addWidget(self.SpeedLimitLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SpeedLimitTextBox = QtWidgets.QLineEdit(SetSpeedLimitDialog)
        self.SpeedLimitTextBox.setObjectName("SpeedLimitTextBox")
        self.horizontalLayout_2.addWidget(self.SpeedLimitTextBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
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
