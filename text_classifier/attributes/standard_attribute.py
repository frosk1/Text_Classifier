__author__ = 'jan'
'''
Test Class :

'''
from text_classifier.attributes.attribute import Attribute
from random import randint


class StandardAttribute(Attribute):

    def __init__(self):
        self._name = "standard_attribute"
        self._data = None

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
        for i in self.data.keys():
            self.data[i].text1.features["standard_attribute"] = randint(0, 1)
            self.data[i].text2.features["standard_attribute"] = randint(0, 1)
