from text_classifier.test_suitcase.test_case import *
__author__ = 'jan'


class TestSuits(object):

    def __init__(self, test_name=None):
        self.test_name = test_name
        self.test_dict = {"system_test": [TextTest, TextPairTest, KorpusTest,
                                          DataTest, BagOfWordsTest, TfIdfTest, ModelTest],
                          "attribute_test": [BagOfWordsTest, TfIdfTest],
                          "raw_data_test": [TextTest, KorpusTest],
                          "real_data_test": [TextPairTest, DataTest],
                          "model_test": [ModelTest]
                          }
        self.test_case_list = self.test_dict.keys()
        self.test_load = unittest.TestLoader()
        self.test_runner = unittest.TextTestRunner()
        self._selected_test_list = self.load_test_case_list()

    def load_test_case_list(self):
        case_list = []
        try:
            for testCase in self.test_dict[self.test_name]:
                test_suite = self.test_load.loadTestsFromTestCase(testCase)
                case_list.append(test_suite)
            return case_list
        except KeyError:
            print "Test" + str(self.test_name) + "does not exist."
            print "Lookup tests in test_case_list."

    def run_test(self):
        test_suit = unittest.TestSuite(self._selected_test_list)
        self.test_runner.run(test_suit)
