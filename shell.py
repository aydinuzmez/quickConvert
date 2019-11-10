# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, Aydin Uzmez
#
# This module is part of shell_ffmpeg and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

#   File
#    - Author: Aydin Uzmez
#    - File : shell.py
#    - Date: April 2017
#

import argparse
import sys
import os

from PyQt4 import QtGui
from ui.py.quickConvert import Ui_quickConvert
from lib.ffmpeg import FFmpeg


class UI(QtGui.QMainWindow, Ui_quickConvert):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.arg = {}
        self.ui = Ui_quickConvert()
        self.ui.setupUi(self)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.ok)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(sys.exit)

    def path_set_edit(self, path):
        self.ui.path_edit.setText(path)

    def ok(self):
        self.arg = {"path": str(self.ui.path_edit.text()),
                    "size": str(self.ui.size_combo.currentText()),
                    "format": str(self.ui.format_combo.currentText()),
                    "folder_name": str(self.ui.foldername_edit.text())
                    }

        if os.path.isdir(self.arg["folder_name"]):
            print(self.arg["folder_name"])
            print("that file already exists")
        else:
            os.mkdir(self.arg["folder_name"])
            ffmpeg1 = FFmpeg(self.arg)
            ffmpeg1.call()
            sys.exit()


class Parser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--path", type=str, default="None", help='This path is giving clicking path')

    def arg(self):
        return self.parser.parse_args()


def run():
    parser1 = Parser()
    arg = parser1.arg()

    app = QtGui.QApplication(sys.argv)
    ui1 = UI()
    ui1.path_set_edit(arg.path)
    ui1.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
