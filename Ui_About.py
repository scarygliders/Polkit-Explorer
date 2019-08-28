# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created: Tue Mar 26 14:49:52 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.setWindowModality(QtCore.Qt.NonModal)
        About.resize(400, 375)
        self.frame = QtWidgets.QFrame(About)
        self.frame.setGeometry(QtCore.QRect(9, 9, 381, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 10, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setLineWidth(3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 361, 151))
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.closeAboutButton = QtWidgets.QPushButton(self.frame)
        self.closeAboutButton.setGeometry(QtCore.QRect(150, 330, 87, 29))
        self.closeAboutButton.setObjectName(_fromUtf8("closeAboutButton"))
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(130, 60, 151, 141))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("PKEIconV001.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(About)
        self.closeAboutButton.clicked.connect(About.aboutClose)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(QtWidgets.QApplication.translate("About", "About Polkit Explorer", None))
        self.label.setText(QtWidgets.QApplication.translate("About", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Polkit Explorer</span></p></body></html>", None))
        self.label_2.setText(QtWidgets.QApplication.translate("About", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Author : Kevin Cave.</span></p><p><span style=\" font-size:11pt; font-weight:600;\">Version : 1.0</span></p><p><span style=\" font-size:11pt; font-weight:600;\">Allows a user to load polkit-1 .policy files and explore their contents in a human-readable format.</span></p></body></html>", None))
        self.closeAboutButton.setText(QtWidgets.QApplication.translate("About", "Close", None))

