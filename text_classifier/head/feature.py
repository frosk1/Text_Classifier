from __builtin__ import staticmethod
from text_classifier.attributes.bag_of_words import BagOfWords
from text_classifier.attributes.tf_idf import TfIdf
from text_classifier.exceptions import FeatureNotExistException
__author__ = 'jan'


'''
Class Feature :

Interface for communication between data and attributes

'''


class Feature(object):

    @staticmethod
    def init_attribute(attribute_name):
        if attribute_name == "bag_of_words":
            attribute = BagOfWords()
            return attribute
        elif attribute_name == "tf_idf":
            attribute = TfIdf()
            return attribute
        else:
            raise FeatureNotExistException(attribute_name)

    @staticmethod
    def add_attribute(attribute_name, data):
        attribute = Feature.init_attribute(attribute_name)
        attribute._data = data
        attribute.compute()
        return attribute._data

    @staticmethod
    def add_attribute_list(attribute_list, data):
        for att_name in attribute_list:
            data = Feature.add_attribute(att_name, data)
        return data
