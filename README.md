Text_Classifier
=============

GitHub: https://github.com/frosky/Text_Classifier


About
=====

This text classification system was build in the course of the Bachelorarbeit
"Entwicklung eines schwach überwachten Modells zur Bewertung von automatisch
generierten Texten" from Jan Wessling. The system classifies textpair objects
from a developed corpus. A textpair was annotated by the text quaility of its
inner text objects. A classification tries to predict the highly subjective choice
of Text quality. The system is able to deal with different data structures
to ensure an easy to use classification mechanism. All classification
algorithms are part of the scikit-learn python modul.

See reference : https://github.com/scikit-learn/scikit-learn

Requirements-Python
============
-  Python 2.7.x 
-  Numpy 1.9.2
-  Scipy 0.14.1
-  scikit-learn 0.17
-  nltk 3.1 
-  pyphen 0.9.2

Other Requirements
============
POS-Tagger from Helmut Schmid(1994) : http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/tree-tagger1.pdf

Dependency-Parser from Sennrich et al.(2009) : https://files.ifi.uzh.ch/CL/volk/papers/Sennrich_Schneider_Volk_Warin_Pro3Gres_GSCL.pdf



-  ParZu - Dpendency Parser : https://github.com/rsennrich/parzu
-  Treetagger ; Helmut Schmid http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/
-  treetaggerwrapper for python ; http://treetaggerwrapper.readthedocs.org/en/latest/

Use System
============
First change the needed file paths in main.py and ressource_path.py. After that your whole system is build in main()
of the main.py.

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
