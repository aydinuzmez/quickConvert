# -*- coding: latin1 -*-
# Copyright (c) 2017-2018, Aydin Uzmez
#
# This module is part of shell_ffmpeg and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#   File
#    - Author: Aydin Uzmez
#    - File : cmd_color
#    - Date: Jun 2017

#print u"\u2588" + "asdad" + u"\u2588" * 500



def decorate(func):
    color_type = {
            "default":  "\x1b[0;31;40m",
            "red":      "\x1b[0;37;41m",
            "green":   "\x1b[0;30;42m",
            "yellow":    "\x1b[0;30;43m",
            "blue":     "\x1b[0;30;44m",
            "purple":   "\x1b[0;30;45m",
            "gray":     "\x1b[0;30;47m",
            }
    end= "\x1b[0m"
    def func_wrapper(self,write,color):
        func1 = func(self,write,color)
        #return "{0} {1} \x1b[0m".format(color_type[func1["color"]], func1["write"] )
        return "{0}    {1}    {2}".format(color_type[func1["color"]], func1["write"],end )
    return func_wrapper

class Cmd(object):
    def __init__(self):
        self.CSI = "\x1b[6;30;42m"
        self.end = "\x1b[0m"

    @decorate
    def write(self,write,color="default"):
        return {"write" : write,
                "color" : color
                }

if __name__ == '__main__':
    cmd1 = Cmd()
    print cmd1.write("Successfull","default")
