# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetailsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DetailsDialog(object):
    def setupUi(self, DetailsDialog):
        DetailsDialog.setObjectName("DetailsDialog")
        DetailsDialog.resize(367, 291)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        DetailsDialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(DetailsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CurrentAliasTooltip = QtWidgets.QLabel(DetailsDialog)
        self.CurrentAliasTooltip.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CurrentAliasTooltip.setObjectName("CurrentAliasTooltip")
        self.horizontalLayout.addWidget(self.CurrentAliasTooltip)
        self.CurrentAliasLabel = QtWidgets.QLabel(DetailsDialog)
        self.CurrentAliasLabel.setObjectName("CurrentAliasLabel")
        self.horizontalLayout.addWidget(self.CurrentAliasLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.IMEITooltip = QtWidgets.QLabel(DetailsDialog)
        self.IMEITooltip.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.IMEITooltip.setObjectName("IMEITooltip")
        self.horizontalLayout_2.addWidget(self.IMEITooltip)
        self.IMEILabel = QtWidgets.QLabel(DetailsDialog)
        self.IMEILabel.setObjectName("IMEILabel")
        self.horizontalLayout_2.addWidget(self.IMEILabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.StatusTooltip = QtWidgets.QLabel(DetailsDialog)
        self.StatusTooltip.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.StatusTooltip.setObjectName("StatusTooltip")
        self.horizontalLayout_3.addWidget(self.StatusTooltip)
        self.StatusLabel = QtWidgets.QLabel(DetailsDialog)
        self.StatusLabel.setObjectName("StatusLabel")
        self.horizontalLayout_3.addWidget(self.StatusLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ValueTooltip = QtWidgets.QLabel(DetailsDialog)
        self.ValueTooltip.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ValueTooltip.setObjectName("ValueTooltip")
        self.horizontalLayout_5.addWidget(self.ValueTooltip)
        self.ValueLabel = QtWidgets.QLabel(DetailsDialog)
        self.ValueLabel.setObjectName("ValueLabel")
        self.horizontalLayout_5.addWidget(self.ValueLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.CloseButton = QtWidgets.QPushButton(DetailsDialog)
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout_4.addWidget(self.CloseButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(DetailsDialog)
        QtCore.QMetaObject.connectSlotsByName(DetailsDialog)

    def retranslateUi(self, DetailsDialog):
        _translate = QtCore.QCoreApplication.translate
        DetailsDialog.setWindowTitle(_translate("DetailsDialog", "DetailsDialog"))
        self.CurrentAliasTooltip.setText(_translate("DetailsDialog", "Current alias:"))
        self.CurrentAliasLabel.setText(_translate("DetailsDialog", "???"))
        self.IMEITooltip.setText(_translate("DetailsDialog", "IMEI:"))
        self.IMEILabel.setText(_translate("DetailsDialog", "???"))
        self.StatusTooltip.setText(_translate("DetailsDialog", "Status:"))
        self.StatusLabel.setText(_translate("DetailsDialog", "???"))
        self.ValueTooltip.setText(_translate("DetailsDialog", "Value:"))
        self.ValueLabel.setText(_translate("DetailsDialog", "???"))
        self.CloseButton.setText(_translate("DetailsDialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DetailsDialog = QtWidgets.QDialog()
    ui = Ui_DetailsDialog()
    ui.setupUi(DetailsDialog)
    DetailsDialog.show()
    sys.exit(app.exec_())
