"""
attribute class Variety
"""
# -*- coding: utf-8 -*-

from text_classifier.attributes.attribute import Attribute
import re
import collections
from nltk.corpus import stopwords

# Author Jan Wessling


class Variety(Attribute):
    """
    attribute class Variety

    Compute the variety count. Looking for recurrence in successive
    sentence.


    Attributes
    ----------
    _name : string
        corresponding name of the implemented attribute

    _text_set : set
        Contains the unique text objects from the real data.
        Initial value : None

    stopwords : array, shape = [string stopdword1, string stopword2, ...]
        Contains list of stopwords from the nltk.corpus for german language.

    var_count : hash, shape = { int text id : int variety count}
        Contains the corresponding variety count for the text object.
    """
    def __init__(self):
        self._name = "variety"
        self._text_set = None
        self.stopwords = stopwords.words("german")
        self.var_count = dict()

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
        """ Compute the feature value for attribute Variety

        Build wordlist for all two successive sentence in the text.
        Count and filter wordlist.

        Storing feature value in text.feature hash.
        """
        for text in self._text_set:
            self.var_count[text.id] = 0

            if len(text.sentencelist) > 1:
                for i in range(len(text.sentencelist)):
                    try:
                        words = re.findall(r'\w+', (text.sentencelist[i] + text.sentencelist[i + 1]), re.UNICODE)
                        self.count_and_filter(words, text)

                    except IndexError:
                        continue
            else:
                words = re.findall(r'\w+', text.sentencelist[0], re.UNICODE)
                self.count_and_filter(words, text)

    def count_and_filter(self, wordlist, text):
        """ Count recurrence and filter stopwords.

        Parameter
        ---------
        wordlist : array, shape = [unicode word1, unicode word2, ...]
            contains all words from two successive sentences.

        text : Text
            Contains text object from the text_set.
        """
        c = collections.Counter(wordlist)
        for x in c.keys():
            if x.lower() in self.stopwords:
                c.pop(x)
            else:
                if c[x] > 1:
                    self.var_count[text.id] += 1

        text.features["variety"] = self.var_count[text.id]
