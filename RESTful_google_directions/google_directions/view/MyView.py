# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DirectionsView.ui'
#
# Created: Wed Nov 23 20:39:22 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 595)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 781, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_start = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_start.setMinimumSize(QtCore.QSize(30, 0))
        self.label_start.setObjectName("label_start")
        self.horizontalLayout_2.addWidget(self.label_start)
        self.lineEdit_start = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_start.setObjectName("lineEdit_start")
        self.horizontalLayout_2.addWidget(self.lineEdit_start)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_ziel = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_ziel.setMinimumSize(QtCore.QSize(30, 0))
        self.label_ziel.setObjectName("label_ziel")
        self.horizontalLayout_3.addWidget(self.label_ziel)
        self.lineEdit_ziel = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_ziel.setObjectName("lineEdit_ziel")
        self.horizontalLayout_3.addWidget(self.lineEdit_ziel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textEdit_output = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_output.setObjectName("textEdit_output")
        self.textEdit_output.setReadOnly(True)                           # Ausgabefeld kann nicht mehr bearbeitet werden
        self.verticalLayout.addWidget(self.textEdit_output)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_submit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.horizontalLayout_10.addWidget(self.pushButton_submit)
        self.pushButton_reset = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.horizontalLayout_10.addWidget(self.pushButton_reset)
        self.pushButton_close = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_10.addWidget(self.pushButton_close)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_close, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QObject.connect(self.pushButton_reset, QtCore.SIGNAL("clicked()"), self.lineEdit_start.clear)
        QtCore.QObject.connect(self.pushButton_reset, QtCore.SIGNAL("clicked()"), self.lineEdit_ziel.clear)
        QtCore.QObject.connect(self.pushButton_reset, QtCore.SIGNAL("clicked()"), self.textEdit_output.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "RESTful Google Directions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_start.setText(QtGui.QApplication.translate("MainWindow", "Start:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_start.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Adresse, Stadt, Land", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ziel.setText(QtGui.QApplication.translate("MainWindow", "Ziel:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ziel.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Adresse, Stadt, Land", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_submit.setText(QtGui.QApplication.translate("MainWindow", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_reset.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_close.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))

