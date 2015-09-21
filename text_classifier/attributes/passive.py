# -*- coding: utf-8 -*-
import imp
import sys
from subprocess import *
import treetaggerwrapper
import re
import os
import attribute
__author__ = 'jan'


class Passive(attribute.Attribute):

    def __init__(self):
        self._name = "passive"
        self._text_set = None
        self.analyses_dict = {}
        self.analyses_list = []
        self.id_len_tuples = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def text_set(self):
        return self._text_set

    @text_set.setter
    def text_set(self, new_value):
        self._text_set = new_value

    def compute(self):
        self.parse_analyses()
        self.fill_analyses_dict()
        for text in self._text_set:
            text.features["passive"] = self.count_passive(text.id)
            print "text_id: ",text.id, "passive_count: ", text.features["passive"]

    def parse_analyses(self):
        tmp = open("tmp.txt", "w")

        for text in self._text_set:
            self.id_len_tuples.append((text.id, len(text.sentencelist)))
            tmp.write(text.text + "\n")

        tmp.close()
        tmp2 = open("tmp.txt", "r")
        output = Popen('/home/jan/Development-Tools/ParZu_Parser/ParZu/parzu', stdin=tmp2, stdout=PIPE).communicate()[0]

        self.analyses_list = re.findall("analyses.*", output)
        tmp2.close()
        os.remove("/home/jan/Development/Text_Classifier/text_classifier/tmp.txt")

    def fill_analyses_dict(self):
        ######################################################################################
        # read analyses from analyses_list into analyses_dict, to look for passive constructions.
        #######################################################################################
        start = 0

        for tupl in self.id_len_tuples:
            text_id = tupl[0]
            length = tupl[1]
            end = start + (length - 1) + 1
            tmp_list = []

            for analyses in self.analyses_list[start:end]:
                tmp_list.append(analyses)

            self.analyses_dict[text_id] = tmp_list
            start = end

    def count_passive(self, text_id):
        count = 0
        for analyses in self.analyses_dict[text_id]:
            if "passive" in analyses:
                count += 1
        return count
