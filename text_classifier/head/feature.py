from __builtin__ import staticmethod

__author__ = 'jan'

from text_classifier.attributes.standard_attribute import StandardAttribute

'''
Class Feature :

Interface for communication between data and attributes

'''

class Feature(object):

    def __init__(self, anno_data, attribute_list=None):
        self.anno_data = anno_data
        self.attribute_list = attribute_list

    @staticmethod
    def init_attribute(attribute_name):
        if attribute_name == "standard_attribute":
            attribute = StandardAttribute()
            return attribute

    def add_attribute(self, attribute_name):
        attribute = Feature.init_attribute(attribute_name)
        attribute._data = self.anno_data
        attribute.compute()
        self.anno_data = attribute._data