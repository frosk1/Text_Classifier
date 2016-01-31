"""
Test suits for the text-classification-system
"""

from text_classifier.test_suitcase.test_case import *

# Author Jan Wessling


class TestSuits(object):
    """
    Test Suits

    Loading test cases from test_case.py into test suits.

    Parameters
    ----------
    test_name : string, optional
        Containing the name of the used system test.

    Attributes
    ----------
    test_dict : hash, shape = {string test name : array}
        Containing predefined test structures for the system.
        array, shape : [TestCase1, TestCase2, ...]

    test_case_list : array, shape = [string test name1, ...]
        Containing all names of the predefined test structures.

    test_load : unittest.TestLoader object
        TestLoader is responsible for loading test cases in a
        TestSuit

    test_runner : unittest.TextTestRunner object
        TextTestRunner displays test results in a textual form.

    _selected_test_list : array, shape = [loaded testcase1, ...]
        Contains all loaded testCases from the test_dict.
    """

    def __init__(self, test_name=None):
        self.test_name = test_name
        self.test_dict = {"system_test": [TextTest, TextPairTest, KorpusTest,
                                          DataTest, BagOfWordsTest, TfIdfTest, ModelTest],
                          "attribute_test": [BagOfWordsTest, TfIdfTest, ReadabilityTest, VarietyTest],
                          "raw_data_test": [TextTest, KorpusTest],
                          "real_data_test": [TextPairTest, DataTest],
                          "model_test": [ModelTest],
                          "variety_test": [VarietyTest]
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
