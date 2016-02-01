""" Main Module for Classification-System

Usage :


Change the path to your Text_Classifier folder

    sys.path.insert(0, '/path to your Text_Classifier folder/Text_Classifier')

Use the classification system in the main method.
    1. Set Korpus
    2. Set Data
    3. Attach Features
    4. Set Model
    5. Start Classification with Report

"""

import sys
sys.path.insert(0, '/home/jan/Development/Text_Classifier')
from time import time
from head.data import summarize_textpair
from body.korpus import Korpus
from head.data import Data
from model.model import Model
import ressource_path as res

# Author Jan Wessling


def main():
    print "Starting Text Classification System" + "\n"

    # Set Korpus
    k1 = Korpus("Test")
    k1.insert_from_file(res.Fball)

    # Set Data
    data1 = Data("train", k1)
    data1.add_anno(res.fball_sampling_anno_man1_10k)

    data2 = Data("test", k1)
    data2.add_anno(res.testmenge_Fball)

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
    print "+++++++++++ summarize " + data1.name + " data+++++++++++" + "\n"
    summarize_textpair(data1.real_data.values())
    # test data
    print "+++++++++++ summarize " + data2.name + " data+++++++++++" + "\n"
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
