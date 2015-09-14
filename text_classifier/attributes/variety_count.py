# -*- coding: utf-8 -*-
from text_classifier.attributes.attribute import Attribute
import re
import collections
from nltk.corpus import stopwords
__author__ = 'jan'


class Variety(Attribute):

    def __init__(self):
        self._name = "variety"
        self._text_set = None
        self.stopwords = stopwords.words("german")

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
        var_count = dict()
        for text in self._text_set:
            var_count[text.id] = 0

            if len(text.sentencelist) > 1:
                for i in range(len(text.sentencelist)):

                    try:
                        words = re.findall(r'\w+', (text.sentencelist[i] + text.sentencelist[i + 1]), re.UNICODE)
                        c = collections.Counter(words)
                        for x in c.keys():
                            if x.lower() in self.stopwords:
                                c.pop(x)
                            else:
                                if c[x] > 1:
                                    var_count[text.id] += 1

                        text.features["variety"] = var_count[text.id]

                    except IndexError:
                        continue

            else:
                words = re.findall(r'\w+', text.sentencelist[0], re.UNICODE)
                c = collections.Counter(words)
                for x in c.keys():
                    if x.lower() in self.stopwords:
                        c.pop(x)
                    else:
                        if c[x] > 1:
                            var_count[text.id] += 1

                text.features["variety"] = var_count[text.id]
        print var_count