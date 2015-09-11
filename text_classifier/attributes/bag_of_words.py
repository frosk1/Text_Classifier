from text_classifier.attributes.attribute import Attribute
import re
import collections
__author__ = 'jan'
'''
class BagOfWords :

'''


class BagOfWords(Attribute):

    def __init__(self):
        self._name = "bag_of_words"
        self._text_set = None
        self.model = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def text_set(self):
        return self._text_set

    @text_set.setter
    def text_set(self, new_value):
        self._text_set = new_value

    def compute(self):
        self.build_model()

        for text in self._text_set:
            # for test_case ''' test__bag_of_words__compute ''' use the OrderedDict
            # to check the values with the term_frequency in test_suitcase.resource
            #
            # temp_model = collections.OrderedDict(sorted(self.model.items()))

            temp_model = dict(self.model)
            for word in text.wordlist_lower:
                try:
                    temp_model[word] += 1
                except KeyError:
                    continue

            text.features["bag_of_words"] = temp_model.values()

    def build_model(self):
        for text in self._text_set:
            for word in text.wordlist_lower:
                self.model[word] = 0
