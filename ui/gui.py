# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiUTQPKR.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

import icons.icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(444, 136)
        Dialog.setMinimumSize(QSize(420, 70))
        Dialog.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setStrikeOut(False)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/plot_icon_8_Ywb_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.plotButton = QPushButton(Dialog)
        self.plotButton.setObjectName(u"plotButton")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.plotButton.setFont(font1)
        self.plotButton.setCursor(QCursor(Qt.ArrowCursor))
#if QT_CONFIG(whatsthis)
        self.plotButton.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)

        self.gridLayout.addWidget(self.plotButton, 1, 0, 1, 3)

        self.maCheckBox = QCheckBox(Dialog)
        self.maCheckBox.setObjectName(u"maCheckBox")
        self.maCheckBox.setChecked(False)
        self.maCheckBox.setTristate(False)

        self.gridLayout.addWidget(self.maCheckBox, 4, 0, 1, 1)

        self.maTextBox = QLineEdit(Dialog)
        self.maTextBox.setObjectName(u"maTextBox")
        self.maTextBox.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maTextBox.sizePolicy().hasHeightForWidth())
        self.maTextBox.setSizePolicy(sizePolicy)
        self.maTextBox.setMinimumSize(QSize(100, 20))
        self.maTextBox.setMaximumSize(QSize(16777215, 20))
        self.maTextBox.setBaseSize(QSize(0, 0))
        self.maTextBox.setMaxLength(32762)
        self.maTextBox.setAlignment(Qt.AlignCenter)
        self.maTextBox.setReadOnly(False)

        self.gridLayout.addWidget(self.maTextBox, 4, 1, 1, 1)

        self.datasetButton = QToolButton(Dialog)
        self.datasetButton.setObjectName(u"datasetButton")

        self.gridLayout.addWidget(self.datasetButton, 1, 3, 1, 1)

        self.pathTextBox = QLineEdit(Dialog)
        self.pathTextBox.setObjectName(u"pathTextBox")

        self.gridLayout.addWidget(self.pathTextBox, 0, 0, 1, 3)

        self.datasetList = QComboBox(Dialog)
        self.datasetList.setObjectName(u"datasetList")

        self.gridLayout.addWidget(self.datasetList, 1, 4, 1, 1)

        self.pathButton = QPushButton(Dialog)
        self.pathButton.setObjectName(u"pathButton")

        self.gridLayout.addWidget(self.pathButton, 0, 3, 1, 2)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 5)


        self.retranslateUi(Dialog)
        self.maCheckBox.clicked.connect(self.maTextBox.setEnabled)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Data Plot", None))
        self.plotButton.setText(QCoreApplication.translate("Dialog", u"Plot", None))
        self.maCheckBox.setText(QCoreApplication.translate("Dialog", u"Average Angle", None))
        self.maTextBox.setText(QCoreApplication.translate("Dialog", u"40", None))
        self.datasetButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.pathTextBox.setText(QCoreApplication.translate("Dialog", u"./data/33_/velocity/velocity_line3_33_controller_off_2.csv", None))
        self.pathButton.setText(QCoreApplication.translate("Dialog", u"Get Path", None))
    # retranslateUi

