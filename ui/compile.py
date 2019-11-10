# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, Aydin Uzmez
#
# This module is part of shell_ffmpeg and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#   File
#    - Author: Aydin Uzmez
#    - File : quick_convert
#    - Date: Jun 2017


import sys
from PyQt4 import QtGui, uic
import os

COMPILE_PATH = os.path.dirname(__file__)

UIFOLDER_PATH = os.path.join(COMPILE_PATH,"ui")
PYFOLDER_PATH = os.path.join(COMPILE_PATH,"py")

UIFILE_PATH = os.path.join(UIFOLDER_PATH,"quickConvert.ui")
PYFILE_PATH = os.path.join(PYFOLDER_PATH,"quickConvert.py")

#UI_FILE = os.getcwd()
print(COMPILE_PATH)

def compile_ui():
    ui_file = file(UIFILE_PATH)
    py_file = file(PYFILE_PATH,"w")
    uic.compileUi(ui_file,py_file)
    ui_file.close()
    py_file.close()
    print("finished compiling")


compile_ui()
