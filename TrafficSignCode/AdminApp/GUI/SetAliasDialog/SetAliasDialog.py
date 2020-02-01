# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetAliasDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetAliasDialog(object):
    def setupUi(self, SetAliasDialog):
        SetAliasDialog.setObjectName("SetAliasDialog")
        SetAliasDialog.resize(398, 262)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SetAliasDialog.sizePolicy().hasHeightForWidth())
        SetAliasDialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        SetAliasDialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(SetAliasDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SetAliasLabel = QtWidgets.QLabel(SetAliasDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SetAliasLabel.setFont(font)
        self.SetAliasLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SetAliasLabel.setObjectName("SetAliasLabel")
        self.verticalLayout_3.addWidget(self.SetAliasLabel)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CurrentNameLabel = QtWidgets.QLabel(SetAliasDialog)
        self.CurrentNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentNameLabel.setObjectName("CurrentNameLabel")
        self.verticalLayout_2.addWidget(self.CurrentNameLabel)
        self.CurrentNameTextBox = QtWidgets.QLineEdit(SetAliasDialog)
        self.CurrentNameTextBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.CurrentNameTextBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.CurrentNameTextBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CurrentNameTextBox.setReadOnly(True)
        self.CurrentNameTextBox.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.CurrentNameTextBox.setObjectName("CurrentNameTextBox")
        self.verticalLayout_2.addWidget(self.CurrentNameTextBox)
        self.NewNameLabel = QtWidgets.QLabel(SetAliasDialog)
        self.NewNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NewNameLabel.setObjectName("NewNameLabel")
        self.verticalLayout_2.addWidget(self.NewNameLabel)
        self.NewNameTextBox = QtWidgets.QLineEdit(SetAliasDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.NewNameTextBox.sizePolicy().hasHeightForWidth())
        self.NewNameTextBox.setSizePolicy(sizePolicy)
        self.NewNameTextBox.setObjectName("NewNameTextBox")
        self.verticalLayout_2.addWidget(self.NewNameTextBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ConfirmButton = QtWidgets.QPushButton(SetAliasDialog)
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.horizontalLayout.addWidget(self.ConfirmButton)
        self.CancelButton = QtWidgets.QPushButton(SetAliasDialog)
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SetAliasDialog)
        QtCore.QMetaObject.connectSlotsByName(SetAliasDialog)

    def retranslateUi(self, SetAliasDialog):
        _translate = QtCore.QCoreApplication.translate
        SetAliasDialog.setWindowTitle(_translate("SetAliasDialog", "Set alias"))
        self.SetAliasLabel.setText(_translate("SetAliasDialog", "Set alias:"))
        self.CurrentNameLabel.setText(_translate("SetAliasDialog", "Current name:"))
        self.NewNameLabel.setText(_translate("SetAliasDialog", "New name:"))
        self.ConfirmButton.setText(_translate("SetAliasDialog", "Confirm"))
        self.CancelButton.setText(_translate("SetAliasDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SetAliasDialog = QtWidgets.QWidget()
    ui = Ui_SetAliasDialog()
    ui.setupUi(SetAliasDialog)
    SetAliasDialog.show()
    sys.exit(app.exec_())
