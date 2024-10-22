# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Glossary.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Glossary(object):
    def setupUi(self, Glossary):
        if not Glossary.objectName():
            Glossary.setObjectName(u"Glossary")
        Glossary.setWindowModality(Qt.WindowModality.WindowModal)
        Glossary.resize(1018, 520)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Glossary.sizePolicy().hasHeightForWidth())
        Glossary.setSizePolicy(sizePolicy)
        Glossary.setSizeGripEnabled(False)
        Glossary.setModal(False)
        self.label = QLabel(Glossary)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 10, 81, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.Shape.StyledPanel)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setLineWidth(2)
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_2 = QLabel(Glossary)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 1001, 391))
        font1 = QFont()
        font1.setFamilies([u"Monospace"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_2.setLineWidth(3)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.glossaryClose = QPushButton(Glossary)
        self.glossaryClose.setObjectName(u"glossaryClose")
        self.glossaryClose.setGeometry(QRect(460, 480, 81, 29))
        self.glossaryClose.setFont(font)

        self.retranslateUi(Glossary)
        self.glossaryClose.clicked.connect(Glossary.closeGlossary)

        QMetaObject.connectSlotsByName(Glossary)
    # setupUi

    def retranslateUi(self, Glossary):
        Glossary.setWindowTitle(QCoreApplication.translate("Glossary", u"Glossary", None))
        self.label.setText(QCoreApplication.translate("Glossary", u"Glossary", None))
        self.label_2.setText(QCoreApplication.translate("Glossary", u"<html><head/><body><p>Allow Any : Anyone logged in from anywhere<br/><br/>Allow Inactive : Users logged in remotely<br/><br/>Allow Active : Users logged in at a system terminal</p><p><br/></p><p>no : Not authorized.<br/><br/>yes : Authorized.<br/><br/>auth_self : Authentication by the owner of the session that the client originates from is required.<br/><br/>auth_admin : Authentication by an administrative user is required.<br/><br/>auth_self_keep : Like auth_self but the authorization is kept for a brief period.<br/><br/>auth_admin_keep : Like auth_admin but the authorization is kept for a brief period.</p></body></html>", None))
        self.glossaryClose.setText(QCoreApplication.translate("Glossary", u"Close", None))
    # retranslateUi

