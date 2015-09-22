# -*- coding: utf-8 -*-
from text_classifier.parzu import *
from text_classifier.attributes.attribute import Attribute
__author__ = 'jan'


class Passive(Attribute):

    def __init__(self):
        self._name = "passive"
        self._text_set = None
        self.analyses_list = None
        self.id_len_tuples = None
        self.analyses_dict = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def text_set(self):
        return self._text_set

    @text_set.setter
    def text_set(self, new_value):
        self._text_set = new_value

    def compute(self):
        self.id_len_tuples, self.analyses_list = parse_analyses(self._text_set)
        self.analyses_dict = fill_analyses_dict(self.id_len_tuples, self.analyses_list)

        for text in self._text_set:
            text.features["passive"] = self.count_passive(text.id)

    def count_passive(self, text_id):
        count = 0
        for analyses in self.analyses_dict[text_id]:
            if "passive" in analyses:
                count += 1
        return count
