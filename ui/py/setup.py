# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\AYDINU\Desktop\quickConvert\ui\ui\setup.ui'
#
# Created: Mon Nov 11 17:43:45 2019
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_setup(object):
    def setupUi(self, setup):
        setup.setObjectName(_fromUtf8("setup"))
        setup.resize(400, 200)
        setup.setMinimumSize(QtCore.QSize(400, 200))
        setup.setMaximumSize(QtCore.QSize(400, 200))
        self.centralwidget = QtGui.QWidget(setup)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.run_path_label = QtGui.QLabel(self.centralwidget)
        self.run_path_label.setGeometry(QtCore.QRect(20, 70, 61, 16))
        self.run_path_label.setObjectName(_fromUtf8("run_path_label"))
        self.icon_path_edit = QtGui.QLineEdit(self.centralwidget)
        self.icon_path_edit.setGeometry(QtCore.QRect(110, 40, 241, 21))
        self.icon_path_edit.setObjectName(_fromUtf8("icon_path_edit"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 70, 31, 21))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.icon_path_label = QtGui.QLabel(self.centralwidget)
        self.icon_path_label.setGeometry(QtCore.QRect(20, 40, 51, 16))
        self.icon_path_label.setObjectName(_fromUtf8("icon_path_label"))
        self.run_path_edit = QtGui.QLineEdit(self.centralwidget)
        self.run_path_edit.setGeometry(QtCore.QRect(110, 70, 241, 21))
        self.run_path_edit.setObjectName(_fromUtf8("run_path_edit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 40, 31, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(40, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        setup.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(setup)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        setup.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(setup)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        setup.setStatusBar(self.statusbar)

        self.retranslateUi(setup)
        QtCore.QMetaObject.connectSlotsByName(setup)

    def retranslateUi(self, setup):
        setup.setWindowTitle(QtGui.QApplication.translate("setup", "quickConvert Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.run_path_label.setText(QtGui.QApplication.translate("setup", "Run Path :", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("setup", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.icon_path_label.setText(QtGui.QApplication.translate("setup", "Icon Path :", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("setup", "...", None, QtGui.QApplication.UnicodeUTF8))

