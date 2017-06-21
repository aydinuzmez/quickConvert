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
from lib.cmd_color import Cmd

from PyQt4 import QtGui
from PyQt4 import QtCore
from ui.py.quickConvert import Ui_quickConvert
from lib.ffmpeg import FFmpeg


FFMPEG_BIN = "ffmpeg"


class UI(QtGui.QMainWindow,Ui_quickConvert):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
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
            print self.arg["folder_name"]
            print "that file already exists"
        else:
            os.mkdir(self.arg["folder_name"])
            ffmpeg1 = FFmpeg(self.arg)
            ffmpeg1.call()
            #ff1 = FFmpeg(self.ui.path_edit.text())
            #ff1.convert()
            sys.exit()


"""
class FFmpeg(object):
    def __init__(self,args):
        self.path = str(args)

    def convert(self):
        print ("FFmpeg Convert Jpg "+'\n')
        print("File Path: " + self.path)
        sp.call(['import','os'],shell=True)
        cmd1 = Cmd()
        try:
            print sp.call(ffmpeg_call1.call)

        except WindowsError as e:
            print cmd1.write(e,"red")
            return
        except Exception:
            print cmd1.write("The file isn't support now","red")
            return

        for i in range(6):
            sys.stdout.write(cmd1.write("Succesfull","green"))
"""

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
    #ff1 = FF(path_arg)
    #ff1.convert()

    sys.exit(app.exec_())

"""
command = [FFMPEG_BIN,
           '-i', r"C:\Users\AYDINU\Desktop\ffmpeg\input\Casper_VIA_F1_%04d.exr", r"C:\Users\AYDINU\Desktop\ffmpeg\png\abc_%04d.jpg"]


pipe = sp.Popen(command,stdout=sp.PIPE,bufsize=10**8)
pipe.stdout.readline()
pipe.terminate()
"""


if __name__ == "__main__":
    run()
