from __builtin__ import staticmethod
from text_classifier.attributes.standard_attribute import StandardAttribute
from text_classifier.attributes.bag_of_words import BagOfWords

__author__ = 'jan'


'''
Class Feature :

Interface for communication between data and attributes

'''


class Feature(object):

    @staticmethod
    def init_attribute(attribute_name):
        if attribute_name == "standard_attribute":
            attribute = StandardAttribute()
            return attribute
        elif attribute_name == "bag_of_words":
            attribute = BagOfWords()
            return attribute
        else:
            print "Feature does not exist."

    @staticmethod
    def add_attribute(attribute_name, data):
        attribute = Feature.init_attribute(attribute_name)
        attribute._data = data
        attribute.compute()
        return attribute._data

    @staticmethod
    def add_attribute_list(attribute_list, data):
        # Todo Implement call from list. <>
        pass