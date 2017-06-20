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

FFMPEG = "ffmpeg"

class Call(object):
    def __init__(self,path):
        self.path = path
        fileseq1 = FileSequences(self.path)
        try:
            if int(fileseq1.digit()) == 0:
                self.call = FFMPEG+" -i {0} jpg/{1}.jpg".format(fileseq1.name() + fileseq1.format() + fileseq1.ext(),fileseq1.name() + fileseq1.format())
                print self.call
            else:
                self.call = FFMPEG+" {0} -i {1} {0} jpg/{2}.jpg".format("-start_number "+fileseq1.digit(),fileseq1.name() + fileseq1.format() + fileseq1.ext(),fileseq1.name() + fileseq1.format())
        except Exception as e:
            print e


if __name__ == '__main__':
    call1 = Call(r"C:\Users\AYDINU\Documents\shell-ffmpeg\test\_SEQ_INTERVAL\sh100_0010.exr")
    print call1.call

