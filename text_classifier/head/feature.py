"""
Feature class
"""

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

# Author Jan Wessling


class Feature(object):
    """
    Feature Interface

    Interface for communication between attribute classes and data class.

    Parameter
    ---------
    name : string, optional
        Contains the name of the feature, that should be attached.

    name_list : array, shape = [string feature name1, ...]
        Contains the names of the features, that should be attached.

    bow_model :  bow skeleton --> hash, shape = { string word : int 0 }
                 bop skeleton --> hash, shape = { string pos tag : int 0 }
        Contains bow or bop skeleton. Inital value is None.
    """

    def __init__(self, name=None, name_list=None, bow_model=None):
        self.name = name
        self.name_list = name_list
        self.bow_model = bow_model

    def init_attribute(self, attribute_name):
        """Create attribute instance

        Parameter
        ---------
        attribute_name : string
            Contains the feature name, to create an attribute
            instance.
        """
        if attribute_name == "bag_of_words":
            attribute = BagOfWords(self.bow_model)
            return attribute
        elif attribute_name == "tf_idf":
            attribute = TfIdf(self.bow_model)
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
        """ Attach feature value from one attribute

        Build attribute class and compute feature value. Attach
        feauture value to text objects in _text_set.

        Parameter
        ---------
        text_set : set
            Contains all unique text objects. Basis for Computation
            of feature values.
        """
        attribute = self.init_attribute(self.name)
        attribute._text_set = text_set
        attribute.compute()
        if self.name == "bag_of_words" or self.name == "bag_of_pos" or self.name == "tf_idf":
            self.bow_model = attribute.bow_model

    def add_attribute_list(self, text_set):
        """ Attach feature value from more than one attribute

        Build attribute class and compute feature value. Attach
        feauture value to text objects in _text_set.

        Parameter
        ---------
        text_set : set
            Contains all unique text objects. Basis for Computation
            of feature values.
        """
        for att_name in self.name_list:
            self.name = att_name
            self.add_attribute(text_set)
