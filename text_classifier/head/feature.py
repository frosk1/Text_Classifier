from __builtin__ import staticmethod
from text_classifier.attributes.bag_of_words import BagOfWords
from text_classifier.attributes.tf_idf import TfIdf
from text_classifier.attributes.readability import Readability
from text_classifier.attributes.variety_count import Variety
from text_classifier.attributes.perfect_tense import PerfectTense
from text_classifier.attributes.nested_sentence import NestedSentence
from text_classifier.attributes.passive import Passive
from text_classifier.attributes.adjective import Adjective
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
        elif attribute_name == "readability":
            attribute = Readability()
            return attribute
        elif attribute_name == "variety":
            attribute = Variety()
            return attribute
        elif attribute_name == "perfect_tense":
            attribute = PerfectTense()
            return attribute
        elif attribute_name == "nested_sentence":
            attribute = NestedSentence()
            return attribute
        elif attribute_name == "passive":
            attribute = Passive()
            return attribute
        elif attribute_name == "adjective":
            attribute = Adjective()
            return attribute
        else:
            raise FeatureNotExistException(attribute_name)

    @staticmethod
    def add_attribute(attribute_name, text_set):
        attribute = Feature.init_attribute(attribute_name)
        attribute._text_set = text_set
        attribute.compute()

    @staticmethod
    def add_attribute_list(attribute_list, text_set):
        for att_name in attribute_list:
            Feature.add_attribute(att_name, text_set)
