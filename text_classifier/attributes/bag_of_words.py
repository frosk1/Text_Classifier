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
        self._data = None
        self.text_set = set()
        self.model = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        self._data = new_value

    def compute(self):
        self.build_model()

        for text in self.text_set:
            temp_model = collections.OrderedDict(sorted(self.model.items()))

            for token in text.tokenlist:
                if token.lower() in self.model.keys():
                    temp_model[token.lower()] += 1

            text.features["bag_of_words"] = temp_model.values()

    def build_model(self):

        for textpair in self._data.values():
            self.text_set.add(textpair.text1)
            self.text_set.add(textpair.text2)

        for text in self.text_set:
            for token in text.tokenlist:
                if re.match("\w+", token) and token not in self.model.keys():
                    self.model[token.lower()] = 0
