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
from text_classifier.attributes.bag_of_pos import BagOfPos
from text_classifier.attributes.modal import ModalVerb
from text_classifier.attributes.sentence_start import SentenceStart

__author__ = 'jan'


'''
Class Feature :

Interface for communication between data and attributes

'''


class Feature(object):

    def __init__(self, name=None, name_list=None, bow_model=None):
        self.name = name
        self.name_list = name_list
        self.bow_model = bow_model

    def init_attribute(self, attribute_name):
        if attribute_name == "bag_of_words":
            attribute = BagOfWords(self.bow_model)
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
        elif attribute_name == "sentence_start":
            attribute = SentenceStart()
            return attribute
        elif attribute_name == "bag_of_pos":
            attribute = BagOfPos(self.bow_model)
            return attribute
        elif attribute_name == "modal_verb":
            attribute = ModalVerb()
            return attribute
        else:
            raise FeatureNotExistException(attribute_name)

    def add_attribute(self, text_set):
        attribute = self.init_attribute(self.name)
        attribute._text_set = text_set
        attribute.compute()
        if self.name == "bag_of_words" or self.name == "bag_of_pos":
            self.bow_model = attribute.bow_model

    def add_attribute_list(self, text_set):
        for att_name in self.name_list:
            self.name = att_name
            self.add_attribute(text_set)