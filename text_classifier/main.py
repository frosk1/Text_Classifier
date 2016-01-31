""" Main Module for Classification-System
"""
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '/home/jan/Development/Text_Classifier')

from time import time
from head.data import summarize_textpair
from body.korpus import Korpus
from head.data import Data
from model.model import Model


# Author Jan Wessling


def main():

    ZA = "/home/jan/Development/Korpus/ZA/Finales_Korpus/Text_Korpus_aktuell_marked.txt"
    Fball = "/home/jan/Development/Korpus/Fball/Finales_Korpus/Fussball_korpus_marked.txt"
    file_test = "/home/jan/Development/Text_Classifier/text_classifier/test_suitcase/test_korpus2.txt"
    file_test2 = "/home/jan/Development/Text_Classifier/text_classifier/test_suitcase/test_annotation2.txt"
    file_test2_2 ="/home/jan/Development/Text_Classifier/text_classifier/test_suitcase/test_annotation2_2.txt"
    file1 = "/home/jan/Development/Text_Classifier/text_classifier/test_suitcase/test_korpus.txt"
    file2 = "/home/jan/Development/Text_Classifier/text_classifier/test_suitcase/test_annotation.txt"
    file3 = "/home/jan/Development/Korpus/ZA/Annotation/annotation_regular_equal_Jan_Mel.txt"
    file4 = "/home/jan/Development/Korpus/ZA/Annotation/annotation_independent_350_Jan.txt"
    file5 = "/home/jan/Development/Korpus/ZA/Annotation/annotation_independent_350_Mel.txt"
    file6 = "/home/jan/Development/Korpus/ZA/Annotation/overall_annotation_80.txt"
    testmenge_ZA = "/home/jan/Development/Korpus/ZA/Annotation/testmenge400_ZA.txt"
    trainingsmenge_ZA = "/home/jan/Development/Korpus/ZA/Annotation/trainingsmenge600_ZA.txt"
    testmenge_Fball = "/home/jan/Development/Korpus/Fball/Annotation/testmenge200_Fball.txt"
    trainingsmenge_Fball = "/home/jan/Development/Korpus/Fball/Annotation/trainingsmenge500_Fball.txt"
    file6_test = "/home/jan/Development/Korpus/ZA/Annotation/overall_annotation_80_20pro.txt"
    file7 = "/home/jan/Development/Korpus/ZA/Annotation/overall_annotation_20.txt"
    file8 = "/home/jan/Development/Korpus/ZA/Annotation/overall_annotation_100.txt"
    file6_testing = "/home/jan/Development/Korpus/ZA/Annotation/auto_sample_geteilt/overall_annotation_80.txt"
    file10 = "/home/jan/Development/Korpus/Fball/Annotation/overall_annotation_100.txt"
    file11 = "/home/jan/Development/Korpus/Fball/Annotation/overall_annotation_818.txt"

    # manuelle_Annotation
    testmenge_ZA = "/home/jan/Development/Korpus/ZA/Annotation/testmenge400_ZA.txt"
    trainingsmenge_ZA = "/home/jan/Development/Korpus/ZA/Annotation/trainingsmenge600_ZA.txt"
    testmenge_Fball = "/home/jan/Development/Korpus/Fball/Annotation/testmenge200_Fball.txt"
    trainingsmenge_Fball = "/home/jan/Development/Korpus/Fball/Annotation/trainingsmenge600_Fball.txt"

    # train
    sampling_anno_auto_gut1_10k = "/home/jan/Development/Korpus/ZA/Annotation/auto_sample/sampling_anno_auto_gut1_10k.txt"
    sampling_anno_auto_gut2_10k = "/home/jan/Development/Korpus/ZA/Annotation/auto_sample/sampling_anno_auto_gut2_10k.txt"
    sampling_anno_auto_schlecht1_10k = "/home/jan/Development/Korpus/ZA/Annotation/auto_sample/sampling_anno_auto_schlecht1_10k.txt"
    sampling_anno_auto_schlecht2_10k = "/home/jan/Development/Korpus/ZA/Annotation/auto_sample/sampling_anno_auto_schlecht2_10k.txt"
    sampling_anno_man1_10k = "/home/jan/Development/Korpus/ZA/Annotation/auto_sample/sampling_anno_man1_10k.txt"
    sampling_anno_man_all = "/home/jan/Development/Korpus/ZA/Annotation/auto_sample/sampling_anno_man1.txt"
    sampling_anno_man2_10k = "/home/jan/Development/Korpus/ZA/Annotation/auto_sample/sampling_anno_man2_10k.txt"
    sampling_anno_man4_10k = "/home/jan/Development/Korpus/ZA/Annotation/auto_sample/sampling_anno_man4_10k.txt"
    sampling_anno_man_auto_gut_1_10k = "/home/jan/Development/Korpus/ZA/Annotation/auto_sample/sampling_anno_man_auto_gut_1_10k.txt"

    fball_sampling_anno_man1_10k = "/home/jan/Development/Korpus/Fball/Annotation/auto_sample/fball_sampling_anno_man1_10k.txt"
    fball_sampling_anno_man_auto_gut1 = "/home/jan/Development/Korpus/Fball/Annotation/auto_sample/fball_sampling_anno_man_auto_gut1.txt"
    fball_sampling_anno_man2 = "/home/jan/Development/Korpus/Fball/Annotation/auto_sample/fball_sampling_anno_man2.txt"
    fball_sampling_anno_auto_gut1_10k = "/home/jan/Development/Korpus/Fball/Annotation/auto_sample/fball_sampling_anno_auto_gut1_10k.txt"
    fball_sampling_anno_auto_gut2 = "/home/jan/Development/Korpus/Fball/Annotation/auto_sample/fball_sampling_anno_auto_gut2.txt"
    fball_sampling_anno_auto_schlecht1 = "/home/jan/Development/Korpus/Fball/Annotation/auto_sample/fball_sampling_anno_auto_schlecht1.txt"
    fball_sampling_anno_auto_schlecht2 = "/home/jan/Development/Korpus/Fball/Annotation/auto_sample/fball_sampling_anno_auto_schlecht2.txt"
    fball_sampling_anno_man4_10k = "/home/jan/Development/Korpus/Fball/Annotation/auto_sample/fball_sampling_man4_10k.txt"

    # test
    filter_anno_auto_gut_auto_schlecht = "/home/jan/Development/Korpus/ZA/Annotation/filter_anno/filter_anno_auto_gut_auto_schlecht.txt"
    filter_anno_auto_gut_man = "/home/jan/Development/Korpus/ZA/Annotation/filter_anno/filter_anno_auto_gut_man.txt"
    filter_anno_auto_schlecht_man = "/home/jan/Development/Korpus/ZA/Annotation/filter_anno/filter_anno_auto_schlecht_man.txt"
    filter_anno_man_auto_schlecht_auto_gut_auto_schlecht = "/home/jan/Development/Korpus/ZA/Annotation/filter_anno/Rfilter_anno_man_auto_schlecht_auto_gut_auto_schlecht.txt"
    filter_anno_never_same = "/home/jan/Development/Korpus/ZA/Annotation/filter_anno/filter_anno_never_same.txt"
    filter_anno_man_man = "/home/jan/Development/Korpus/ZA/Annotation/filter_anno/filter_anno_man_man.txt"
    filter_anno_JMequal_man_man = "/home/jan/Development/Korpus/ZA/Annotation/filter_anno/filter_anno_JMequal_man_man.txt"






    # Set Korpus
    k1 = Korpus("Test")
    k1.insert_from_file(Fball)

    # Set Data
    data1 = Data("train", k1)
    data1.add_anno(fball_sampling_anno_man1_10k)

    data2 = Data("test", k1)
    data2.add_anno(testmenge_Fball)

    datas = [data1, data2]

    # Attach Features

    # data1.attach_feature("bag_of_pos")
    # data1.attach_feature("bag_of_words")
    # data1.attach_feature("tf_idf")
    data1.attach_feature("readability")
    # data1.attach_feature("variety")
    # data1.attach_feature("adjective")
    # data1.attach_feature("sentence_start")
    # data1.attach_feature("modal_verb")
    # data1.attach_feature("perfect_tense")
    # data1.attach_feature("passive")


    # Shell output for detailed information of set data

    # training data
    print "+++++++++++ summarize " + data1.name + " data+++++++++++"+"\n"
    summarize_textpair(data1.real_data.values())
    # test data
    print "+++++++++++ summarize " + data2.name + " data+++++++++++" +"\n"
    summarize_textpair(data2.real_data.values())

    # Set Model
    model1 = Model(data_list=datas)
    # Set classifier
    model1.set_classifier("svm_linear")
    # Set train data
    model1.set_train_data(data1.name)
    # Set test data
    model1.set_test_data(data2.name)

    # Print Evaluation Report
    model1.evaluate_classification_report(100)


if __name__ == '__main__':
    x = time()
    main()
    y = time()
    print "--------------------------------"
    print "\n" + "Time needed :", y - x, "sec"
