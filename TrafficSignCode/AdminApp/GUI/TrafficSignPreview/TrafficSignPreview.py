# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrafficSignPreview.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TrafficSignPreview(object):
    def setupUi(self, TrafficSignPreview):
        TrafficSignPreview.setObjectName("TrafficSignPreview")
        TrafficSignPreview.resize(320, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TrafficSignPreview.sizePolicy().hasHeightForWidth())
        TrafficSignPreview.setSizePolicy(sizePolicy)
        TrafficSignPreview.setMinimumSize(QtCore.QSize(320, 320))
        TrafficSignPreview.setMaximumSize(QtCore.QSize(320, 320))
        self.TrafficSignImage = QtWidgets.QLabel(TrafficSignPreview)
        self.TrafficSignImage.setGeometry(QtCore.QRect(0, 0, 320, 320))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TrafficSignImage.sizePolicy().hasHeightForWidth())
        self.TrafficSignImage.setSizePolicy(sizePolicy)
        self.TrafficSignImage.setMinimumSize(QtCore.QSize(320, 320))
        self.TrafficSignImage.setObjectName("TrafficSignImage")

        self.retranslateUi(TrafficSignPreview)
        QtCore.QMetaObject.connectSlotsByName(TrafficSignPreview)

    def retranslateUi(self, TrafficSignPreview):
        _translate = QtCore.QCoreApplication.translate
        TrafficSignPreview.setWindowTitle(_translate("TrafficSignPreview", "Traffic sign preview"))
        self.TrafficSignImage.setText(_translate("TrafficSignPreview", "Traffic sign image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TrafficSignPreview = QtWidgets.QDialog()
    ui = Ui_TrafficSignPreview()
    ui.setupUi(TrafficSignPreview)
    TrafficSignPreview.show()
    sys.exit(app.exec_())
