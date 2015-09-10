# -*- coding: utf-8 -*-
from text_classifier.attributes.attribute import Attribute
import pyphen


class Readability(Attribute):

    def __init__(self):
        self._name = "readability"
        self._text_set = None

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
            asl = float(len(text.wordlist)) / float(len(text.sentencelist))
            syl = self.count_syllables(text.wordlist)
            asw = float(syl) / float(len(text.wordlist))
            text.features["readability"] = (float(180) - float(asl) - (58.5 * float(asw)))

    @staticmethod
    def count_syllables(wordlist):
        syl = 0
        lang_dict = pyphen.Pyphen(lang='de_DE')
        for word in wordlist:
            count_syl = len(lang_dict.inserted(word).split("-"))
            syl += count_syl
        return syl
