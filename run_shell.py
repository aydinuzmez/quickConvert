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
        self.ui.path_browse.clicked.connect(self.file_browser)
        self.statusBar().showMessage("Ready")
        self.progressBar = QtGui.QProgressBar()
        self.progressBar.setTextVisible(False)
        self.statusBar().addPermanentWidget(self.progressBar)


    def set_progressbar(self, process=0, max=100):
        print {"process": process, "max": max}
        self.progressBar.setValue(process)
        self.progressBar.setMaximum(max)
        self.statusBar().showMessage("Rendering/ Completed Frame %s / %s" % (process, self.progressBar.text()))

    def path_set_edit(self, path):
        self.ui.path_edit.setText(path)

    def file_browser(self):
        file_browser = QtGui.QFileDialog.getOpenFileName()
        if file_browser:
            self.ui.path_edit.setText(file_browser)

    def ok(self):
        self.arg = {"path": str(self.ui.path_edit.text()),
                    "size": str(self.ui.size_combo.currentText()),
                    "format": str(self.ui.format_combo.currentText()),
                    "folder_name": str(self.ui.foldername_edit.text())
                    }

        ffmpeg1 = FFmpeg(self.arg)
        if ffmpeg1.makefolder():
            ffmpeg1.call()
            while True:
                completed_frame = ffmpeg1.completed_frame
                self.set_progressbar(completed_frame, int(ffmpeg1.processing_max()))
                if completed_frame == -1:
                    break

            sys.exit()

        else:
            QtGui.QMessageBox().information(QtGui.QWidget.__init__(self, None), "Message",
                                                  "{0} folder already exist.".format(self.arg["format"]))


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
