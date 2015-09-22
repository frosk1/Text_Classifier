# -*- coding: utf-8 -*-
from text_classifier.attributes.attribute import Attribute
from text_classifier.parzu import *

__author__ = 'jan'


class PerfectTense(Attribute):

    def __init__(self):
        self._name = "perfect_tense"
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
            text.features["perfect_tense"] = self.count_perfect(text.id)

    def count_perfect(self, text_id):
        perf_count = 0
        for analyses in self.analyses_dict[text_id]:
            pattern = re.search("<-',\[mainclause,(\w+)_VAFIN,(\w+)_VVPP]", analyses)
            if pattern:
                s1 = pattern.group(1)
                s2 = pattern.group(2)
                pattern2 = re.search(".*" + s1 + "#(\d+).*" + s2 + "#(\d+).*", analyses)
                if pattern2:
                    if int(pattern2.group(2))-int(pattern2.group(1)) > 3:
                        perf_count += 1

        return perf_count
