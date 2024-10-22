# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'About.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.setWindowModality(Qt.WindowModality.NonModal)
        About.resize(400, 386)
        self.frame = QFrame(About)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 381, 371))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 0, 281, 41))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setLineWidth(3)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 260, 361, 71))
        self.label_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2.setTextFormat(Qt.TextFormat.RichText)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.closeAboutButton = QPushButton(self.frame)
        self.closeAboutButton.setObjectName(u"closeAboutButton")
        self.closeAboutButton.setGeometry(QRect(150, 340, 87, 29))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 40, 151, 141))
        self.label_3.setPixmap(QPixmap(u"PKEIconV001.png"))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 180, 361, 31))
        self.label_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4.setTextFormat(Qt.TextFormat.RichText)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.versionlabel = QLabel(self.frame)
        self.versionlabel.setObjectName(u"versionlabel")
        self.versionlabel.setGeometry(QRect(10, 219, 361, 31))
        self.versionlabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.versionlabel.setFrameShadow(QFrame.Shadow.Raised)
        self.versionlabel.setTextFormat(Qt.TextFormat.RichText)
        self.versionlabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.versionlabel.setWordWrap(True)
        self.versionlabel.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.retranslateUi(About)
        self.closeAboutButton.clicked.connect(About.aboutClose)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"About Polkit Explorer", None))
        self.label.setText(QCoreApplication.translate("About", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Polkit Explorer</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("About", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Allows a user to load polkit-1 .policy files and explore their contents in a human-readable format.</span></p></body></html>", None))
        self.closeAboutButton.setText(QCoreApplication.translate("About", u"Close", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("About", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Copyright (c) Kevin Cave 2013-onwards</span></p></body></html>", None))
        self.versionlabel.setText(QCoreApplication.translate("About", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Version :</span></p></body></html>", None))
    # retranslateUi

