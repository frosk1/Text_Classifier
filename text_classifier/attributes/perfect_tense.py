# -*- coding: utf-8 -*-
from text_classifier.attributes.attribute import Attribute
import treetaggerwrapper

__author__ = 'jan'


class PerfectTense(Attribute):

    def __init__(self):
        self._name = "perfect_tense"
        self._text_set = None
        self.perf_count = dict()
        self.tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
        self.perf_tag_list = [u"VVPP", u"VMPP", u"VAPP"]

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
        for text in self._text_set:

            self.perf_count[text.id] = 0
            tags = treetaggerwrapper.make_tags(self.tagger.tag_text(text.text.decode("utf-8")))

            for tuple_tag in tags:
                print tuple_tag
                if tuple_tag[1] in self.perf_tag_list:
                    self.perf_count[text.id] += 1

            text.features["perfect_tense"] = self.perf_count[text.id]



