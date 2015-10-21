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
    def __init__(self, name, raw_data):
        self.name = name
        self.raw_data = raw_data
        self.real_data = {}
        self.r_D_text_set = set()
        self.real_data_size = 0
        self.features_fit = []
        self.feature_list = ["bag_of_words", "tf_idf", "readability", "variety", "perfect_tense",
                             "passive", "adjective", "sentence_start","test_attribute"]
        self.bow_model = None

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
            feature = Feature(name=feature_name, bow_model=self.bow_model)
            feature.add_attribute(self.r_D_text_set)
            self.bow_model = feature.bow_model
            self.features_fit.append(feature_name)

    def attach_feature_list(self, feature_list):
        """

        :param feature_list:
        :return:
        """
        if self.real_data_size == 0:
            raise NoAnnotationException(self.raw_data.name)
        else:
            feature = Feature(name_list=feature_list, bow_model=self.bow_model)
            feature.add_attribute_list(self.r_D_text_set)
            self.bow_model = feature.bow_model

            for feature_name in feature_list:
                self.features_fit.append(feature_name)

#####################################################
# Analyze Data
####################################################

def summarize_text(data_set):
    text_category_list = []
    for obj in data_set:
        if type(obj) is TextPair:
            text_category_list.append(obj.text1.category)
            text_category_list.append(obj.text2.category)
        elif type(obj) is Text:
            text_category_list.append(obj.category)
        else:
            print "wrong data_input"
    print "----------------Text--------------"
    printer(collections.Counter(text_category_list))


def summarize_textpair(data_set):
    text_selected_list = []
    for textpair in data_set:
        text_selected_list.append(select_anno(textpair))
        # print textpair.text1.category, "---", textpair.text2.category
        #######################
        #### Auto-Schlecht ####
        #######################
        # if textpair.text1.category == "man" and textpair.text2.category == "auto_schlecht":
        #     text_selected_list.append(select_anno(textpair))
        # if textpair.text1.category == "auto_gut" and textpair.text2.category == "auto_schlecht":
        #     text_selected_list.append(select_anno(textpair))
        # if textpair.text1.category == "auto_schlecht" and textpair.text2.category == "man":
        #     text_selected_list.append(select_anno(textpair))
        # if textpair.text1.category == "auto_schlecht" and textpair.text2.category == "auto_gut":
        #     text_selected_list.append(select_anno(textpair))

        #######################
        #### Auto-Man-All #########
        #######################
        # if textpair.text1.category == "man" and textpair.text2.category == "auto_schlecht":
        #     text_selected_list.append(select_anno(textpair))
        # elif textpair.text1.category == "man" and textpair.text2.category == "auto_gut":
        #     text_selected_list.append(select_anno(textpair))
        # elif textpair.text1.category == "auto_schlecht" and textpair.text2.category == "man":
        #     text_selected_list.append(select_anno(textpair))
        # elif textpair.text1.category == "auto_gut" and textpair.text2.category == "man":
        #     text_selected_list.append(select_anno(textpair))

        #######################
        #### Auto-All #########
        #######################
        # if textpair.text1.category == "auto_gut" and textpair.text2.category == "auto_schlecht":
        #     text_selected_list.append(select_anno(textpair))
        # elif textpair.text1.category == "auto_schlecht" and textpair.text2.category == "auto_gut":
        #     text_selected_list.append(select_anno(textpair))

        ###########################
        #### Auto_gut-Man #########
        ###########################
        # if textpair.text1.category == "man" and textpair.text2.category == "auto_gut":
        #     text_selected_list.append(select_anno(textpair))
        # elif textpair.text1.category == "auto_gut" and textpair.text2.category == "man":
        #     text_selected_list.append(select_anno(textpair))

    print "-------------Textpair-------------"
    printer(collections.Counter(text_selected_list))


def select_anno(textpair):
    if textpair.target == 0:
        return textpair.text1.category
    else:
        return textpair.text2.category


def printer(counter_dic):
    counter_dic["Overall"] = 0
    for i in counter_dic.keys():
        counter_dic["Overall"] += counter_dic[i]
    counter_dic["auto_gesamt"] = counter_dic["auto_gut"] + counter_dic["auto_schlecht"]
    print "----------------------------------"
    print "Overall: ", counter_dic["Overall"]
    print "----------------------------------"
    for i in counter_dic.keys():
        if i == "Overall":
            continue
        else:
            print i, ": ", counter_dic[i], ";", round(float(counter_dic[i]) / (float(counter_dic["Overall"]) / 100), 2), "%"
    print "----------------------------------"
