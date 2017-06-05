# -*- coding: utf-8 -*-
# Copyright (c) 2012-2015, Anima Istanbul
#
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#   File
#    - Author: Aydin Uzmez
#    - File : fileseq
#    - Date: May 2017

import os
import re

class FileSequences(object):
    def __init__(self):
        self.in_path = ""
        self.in_path_name = ""
        self.in_path_name_name = ""
        self.in_path_name_seq_name = ""
        self.in_path_name_ext = ""
        self.current_path = ""
        self.divide_seq_name = ""
        self.main_name = str()
        self.current_path_list = []

    def open(self, path):
        """
        :param path: 
        :return: 
        """
        self.in_path = path
        self.current_path, self.in_path_name = self.in_path.rsplit(os.sep, 1)
        self.current_path_list = os.listdir(self.current_path)

        print self.in_path
        if os.path.isfile(self.in_path):
            print self.in_path_name_seq_name
            self.__spell_iterator()
            self.main_name= self.__divide_path_name(self.in_path_name)
            #self.__name_sum_seq()
            #self.__iterator_sequence()

        else:
            print "Undefined"

    def convert(self):
        name = ''.join(self.main_name[0:2])
        seq_pattern = "%"+str(''.join(self.main_name[2]).__len__())+"d"+self.main_name[3]+self.main_name[4]
        return name+seq_pattern
        #print ''.ljust(self.main_name.__len__(), "#")

    def __name_sum_seq(self):
        self.seq_name = self.divide_seq_name[:-self.seq_length]
        self.seq_name = ''.join(self.seq_name)

    def __spell_iterator(self):
        self.in_path_name_seq_name, self.in_path_name_ext = self.in_path_name.rsplit(".", 1)
        self.name_spell = list(self.in_path_name_seq_name)

    def __divide_path_name(self, in_path_name):
        i = 0
        digit = []
        print self.name_spell
        for spell in reversed(self.name_spell):
            if spell.isdigit() == False:
                if i == 0:
                    return None
                digit.reverse()
                sequence_number_str = ''.join(digit)
                divide = (''.join(self.name_spell[0:-i-1]), self.name_spell[-i-1], sequence_number_str, '.', self.in_path_name_ext)
                #print ''.join(divide[0:2])
                return divide
            digit.append(spell)
            i = i + 1

    def __iterator_sequence(self):
        if self.main_name is not None:
            for each_name in self.current_path_list:
                pass
                #print each_name
                #print self.__divide_path_name(each_name)

            #digit_int = int(self.divide[2])
            #print self.current_path_list
            seq_count = 0
            #digit_length = len(self.sequence_number_str)
            for current in self.current_path_list:
                pass
                #self.sequence_number_str = str(digit_int).zfill(digit_length)
                #digit_int = digit_int + 1
                #seq_count = seq_count + 1

            #name = self.seq_name.ljust(len(self.in_path_name_name) + digit_length, "#") + self.in_path_name_ext
            #print name

"""
    def __multiple_file_seq(self):
        listdir = os.listdir(self.in_path)
        for dir in listdir:
            current_path = os.path.join(self.in_path, dir)
            if os.path.isfile(current_path):
                name, ext = os.path.splitext(dir)
                #self.__single_file_seq(current_path)
                print (dir, ext + " File")
            elif os.path.isdir(current_path):
                print (dir, "Folder")

                # self.counting_sequences(self.digit)

    def __folder_list(self):
        listdir = os.listdir(self.in_path)
        name_list = []
        print listdir
        for file in listdir:
            one_file = os.path.splitext(file)
            divide_file_names = list(one_file[0])
            divide_file_names.reverse()
            print divide_file_names
            sequences_list = []
            i = 0
            for divideName in divide_file_names:
                if divideName.isdigit() == False:
                    del divide_file_names[0:i]
                    divide_file_names.reverse()
                    name = ''.join(divide_file_names)
                    name_list.append(name)

                    break

                i = i + 1
        print name_list
"""

#path1 = r"C:\Users\AYDINU\Desktop\Sequences_Test(DELETE)\sh100.0000.exr"
#path1 = r"C:\Users\AYDINU\Desktop\Sequences_Test(DELETE)\sh1234567 - Copy.exr"
#path1 = r"C:\Users\AYDINU\Desktop\Sequences_Test(DELETE)"
# path1 = r"C:\Users\AYDINU\Desktop\Sequences_Test(DELETE)\sh100.0000.exr"
if __name__ == '__main__':
    path1 = r"C:\Users\AYDINU\Desktop\Sequences_Test(DELETE)\sh1234567.exr"
    filesequences1 = FileSequences()
    filesequences1.open(path1)
    print filesequences1.convert()