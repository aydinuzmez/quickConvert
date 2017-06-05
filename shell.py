# -*- coding: utf-8 -*-
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
from ffmpeg.fileseq import FileSequences


FFMPEG_BIN = "ffmpeg"
FFMPEG_BIN = "ffmpeg.exe"

def context_menu():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default="None", help='This path is giving clicking path')
    args = parser.parse_args()
    FF1 = FF(args)
    FF1.convert()


class FF(object):
    def __init__(self,args):
        self.path = args.path

    def convert(self):
        print ("FFmpeg Convert Jpg "+'\n')
        print("File Path: " + self.path )
        fileseq1 =FileSequences()
        fileseq1.open(self.path)
        seq_path = fileseq1.convert()
        name = str(''.join(fileseq1.main_name[0:2]))
        print name
        os.mkdir("jpg")
        print sp.call("ffmpeg -i " +seq_path+ " jpg/abc-%3d.jpg")
        sys.stdout.write("ffmpeg -i " +seq_path+ " jpg/abc-%3d.jpg")
        for i in range(30):
            sys.stdout.write(".")
            sleep(0.2)



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
