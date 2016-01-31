# -*- coding: utf-8 -*-
"""
Test Case Modul

Definition of all test cases for the text-classificaion-system.
"""

from text_classifier.body.korpus import Korpus
from text_classifier.head.data import Data
from text_classifier.attributes.bag_of_words import BagOfWords
from text_classifier.attributes.tf_idf import TfIdf
from text_classifier.model.model import Model
from text_classifier.attributes.readability import Readability
from text_classifier.attributes.variety_count import Variety
import numpy as np
import unittest
import collections
import resource as res

# Author Jan Wessling


class TestBodyModel(unittest.TestCase):
    def setUp(self):
        self.korpus_file = res.korpus_file
        self.anno_file = res.anno_file
        self.test_korpus = Korpus("Test")
        self.test_korpus.insert_from_file(self.korpus_file)
        self.test_data = Data(self.test_korpus)
        self.test_data.add_anno(self.anno_file)
        self.test_data.attach_feature_list(res.feature_list)


class TestBodyKorpus(unittest.TestCase):
    def setUp(self):
        self.korpus_file = res.korpus_file


class TestBodyText(unittest.TestCase):
    def setUp(self):
        self.korpus_file = res.korpus_file
        self.anno_file = res.anno_file
        self.test_korpus = Korpus("Test")
        self.test_korpus.insert_from_file(self.korpus_file)
        self.test_data = Data(self.test_korpus)
        self.test_data.add_anno(self.anno_file)
        self.test_data.attach_feature("bag_of_words")


class TestBodyTextpair(unittest.TestCase):
    def setUp(self):
        self.korpus_file = res.korpus_file
        self.anno_file = res.anno_file
        self.test_korpus = Korpus("Test")
        self.test_korpus.insert_from_file(self.korpus_file)
        self.test_data = Data(self.test_korpus)
        self.test_data.add_anno(self.anno_file)
        self.test_data.attach_feature("tf_idf")


class TestBodyData(unittest.TestCase):
    def setUp(self):
        self.korpus_file = res.korpus_file
        self.anno_file = res.anno_file
        self.test_korpus = Korpus("Test")
        self.test_korpus.insert_from_file(self.korpus_file)


class TestBodyAttribute(unittest.TestCase):
    def setUp(self):
        self.korpus_file = res.korpus_file
        self.anno_file = res.anno_file
        self.test_korpus = Korpus("Test")
        self.test_korpus.insert_from_file(self.korpus_file)
        self.test_data = Data(self.test_korpus)
        self.test_data.add_anno(self.anno_file)



##################################################################################################################
##################################################################################################################


class TextTest(TestBodyText):
    @classmethod
    def setUpClass(cls):
        print "###################### Begin Testing Text Class ######################" + "\n"

    @classmethod
    def tearDownClass(cls):
        print "\n" + "###################### End Testing Text Class ######################"

    def setUp(self):
        test_name = self.shortDescription()
        super(TextTest, self).setUp()
        self.mock_obj_set = set()
        for textpair in self.test_data.real_data.values():
            self.mock_obj_set.add(textpair.text1)
            self.mock_obj_set.add(textpair.text2)

        if test_name == "Test routine vectorize() in textpair":
            print "setting up for testing vectorize()"
            self.term_freq = res.term_frequency

    def tearDown(self):
        test_name = self.shortDescription()
        self.korpus_file = None
        self.anno_file = None
        self.test_korpus = None
        self.test_data = None
        self.mock_obj_set = None

        if test_name == "Test routine vectorize() in textpair":
            print "cleaning up for testing vectorize()"
            self.term_freq = None
            print "--------------------------------------------------------------"

    def test__text__vectorize(self):
        """ Test routine vectorize() in textpair """
        for mock_obj in self.mock_obj_set:
            mock_obj.vectorize()
            self.assertListEqual(mock_obj.feature_vector, self.term_freq[mock_obj.id])


class TextPairTest(TestBodyTextpair):
    @classmethod
    def setUpClass(cls):
        print "###################### Begin Testing Textpair Class ######################" + "\n"

    @classmethod
    def tearDownClass(cls):
        print "\n" + "###################### End Testing Textpair Class ######################"

    def setUp(self):
        test_name = self.shortDescription()
        super(TextPairTest, self).setUp()
        self.mock_obj_list = self.test_data.real_data.values()

        if test_name == "Test routine vectorize() in textpair":
            print "setting up for testing vectorize()"
            self.tf_idf_difference = res.tf_idf_difference

        elif test_name == "Test routine iter_feature_values() in textpair":
            print "setting up for testing iter_feature_values()"
            self.term_freq = res.tf_idf_weight

    def tearDown(self):
        test_name = self.shortDescription()
        self.korpus_file = None
        self.anno_file = None
        self.test_korpus = None
        self.test_data = None
        self.mock_obj_list = None

        if test_name == "Test routine vectorize() in textpair":
            print "cleaning up for testing vectorize()"
            self.tf_idf_difference = None
            print "--------------------------------------------------------------"

        elif test_name == "Test routine iter_feature_values() in textpair":
            print "cleaning up for testing iter_feature_values()"
            self.term_freq = None
            print "--------------------------------------------------------------"

    def test__textpair__vectorize(self):
        """ Test routine vectorize() in textpair """
        for mock_obj in self.mock_obj_list:
            mock_obj.vectorize()
            self.assertListEqual(mock_obj.feature_vector, self.tf_idf_difference[mock_obj.name])

    def test__textpair__iter_feature_values(self):
        """ Test routine iter_feature_values() in textpair """
        for mock_obj in self.mock_obj_list:
            index = 0
            for feature_value1, feature_value2 in mock_obj.iter_feature_values():
                self.assertEqual(feature_value1, self.term_freq[mock_obj.text1.id][index])
                self.assertEqual(feature_value2, self.term_freq[mock_obj.text2.id][index])
                index += 1


class KorpusTest(TestBodyKorpus):
    @classmethod
    def setUpClass(cls):
        print "###################### Begin Testing Korpus Class ######################" + "\n"

    @classmethod
    def tearDownClass(cls):
        print "\n" + "###################### End Testing Korpus Class ######################"

    def setUp(self):
        print "setting up for testing insert_from_file()"
        super(KorpusTest, self).setUp()
        self.mock_obj = Korpus("test_korpus")
        self.mock_obj.insert_from_file(self.korpus_file)
        self.korpus_dic = res.korpus_dic

    def tearDown(self):
        print "cleaning up for testing insert_from_file()"
        self.korpus_file = None
        print "--------------------------------------------------------------"

    def test__korpus__insert_from_file(self):
        """ Test routine insert_from_file() in Korpus """

        for texts in self.mock_obj.content.values():
            self.assertEqual(texts.text, self.korpus_dic[texts.id])


class DataTest(TestBodyData):
    @classmethod
    def setUpClass(cls):
        print "###################### Begin Testing Data Class ######################" + "\n"

    @classmethod
    def tearDownClass(cls):
        print "\n" + "###################### End Testing Data Class ######################"

    def setUp(self):
        test_name = self.shortDescription()
        super(DataTest, self).setUp()
        self.mock_obj = Data(self.test_korpus)
        self.mock_obj.add_anno(self.anno_file)

        if test_name == "Test routine add_anno() in Data":
            print "setting up for testing add_anno()"
            self.textpair_dic = res.textpair_dic

        elif test_name == "Test routine attach_feature() in Data":
            print "setting up for testing attach_feature()"
            self.feature_name = "bag_of_words"

        elif test_name == "Test routine attach_feature_list() in Data":
            print "setting up for testing attach_feature_list()"
            self.feature_list = res.feature_list

    def tearDown(self):
        test_name = self.shortDescription()
        self.korpus_file = None
        self.anno_file = None
        self.test_korpus = None
        self.mock_obj = None

        if test_name == "Test routine add_anno() in Data":
            print "cleaning up for testing add_anno()"
            self.textpair_dic = None
            print "--------------------------------------------------------------"

        elif test_name == "Test routine attach_feature() in Data":
            print "cleaning up for testing attach_feature()"
            self.feature_name = None
            print "--------------------------------------------------------------"

        elif test_name == "Test routine attach_feature_list() in Data":
            print "cleaning up for testing attach_feature_list()"
            self.feature_list = None
            print "--------------------------------------------------------------"

    def test__data__add_anno(self):
        """ Test routine add_anno() in Data """

        self.assertEqual(self.mock_obj.real_data_size, 15)
        self.assertEqual(sorted(self.mock_obj.real_data.keys()), sorted(self.textpair_dic.keys()))

        for textpair_name in self.mock_obj.real_data.keys():
            self.assertEqual(self.mock_obj.real_data[textpair_name].target, self.textpair_dic[textpair_name])

    def test__data__attach_feature(self):
        """ Test routine attach_feature() in Data """

        self.mock_obj.attach_feature("bag_of_words")
        for textpair in self.mock_obj.real_data.values():
            self.assertEqual(textpair.text1.features.keys()[0], self.feature_name)
            self.assertEqual(textpair.text2.features.keys()[0], self.feature_name)

    def test__data__attach_feature_list(self):
        """ Test routine attach_feature_list() in Data """

        self.mock_obj.attach_feature_list(self.feature_list)
        for textpair in self.mock_obj.real_data.values():
            self.assertItemsEqual(textpair.text1.features.keys(), self.feature_list)
            self.assertItemsEqual(textpair.text2.features.keys(), self.feature_list)


class BagOfWordsTest(TestBodyAttribute):
    @classmethod
    def setUpClass(cls):
        print "###################### Begin Testing BagOfWords Class ######################" + "\n"

    @classmethod
    def tearDownClass(cls):
        print "\n" + "###################### End Testing BagOfWords Class ######################"

    def setUp(self):
        test_name = self.shortDescription()
        self.token_list = res.token_list
        super(BagOfWordsTest, self).setUp()

        if test_name == "Test routine build_model() in BagOfWords":
            print "setting up for testing build_model()"
            self.mock_obj = BagOfWords()
            self.mock_obj._text_set = self.test_data.r_D_text_set
            self.mock_obj.build_model()

        elif test_name == "Test routine compute() in BagOfWords":
            print "setting up for testing compute()"

            self.test_data.attach_feature("bag_of_words")
            self.term_freq = res.term_frequency

    def tearDown(self):
        test_name = self.shortDescription()

        self.korpus_file = None
        self.anno_file = None
        self.test_korpus = None
        self.test_data = None
        self.token_list = None

        if test_name == "Test routine build_model() in BagOfWords":
            print "cleaning up for testing build_model()"
            self.mock_obj = None
            print "--------------------------------------------------------------"

        elif test_name == "Test routine compute() in BagOfWords":
            print "cleaning up for testing compute()"
            self.term_freq = None
            print "--------------------------------------------------------------"

    def test__bag_of_words__build_model(self):
        """ Test routine build_model() in BagOfWords """

        self.assertListEqual(sorted(self.token_list), sorted(self.mock_obj.model.keys()))

    def test__bag_of_words__compute(self):
        """ Test routine compute() in BagOfWords """

        for textpair in self.test_data.real_data.values():
            self.assertListEqual(textpair.text1.features["bag_of_words"], self.term_freq[textpair.text1.id])
            self.assertListEqual(textpair.text2.features["bag_of_words"], self.term_freq[textpair.text2.id])


class TfIdfTest(TestBodyAttribute):
    @classmethod
    def setUpClass(cls):
        print "#################### Begin Testing TfIdf Class ####################" + "\n"

    @classmethod
    def tearDownClass(cls):
        print "\n" + "###################### End Testing TfIdf Class ######################"

    def setUp(self):
        test_name = self.shortDescription()
        super(TfIdfTest, self).setUp()
        self.mock_obj = TfIdf()
        self.mock_obj._text_set = self.test_data.r_D_text_set
        self.token_list = res.token_list
        self.mock_obj.build_model()

        if test_name == "Test routine build_model() in TfIdf":
            print "setting up for testing  build_model()"

        elif test_name == "Test routine build_df_model() in TfIdf":
            print "setting up for testing  build_df_model()"
            self.document_frequency = res.document_frequency

        elif test_name == "Test routine build_tf_model() in TfIdf":
            print "setting up for testing  build_tf_model()"
            self.term_frequency = res.term_frequency

        elif test_name == "Test routine build_tf_idf_model()/compute() in TfIdf":
            print "setting up for testing  compute()/build_tf_idf_model()"
            self.test_data.attach_feature("tf_idf")
            self.tf_idf_weight = res.tf_idf_weight

    def tearDown(self):
        test_name = self.shortDescription()
        self.korpus_file = None
        self.anno_file = None
        self.test_korpus = None
        self.test_data = None
        self.token_list = None
        self.mock_obj = None

        if test_name == "Test routine build_model() in TfIdf":
            print "cleaning up for testing  build_model()"
            print "--------------------------------------------------------------"

        elif test_name == "Test routine build_df_model() in TfIdf":
            print "cleaning up for testing  build_df_model()"
            print "--------------------------------------------------------------"
            self.document_frequency = None

        elif test_name == "Test routine build_tf_model() in TfIdf":
            print "cleaning up for testing  build_tf_model()"
            print "--------------------------------------------------------------"
            self.term_frequency = None

        elif test_name == "Test routine build_tf_idf_model()/compute() in TfIdf":
            print "cleaning up for testing  compute()/build_tf_idf_model()"
            print "--------------------------------------------------------------"
            self.tf_idf_weight = None

    def test__tf_idf__build_model(self):
        """ Test routine build_model() in TfIdf """

        self.assertListEqual(sorted(self.token_list), sorted(self.mock_obj.model.keys()))

    def test__tf_idf__build_df_model(self):
        """ Test routine build_df_model() in TfIdf """

        df_model = collections.OrderedDict(sorted(self.mock_obj.build_df_model().items()))
        self.assertListEqual(df_model.values(), self.document_frequency)

    def test__tf_idf__build_tf_model(self):
        """ Test routine build_tf_model() in TfIdf """

        for text in self.mock_obj.text_set:
            tf_model = collections.OrderedDict(sorted(self.mock_obj.build_tf_model(text.tokenlist).items()))
            self.assertListEqual(tf_model.values(), self.term_frequency[text.id])

    def test__tf_idf__compute(self):
        """ Test routine build_tf_idf_model()/compute() in TfIdf """

        for textpair in self.test_data.real_data.values():
            self.assertListEqual(textpair.text1.features["tf_idf"], self.tf_idf_weight[textpair.text1.id])
            self.assertListEqual(textpair.text2.features["tf_idf"], self.tf_idf_weight[textpair.text2.id])


class ReadabilityTest(TestBodyAttribute):
    @classmethod
    def setUpClass(cls):
        print "#################### Begin Testing Readability Class ####################" + "\n"

    @classmethod
    def tearDownClass(cls):
        print "\n" + "###################### End Testing Readability Class ######################"

    def setUp(self):
        test_name = self.shortDescription()
        self.readability_index = res.readability_index
        super(ReadabilityTest, self).setUp()

        if test_name == "Test routine compute() in Model":
            print "setting up for testing  compute()"
            self.mock_obj = Readability()
            self.mock_obj._text_set = self.test_data.r_D_text_set
            self.test_data.attach_feature("readability")

    def tearDown(self):
        test_name = self.shortDescription()
        self.korpus_file = None
        self.anno_file = None
        self.test_korpus = None
        self.test_data = None
        self.readability_index = None

        if test_name == "Test routine compute() in Model":
            print "cleaning up for testing  compute()"
            self.mock_obj = None
            print "--------------------------------------------------------------"

    def test__Readability__compute(self):
        """ Test routine compute() in Model """
        for text in self.test_data.r_D_text_set:
            self.assertEqual(round(text.features["readability"], 10), self.readability_index[text.id])


class VarietyTest(TestBodyAttribute):
    @classmethod
    def setUpClass(cls):
        print "#################### Begin Testing Variety Class ####################" + "\n"

    @classmethod
    def tearDownClass(cls):
        print "\n" + "###################### End Testing Variety Class ######################"

    def setUp(self):
        test_name = self.shortDescription()
        self.variety = res.variety_dic
        super(VarietyTest, self).setUp()

        if test_name == "Test routine compute() in Model":
            print "setting up for testing  compute()"
            self.mock_obj = Variety()
            self.mock_obj._text_set = self.test_data.r_D_text_set
            self.test_data.attach_feature("variety")

    def tearDown(self):
        test_name = self.shortDescription()
        self.korpus_file = None
        self.anno_file = None
        self.test_korpus = None
        self.test_data = None
        self.variety = None

        if test_name == "Test routine compute() in Model":
            print "cleaning up for testing  compute()"
            self.mock_obj = None
            print "--------------------------------------------------------------"

    def test__Readability__compute(self):
        """ Test routine compute() in Model """
        for text in self.test_data.r_D_text_set:
            self.assertEqual(text.features["variety"],self.variety[text.id])


class ModelTest(TestBodyModel):
    @classmethod
    def setUpClass(cls):
        print "#################### Begin Testing Model Class ####################" + "\n"

    @classmethod
    def tearDownClass(cls):
        print "\n" + "###################### End Testing Model Class ######################"

    def setUp(self):
        test_name = self.shortDescription()
        super(ModelTest, self).setUp()
        self.mock_obj = Model(self.test_data)

        if test_name == "Test routine fill_feature_target() in Model":
            self.term_freq = res.term_frequency
            print "setting up for testing fill_feature_target()"

        elif test_name == "Test routine evaluate_cross_validation() in Model":
            self.mock_obj.set_classifier("svm_linear")
            self.accuracy = res.accuracy_svm_bag_of_words
            self.accuracy_mean = res.accuracy_svm_bag_of_words_mean
            print "setting up for testing evaluate_cross_validation()"

    def tearDown(self):
        test_name = self.shortDescription()
        self.korpus_file = None
        self.anno_file = None
        self.test_korpus = None
        self.test_data = None
        self.mock_obj = None

        if test_name == "Test routine fill_feature_target() in Model":
            print "cleaning up for testing fill_feature_target()"
            self.term_freq = None
            print "--------------------------------------------------------------"

        elif test_name == "Test routine evaluate_cross_validation() in Model":
            self.accuracy = None
            self.accuracy_mean = None

            print "cleaning up for testing evaluate_cross_validation()"
            print "--------------------------------------------------------------"

    def test__model__fill_feature_target(self):
        """ Test routine fill_feature_target() in Model """
        for index in range(len(self.test_data.real_data.values())):
            reference = np.array(self.test_data.real_data.values()[index])
            (self.mock_obj.feature_samples[index] == reference).all()

    def test__model__evaluate_cross_validation(self):
        """ Test routine evaluate_cross_validation() in Model """
        acc_list, acc_mean = self.mock_obj.evaluate_cross_validation(10)
        self.assertListEqual(self.accuracy, acc_list)
        self.assertEqual(self.accuracy_mean, acc_mean)


if __name__ == '__main__':
    unittest.main()
