"""
Data class
"""

from text_classifier.body.text import Text
from text_classifier.body.textpair import TextPair
from text_classifier.head.feature import Feature
from text_classifier.exceptions import WrongAnnoFileFormatException
from text_classifier.exceptions import NoAnnotationException
import re
import collections

# Author Jan Wessling


class Data(object):
    """
    Data structure combining coprus and annotation.

    Parameters
    ----------
    name : string, obligatory
        No Data without a name.

    raw_data : Korpus, obligatory
        Contains a korpus object with stored text object in korpus.content.

    Attributes
    -----------
    real_data : hash, shape = {string textpair name : textpair object}
        After reading annotation file, real data is filled with textpair
        obejcts.

    r_D_text_set : set
        Real Data text set contains all unique text objects from the
        real_data hash.

    real_data_size : int
        Contains size of of real_data hash.

    features_fit : array, shape = [string feature1 name, string feature2 name,... ]
        Contains all names of already attached features.

    feature_list : array, shape = [string feature1 name, string feature2 name,... ]
        Contains all names of available features to attach.

    bow_model :  bow skeleton --> hash, shape = { string word : int 0 }
                 bop skeleton --> hash, shape = { string pos tag : int 0 }
        Contains bow or bop skeleton. Inital value is None.
    """

    def __init__(self, name, raw_data):
        self.name = name
        self.raw_data = raw_data
        self.real_data = {}
        self.r_D_text_set = set()
        self.real_data_size = 0
        self.features_fit = []
        self.feature_list = ["bag_of_words", "tf_idf", "readability", "variety", "perfect_tense",
                             "passive", "adjective", "sentence_start", "bag_of_pos", "modal_verb"]
        self.bow_model = None

    def __str__(self):
        return "Korpus: " + "'" + self.raw_data.name + "'" + ", mit " + str(self.raw_data.size) + " Texten" + \
               "\n" + "Annotierte Textpaare: " + str(self.real_data_size)

    def add_anno(self, anno_file):
        """Insert annotation data from annotation file.

        Open annotation file and building textpair object. Storing
        textpair objects in real_data.

        Parameter
        ---------
        anno_file : string
            Contains file path for annotation file.
        """
        with open(anno_file, "r") as f:
            for line in f.readlines():

                # annotaion pattern
                pattern = re.search("Text (\d+), Text (\d+)\t\t(\d)", line)

                if pattern is not None and len(pattern.groups()) == 3:
                    textpair = TextPair(self.raw_data.content[int(pattern.group(1))],
                                        self.raw_data.content[int(pattern.group(2))],
                                        int(pattern.group(3)))

                    self.real_data[textpair.name] = textpair
                else:
                    raise WrongAnnoFileFormatException(anno_file, line)

        self.real_data_size = len(self.real_data)
        f.close()

        for textpair in self.real_data.values():
            self.r_D_text_set.add(textpair.text1)
            self.r_D_text_set.add(textpair.text2)

    def attach_feature(self, feature_name):
        """Attach feature to text objects in real Data set.

        Using feature interface for computing attributes and
        set feature values to text objects in real Data set.

        Parameters
        ----------
        feature_name : string
            Contains the name of the corresponding feature, that
            should be attached.
        """

        if self.real_data_size == 0:
            raise NoAnnotationException(self.raw_data.name)

        else:
            feature = Feature(name=feature_name, bow_model=self.bow_model)
            feature.add_attribute(self.r_D_text_set)
            self.bow_model = feature.bow_model
            self.features_fit.append(feature_name)

    def attach_feature_list(self, feature_list):
        """Attach feature to text objects in real Data set.

        Using feature interface for computing attributes and
        set feature values to text objects in real Data set.

        Use feature_list for attaching more than one feature.

        Parameters
        ----------
        feature_list : array, shape = [string feature1 name, string feature2
        name, ...]
            Contains the names of the corresponding features, that
            should be attached.
        """
        if self.real_data_size == 0:
            raise NoAnnotationException(self.raw_data.name)

        else:
            feature = Feature(name_list=feature_list, bow_model=self.bow_model)
            feature.add_attribute_list(self.r_D_text_set)
            self.bow_model = feature.bow_model

            for feature_name in feature_list:
                self.features_fit.append(feature_name)

"""
Analyzing data methods

Methods
-------
summarize_text()

summarize_textpair()
"""


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
    count_man_autos = 0
    count_man_autog = 0
    count_autos_autos = 0
    count_autog_autog = 0
    count_man_man = 0
    count_autos_autog = 0
    m_s = []
    m_g = []
    s_g = []
    s_s = []
    g_g = []
    m_m = []
    for textpair in data_set:
        # text_selected_list.append(select_anno(textpair))
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
        ###########################
        #### Man-All #########
        ###########################
        # if textpair.text1.category == "man" and textpair.text2.category == "man":
        #     text_selected_list.append(select_anno(textpair))

        ### all ###
        if textpair.text1.category == "man" and textpair.text2.category == "auto_schlecht":
            text_selected_list.append(select_anno(textpair))
            count_man_autos += 1
            m_s.append(select_anno(textpair))
            m_s.append(count0_1(textpair))
        elif textpair.text1.category == "man" and textpair.text2.category == "auto_gut":
            text_selected_list.append(select_anno(textpair))
            count_man_autog += 1
            m_g.append(select_anno(textpair))
            m_g.append(count0_1(textpair))
        elif textpair.text1.category == "man" and textpair.text2.category == "man":
            text_selected_list.append(select_anno(textpair))
            count_man_man += 1
            m_m.append(select_anno(textpair))
            m_m.append(count0_1(textpair))
        elif textpair.text1.category == "auto_schlecht" and textpair.text2.category == "man":
            text_selected_list.append(select_anno(textpair))
            count_man_autos += 1
            m_s.append(select_anno(textpair))
            m_s.append(count0_1(textpair))
        elif textpair.text1.category == "auto_gut" and textpair.text2.category == "man":
            text_selected_list.append(select_anno(textpair))
            count_man_autog += 1
            m_g.append(select_anno(textpair))
            m_g.append(count0_1(textpair))
        elif textpair.text1.category == "auto_schlecht" and textpair.text2.category == "auto_gut":
            text_selected_list.append(select_anno(textpair))
            count_autos_autog += 1
            s_g.append(select_anno(textpair))
            s_g.append(count0_1(textpair))
        elif textpair.text1.category == "auto_gut" and textpair.text2.category == "auto_schlecht":
            text_selected_list.append(select_anno(textpair))
            count_autos_autog += 1
            s_g.append(select_anno(textpair))
            s_g.append(count0_1(textpair))
        elif textpair.text1.category == "auto_schlecht" and textpair.text2.category == "auto_schlecht":
            text_selected_list.append(select_anno(textpair))
            count_autos_autos += 1
            s_s.append(select_anno(textpair))
            s_s.append(count0_1(textpair))
        elif textpair.text1.category == "auto_gut" and textpair.text2.category == "auto_gut":
            text_selected_list.append(select_anno(textpair))
            count_autog_autog += 1
            g_g.append(select_anno(textpair))
            g_g.append(count0_1(textpair))

    print "m_s",collections.Counter(m_s)
    print "m_g", collections.Counter(m_g)
    print "m_m", collections.Counter(m_m)
    print "s_g", collections.Counter(s_g)
    print "s_s", collections.Counter(s_s)
    print "g_g", collections.Counter(g_g)
    print "manull-auto_schlecht paare:", count_man_autos
    print "manull-auto_gut paare:", count_man_autog
    print "auto_schlecht-auto_schlecht paare:", count_autos_autos
    print "auto_gut-auto_gut paare:", count_autog_autog
    print "man-man paare:", count_man_man
    print "auto_schlecht_auto_gut paare", count_autos_autog

    print "auto", count_autos_autos+count_autos_autog+ count_man_autos+count_man_autos+ count_autog_autog
    print "man", count_man_autos+count_man_autos + count_man_man
    print "overall:", count_autos_autos+count_autos_autog+ count_man_autos+count_man_autog+ count_autog_autog+ count_man_man

    print "-------------Textpair-------------"
    # print collections.Counter(m_s)
    # print collections.Counter(m_g)
    # print collections.Counter(s_g)
    # print collections.Counter(s_s)
    # print collections.Counter(g_g)
    # print collections.Counter(m_m)

    printer(collections.Counter(text_selected_list))


def count0_1(textpair):
    if textpair.target == 0:
        return 0
    else:
        return 1


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
