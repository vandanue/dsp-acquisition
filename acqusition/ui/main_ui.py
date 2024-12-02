# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 450)
        MainWindow.setMinimumSize(QSize(400, 450))
        MainWindow.setMaximumSize(QSize(400, 450))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.cmbPort = QComboBox(self.centralwidget)
        self.cmbPort.setObjectName(u"cmbPort")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cmbPort)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txtBaudrate = QLineEdit(self.centralwidget)
        self.txtBaudrate.setObjectName(u"txtBaudrate")

        self.horizontalLayout_2.addWidget(self.txtBaudrate)

        self.horizontalSpacer_2 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.txtFilename = QLineEdit(self.centralwidget)
        self.txtFilename.setObjectName(u"txtFilename")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txtFilename)


        self.verticalLayout.addLayout(self.formLayout)

        self.txtData = QPlainTextEdit(self.centralwidget)
        self.txtData.setObjectName(u"txtData")

        self.verticalLayout.addWidget(self.txtData)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(168, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnStop = QPushButton(self.centralwidget)
        self.btnStop.setObjectName(u"btnStop")

        self.horizontalLayout.addWidget(self.btnStop)

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout.addWidget(self.btnStart)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Test Acquisition", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Baudrate", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

