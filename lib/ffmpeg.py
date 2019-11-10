# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, Aydin Uzmez
#
# This module is part of shell_ffmpeg and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#   File
#    - Author: Aydin Uzmez
#    - File : ffmpeg
#    - Date: Jun 2017

from lib.fileseq import FileSequences
import subprocess as sp
import os

# C:/Users/Aydin/Desktop/quickConvert-master/Setup/Window
current_path = os.path.dirname(os.path.realpath(__file__))

FFMPEG = os.path.abspath(os.path.join(current_path, "..", "ffmpeg", "ffmpeg.exe"))


class FFmpeg(object):
    def __init__(self, arg):
        self.__size = arg["size"]
        self.__format = arg["format"]
        self.__folder_name = arg["folder_name"]
        self.__path = arg["path"]

        self.file_seq1 = FileSequences(self.__path)
        self.__input_name = self.file_seq1.name() + self.file_seq1.format() + self.file_seq1.ext()
        self.__output_name = self.file_seq1.name() + self.file_seq1.format() + "." + self.__format

        try:
            #if int(self.file_seq1.digit()) == 0:
            #    self.call = FFMPEG+" -i {0} {1}/{2}".format(self.__input_name,
            #                                                self.__folder_name,
            #                                                self.__output_name)
            #    print self.call
            #else:
            self.__call = FFMPEG + " -start_number {0} -i {1} {4} -start_number {0} {3}/{2}".format(self.file_seq1.digit(),
                                                                                                    self.__input_name,
                                                                                                    self.__output_name,
                                                                                                    self.__folder_name,
                                                                                                    self.size()
                                                                                                    )
        except Exception as e:
            print(e)


    def input(self):
        print(self.file_seq1.name() + self.file_seq1.format() + self.file_seq1.ext())

    def output(self):
        print(self.file_seq1.name() + self.file_seq1.format() + "." + self.__format)

    def size(self):
        if self.__size == "Same":
            return ""

        elif self.__size == "1920x1080":
            return " -s 1920x1080 "

        elif self.__size == "1280x720":
            return " -s 1280x720 "

        elif self.__size == "PAL":
            return ""

    def path(self):
        print(self.__path)

    def format(self):
        print(self.__format)

    def call(self):
        sp.call(self.__call)

