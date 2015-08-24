from __builtin__ import staticmethod
from text_classifier.attributes.attribute import attribute
import abc
from text_classifier.attributes.standard_attribute import StandardAttribute

__author__ = 'jan'


'''
Class Feature :

Interface for communication between data and attributes

'''

class Feature(object):
    __metaclass__ = abc.ABCMeta

    @staticmethod
    def init_attribute(attribute_name):
        if attribute_name == "standard_attribute":
            attribute = StandardAttribute()
            return attribute

    @staticmethod
    def add_attribute(attribute_name, data):
        attribute = Feature.init_attribute(attribute_name)
        attribute._data = data
        attribute.compute()
        return attribute._data

    @staticmethod
    def add_attribute_list(attribute_list, data):
        # Todo Implment call from list. <>
        pass