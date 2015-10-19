from text_classifier.body.text import Text
from text_classifier.body.textpair import TextPair
from text_classifier.head.feature import Feature
from text_classifier.exceptions import WrongKorpusFileFormatException
from text_classifier.exceptions import NoAnnotationException
import re
import collections

__author__ = 'jan'

'''
Class Data :


'''


class Data(object):
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.real_data = {}
        self.r_D_text_set = set()
        self.real_data_size = 0
        self.feature_list = ["bag_of_words", "tf_idf", "readability", "variety", "perfect_tense",
                             "passive", "adjective", "sentence_start","test_attribute"]

    def __str__(self):
        return "Korpus: " + "'" + self.raw_data.name + "'" + ", mit " + str(self.raw_data.size) + " Texten" + \
               "\n" + "Annotierte Textpaare: " + str(self.real_data_size)

    def add_anno(self, anno_file):
        """

        :param anno_file:
        :return:
        """
        with open(anno_file, "r") as f:
            for line in f.readlines():
                pattern = re.search("Text (\d+), Text (\d+)\t\t(\d)", line)
                if pattern is not None and len(pattern.groups()) == 3:
                    textpair = TextPair(self.raw_data.content[int(pattern.group(1))],
                                        self.raw_data.content[int(pattern.group(2))],
                                        int(pattern.group(3)))

                    self.real_data[textpair.name] = textpair
                else:
                    raise WrongKorpusFileFormatException(anno_file)
        self.real_data_size = len(self.real_data)
        f.close()

        for textpair in self.real_data.values():
            self.r_D_text_set.add(textpair.text1)
            self.r_D_text_set.add(textpair.text2)

    def attach_feature(self, feature_name):
        """

        :param feature_name:
        :return:
        """

        if self.real_data_size == 0:
            raise NoAnnotationException(self.raw_data.name)
        else:
            Feature.add_attribute(feature_name, self.r_D_text_set)

    def attach_feature_list(self, feature_list):
        """

        :param feature_list:
        :return:
        """
        if self.real_data_size == 0:
            raise NoAnnotationException(self.raw_data.name)
        else:
            Feature.add_attribute_list(feature_list, self.r_D_text_set)


#####################################################
# Analyze Data
####################################################

def summarize(data_set):
    text_category_list = []
    for obj in data_set:
        if type(obj) is TextPair:
            text_category_list.append(obj.text1.category)
            text_category_list.append(obj.text2.category)
        elif type(obj) is Text:
            text_category_list.append(obj.category)
        else:
            print "wrong data_input"

    printer(collections.Counter(text_category_list))


def printer(counter_dic):
    counter_dic["Anno_Texts"] = 0
    for i in counter_dic.keys():
        counter_dic["Anno_Texts"] += counter_dic[i]
    counter_dic["auto_gesamt"] = counter_dic["auto_gut"] + counter_dic["auto_schlecht"]
    print "----------------------------------"
    print "Overall_Anno_Texts: ", counter_dic["Anno_Texts"]
    print "----------------------------------"
    for i in counter_dic.keys():
        if i == "Anno_Texts":
            continue
        else:
            print i, ": ", counter_dic[i], ";", round(float(counter_dic[i]) / (float(counter_dic["Anno_Texts"]) / 100), 2), "%"
    print "----------------------------------"
