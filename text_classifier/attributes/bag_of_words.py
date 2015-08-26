__author__ = 'jan'
'''
class BagOfWords :

'''
from text_classifier.attributes.attribute import Attribute
import re

class BagOfWords(Attribute):

    def __init__(self):
        self._name = "bag_of_words"
        self._data = None
        self.corpus = None
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
        BagOfWords.build_model(self.data,self.model)
        for i in self._data.values():

            temp_model = dict(self.model)
            for x in i.text1.tokenlist:
                if x in self.model.keys():
                    temp_model[x] += 1
            i.text1.features["bag_of_words"] = temp_model.values()

            temp_model = dict(self.model)
            for y in i.text2.tokenlist:
                if y in self.model.keys():
                    temp_model[y] += 1
            i.text2.features["bag_of_words"] = temp_model.values()


    @staticmethod
    def build_model(data, model):
        for i in data.values():
            for x in i.text1.tokenlist:
                if re.match("\w+",x):
                    model[x.lower()] = 0
            for y in i.text2.tokenlist:
                if re.match("\w+",y):
                    model[y.lower()] = 0
