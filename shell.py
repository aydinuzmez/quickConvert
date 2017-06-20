# -*- coding: latin1 -*-
# Copyright (c) 2012-2015, Anima Istanbul
#
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

#   File
#    - Author: Aydin Uzmez
#    - File : shell.py
#    - Date: April 2017
#

import argparse
import sys
from time import sleep
import subprocess as sp
import os
import re
from lib.cmd_color import Cmd
from lib.fileseq import FileSequences
import ffmpeg.call as ffmpeg


FFMPEG_BIN = "ffmpeg"
FFMPEG_BIN = "ffmpeg.exe"



class FF(object):
    def __init__(self,args):
        self.path = args.path

    def convert(self):
        print ("FFmpeg Convert Jpg "+'\n')
        print("File Path: " + self.path )
        ffmpeg_call1 = ffmpeg.Call(self.path)
        sp.call(['import','os'],shell=True)
       # print sp.call("os.system('color')")
        cmd1 = Cmd()
        try:
            os.mkdir("jpg")
            print sp.call(ffmpeg_call1.call)

        except WindowsError as e:
            print cmd1.write(e,"red")
            return
        except Exception:
            print cmd1.write("The file isn't support now","red")
            return

        for i in range(6):
            sys.stdout.write(cmd1.write("Succesfull","green"))
            #sleep(0.1)


def context_menu():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default="None", help='This path is giving clicking path')
    args = parser.parse_args()
    FF1 = FF(args)
    FF1.convert()

"""
command = [FFMPEG_BIN,
           '-i', r"C:\Users\AYDINU\Desktop\ffmpeg\input\Casper_VIA_F1_%04d.exr", r"C:\Users\AYDINU\Desktop\ffmpeg\png\abc_%04d.jpg"]


pipe = sp.Popen(command,stdout=sp.PIPE,bufsize=10**8)
pipe.stdout.readline()
pipe.terminate()
"""

def FFmpeg(args):
    return args.path

if __name__ == "__main__":
    context_menu()
