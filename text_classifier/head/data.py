__author__ = 'jan'

from text_classifier.body.textpair import TextPair
from text_classifier.head.feature import Feature
import re

'''
Class Data :


'''


class Data(object):

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.real_data = {}
        self.real_data_size = 0
        # self.feature_list = None ; Soll implementieren, welche und wieviele attribute vorhanden sind.

    def __str__(self):
        return "Korpus: " + "'"+self.raw_data.name+"'" + ", mit " + str(self.raw_data.size) + " Texten" +\
               "\n"+"Annotierte Textpaare: " + str(self.real_data_size)

    def add_anno(self, anno_file):
        """

        :param anno_file:
        :return:
        """
        with open(anno_file, "r") as f:
            for line in f.readlines():
                pattern = re.search("Text (\d+), Text (\d+)\t\t(\d)", line)
                textpair = TextPair(self.raw_data.content[int(pattern.group(1))],
                                    self.raw_data.content[int(pattern.group(2))],
                                    int(pattern.group(3)))

                self.real_data[textpair.name] = textpair
        self.real_data_size = len(self.real_data)
        f.close()

    def attach_feature(self, feature_name):
        """

        :param feature_name:
        :return:
        """
        if self.real_data_size == 0:
            print "No Annotation set. Please add_anno first."
        else:
            self.real_data = Feature.add_attribute(feature_name, self.real_data)

    def attach_feature_list(self, feature_list):
        """

        :param feature_list:
        :return:
        """
        if self.real_data_size == 0:
            print "No Annotation set. Please add_anno first."
        else:
            self.real_data = Feature.add_attribute_list(feature_list, self.real_data)

