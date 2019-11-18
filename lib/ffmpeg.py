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
import sys
import os

if hasattr(sys, "_MEIPASS"):
    FFMPEG = os.path.abspath(os.path.join(sys._MEIPASS, "bin", "ffmpeg.exe"))
    FFPROBE = os.path.abspath(os.path.join(sys._MEIPASS, "bin", "ffprobe.exe"))
    print FFMPEG

else:

    # C:/Users/Aydin/Desktop/quickConvert-master/Setup/Window
    current_path = os.path.dirname(os.path.realpath(__file__))
    BIN_PATH = os.path.abspath(os.path.join(current_path,"..","bin"))
    FFMPEG = os.path.join(BIN_PATH,"ffmpeg.exe")
    FFPROBE = os.path.join(BIN_PATH,"ffprobe.exe")

    FFMPEG = os.path.abspath(os.path.join(current_path, "ffmpeg.exe"))

print(FFMPEG)

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
            # print(self.__call)
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
            return " -vf \"scale=720:432,pad=720:576:(ow-iw)/2:(oh-ih)/2,unsharp=3:3:0.75\" "

    def subprocess(self, queue):
        kuy1 = queue.get()
        self.process = sp.Popen(kuy1, stdout=sp.PIPE, stderr=sp.STDOUT, universal_newlines=True)

        while True:
            line = self.process.stdout.readline().strip()
            search_duration = re.compile("time= *\d+[:]\d+[:]\d+\W\d+").search(line)
            search_frame = re.compile("frame= *\d+").search(line)
            if not line == "":
                if search_frame:
                    self.completed_frame = int(search_frame.group().split("=")[1].strip())
                    print self.completed_frame

                    # if search_duration:
                    #    completed_duration = search_duration.group().split("=")[1].strip()
                    #    self.processing_duration = self.sexa_second(completed_duration)
                    #    print "processing duration "+str(self.processing_duration)
                    # print "Output: " +self.completed_frame
            else:
                self.completed_frame = -1
                break

        queue.task_done()

    def sexa_second(self, sexagesimal):
        """

        :param sexagesimal: 
        :return: milisecond 
        """
        input_split = str(sexagesimal).split(":")
        hours = float(input_split[0]) * 3600
        minutes = float(input_split[1]) * 60
        second = float(input_split[2].split(".")[0])
        microsecond = float(input_split[2].split(".")[1]) / 1000000
        return hours + minutes + second + microsecond

    def completed(self):
        return self.completed_frame

        # print self.process

    def call(self):
        start = time()
        print self.processing_max()
        t1 = Thread(target=self.subprocess, args=(kuyruk,))
        t1.daemon = True
        t1.start()
        kuyruk.put(self.__call)
        #t1.join()
        print "%s saniye surdu" % (time()-start)
        #sp.call(self.__call)

    def makefolder(self):
        path = os.path.join(self.file_seq1.dir_path(), self.__folder_name)

        if os.path.isdir(path):
            print(self.__folder_name)
            print("that file already exists")
            return False
        else:
            os.mkdir(path)
            return True

    def path(self):
        print(self.__path)

    def format(self):
        print(self.__format)

    def call(self):
        sp.call(self.__call)

