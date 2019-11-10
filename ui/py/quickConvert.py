# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/AYDINU/Documents/shell-ffmpeg/ui\ui\quickConvert.ui'
#
# Created: Tue Jun 20 17:45:18 2017
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_quickConvert(object):
    def setupUi(self, quickConvert):
        quickConvert.setObjectName(_fromUtf8("quickConvert"))
        quickConvert.resize(499, 167)
        self.path_widget = QtGui.QWidget(quickConvert)
        self.path_widget.setObjectName(_fromUtf8("path_widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.path_widget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.path_gridlayout = QtGui.QGridLayout()
        self.path_gridlayout.setObjectName(_fromUtf8("path_gridlayout"))
        self.path_text = QtGui.QLabel(self.path_widget)
        self.path_text.setObjectName(_fromUtf8("path_text"))
        self.path_gridlayout.addWidget(self.path_text, 0, 0, 1, 1)
        self.path_edit = QtGui.QLineEdit(self.path_widget)
        self.path_edit.setObjectName(_fromUtf8("path_edit"))
        self.path_gridlayout.addWidget(self.path_edit, 0, 1, 1, 1)
        self.path_browse = QtGui.QToolButton(self.path_widget)
        self.path_browse.setObjectName(_fromUtf8("path_browse"))
        self.path_gridlayout.addWidget(self.path_browse, 0, 2, 1, 1)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.path_gridlayout)
        self.file_gridlayout = QtGui.QGridLayout()
        self.file_gridlayout.setObjectName(_fromUtf8("file_gridlayout"))
        self.foldername_text = QtGui.QLabel(self.path_widget)
        self.foldername_text.setObjectName(_fromUtf8("foldername_text"))
        self.file_gridlayout.addWidget(self.foldername_text, 1, 1, 1, 1)
        self.foldername_edit = QtGui.QLineEdit(self.path_widget)
        self.foldername_edit.setObjectName(_fromUtf8("foldername_edit"))
        self.file_gridlayout.addWidget(self.foldername_edit, 1, 2, 1, 1)
        self.file_attribute = QtGui.QGridLayout()
        self.file_attribute.setObjectName(_fromUtf8("file_attribute"))
        self.format_text = QtGui.QLabel(self.path_widget)
        self.format_text.setObjectName(_fromUtf8("format_text"))
        self.file_attribute.addWidget(self.format_text, 0, 2, 1, 1)
        self.format_combo = QtGui.QComboBox(self.path_widget)
        self.format_combo.setObjectName(_fromUtf8("format_combo"))
        self.format_combo.addItem(_fromUtf8(""))
        self.format_combo.addItem(_fromUtf8(""))
        self.file_attribute.addWidget(self.format_combo, 0, 3, 1, 1)
        self.size_combo = QtGui.QComboBox(self.path_widget)
        self.size_combo.setObjectName(_fromUtf8("size_combo"))
        self.size_combo.addItem(_fromUtf8(""))
        self.size_combo.addItem(_fromUtf8(""))
        self.size_combo.addItem(_fromUtf8(""))
        self.size_combo.addItem(_fromUtf8(""))
        self.file_attribute.addWidget(self.size_combo, 0, 1, 1, 1)
        self.size = QtGui.QLabel(self.path_widget)
        self.size.setObjectName(_fromUtf8("size"))
        self.file_attribute.addWidget(self.size, 0, 0, 1, 1)
        self.file_gridlayout.addLayout(self.file_attribute, 1, 0, 1, 1)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.file_gridlayout)
        self.button_layout = QtGui.QVBoxLayout()
        self.button_layout.setObjectName(_fromUtf8("button_layout"))
        self.buttonBox = QtGui.QDialogButtonBox(self.path_widget)
        self.buttonBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.button_layout.addWidget(self.buttonBox)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.button_layout)
        self.horizontalLayout_2.addLayout(self.formLayout)
        quickConvert.setCentralWidget(self.path_widget)
        self.menubar = QtGui.QMenuBar(quickConvert)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        quickConvert.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(quickConvert)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        quickConvert.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(quickConvert)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(quickConvert)
        QtCore.QMetaObject.connectSlotsByName(quickConvert)

    def retranslateUi(self, quickConvert):
        quickConvert.setWindowTitle(
            QtGui.QApplication.translate("quickConvert", "quickConvert v0.02dev", None, QtGui.QApplication.UnicodeUTF8))
        self.path_text.setText(QtGui.QApplication.translate("quickConvert", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin:5px 5px 5px 5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Path :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.path_browse.setText(QtGui.QApplication.translate("quickConvert", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.foldername_text.setText(QtGui.QApplication.translate("quickConvert", "Folder Name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.foldername_edit.setText(QtGui.QApplication.translate("quickConvert", "jpg", None, QtGui.QApplication.UnicodeUTF8))
        self.format_text.setText(QtGui.QApplication.translate("quickConvert", "Format :", None, QtGui.QApplication.UnicodeUTF8))
        self.format_combo.setItemText(0, QtGui.QApplication.translate("quickConvert", "jpg", None, QtGui.QApplication.UnicodeUTF8))
        self.format_combo.setItemText(1, QtGui.QApplication.translate("quickConvert", "tga", None, QtGui.QApplication.UnicodeUTF8))
        self.size_combo.setItemText(0, QtGui.QApplication.translate("quickConvert", "Same", None, QtGui.QApplication.UnicodeUTF8))
        self.size_combo.setItemText(1, QtGui.QApplication.translate("quickConvert", "1920x1080", None, QtGui.QApplication.UnicodeUTF8))
        self.size_combo.setItemText(2, QtGui.QApplication.translate("quickConvert", "1280x720", None, QtGui.QApplication.UnicodeUTF8))
        self.size_combo.setItemText(3, QtGui.QApplication.translate("quickConvert", "PAL", None, QtGui.QApplication.UnicodeUTF8))
        self.size.setText(QtGui.QApplication.translate("quickConvert", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">*Size :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("quickConvert", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("quickConvert", "Open", None, QtGui.QApplication.UnicodeUTF8))

