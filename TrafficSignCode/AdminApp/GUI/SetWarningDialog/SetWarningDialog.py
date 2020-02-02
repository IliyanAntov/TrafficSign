# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetWarningDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetWarningDialog(object):
    def setupUi(self, SetWarningDialog):
        SetWarningDialog.setObjectName("SetWarningDialog")
        SetWarningDialog.resize(560, 340)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SetWarningDialog.sizePolicy().hasHeightForWidth())
        SetWarningDialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        SetWarningDialog.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SetWarningDialog)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.SelectionBox = QtWidgets.QComboBox(SetWarningDialog)
        self.SelectionBox.setObjectName("SelectionBox")
        self.SelectionBox.addItem("")
        self.SelectionBox.addItem("")
        self.SelectionBox.addItem("")
        self.SelectionBox.addItem("")
        self.SelectionBox.addItem("")
        self.SelectionBox.addItem("")
        self.verticalLayout.addWidget(self.SelectionBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ConfirmButton_2 = QtWidgets.QPushButton(SetWarningDialog)
        self.ConfirmButton_2.setObjectName("ConfirmButton_2")
        self.horizontalLayout_2.addWidget(self.ConfirmButton_2)
        self.CancelButton_2 = QtWidgets.QPushButton(SetWarningDialog)
        self.CancelButton_2.setObjectName("CancelButton_2")
        self.horizontalLayout_2.addWidget(self.CancelButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.ImageLabel = QtWidgets.QLabel(SetWarningDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageLabel.sizePolicy().hasHeightForWidth())
        self.ImageLabel.setSizePolicy(sizePolicy)
        self.ImageLabel.setMinimumSize(QtCore.QSize(330, 320))
        self.ImageLabel.setMaximumSize(QtCore.QSize(330, 320))
        self.ImageLabel.setObjectName("ImageLabel")
        self.horizontalLayout_3.addWidget(self.ImageLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SetWarningDialog)
        QtCore.QMetaObject.connectSlotsByName(SetWarningDialog)

    def retranslateUi(self, SetWarningDialog):
        _translate = QtCore.QCoreApplication.translate
        SetWarningDialog.setWindowTitle(_translate("SetWarningDialog", "Set warning"))
        self.SelectionBox.setItemText(0, _translate("SetWarningDialog", "General warning"))
        self.SelectionBox.setItemText(1, _translate("SetWarningDialog", "Traffic light"))
        self.SelectionBox.setItemText(2, _translate("SetWarningDialog", "No entry"))
        self.SelectionBox.setItemText(3, _translate("SetWarningDialog", "Forward only"))
        self.SelectionBox.setItemText(4, _translate("SetWarningDialog", "Left only"))
        self.SelectionBox.setItemText(5, _translate("SetWarningDialog", "Right only"))
        self.ConfirmButton_2.setText(_translate("SetWarningDialog", "Confirm"))
        self.CancelButton_2.setText(_translate("SetWarningDialog", "Cancel"))
        self.ImageLabel.setText(_translate("SetWarningDialog", "Traffic sign image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SetWarningDialog = QtWidgets.QDialog()
    ui = Ui_SetWarningDialog()
    ui.setupUi(SetWarningDialog)
    SetWarningDialog.show()
    sys.exit(app.exec_())
