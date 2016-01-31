"""
attribute class Readability
"""
# -*- coding: utf-8 -*-

from text_classifier.attributes.attribute import Attribute
import pyphen

# Author Jan Wessling


class Readability(Attribute):
    """
    attribute class Readability

    Computes the readability index for every text in the tex_set.
    The calculated readability index is basesd on the Flesh-Reading-Ease.
    https://de.wikipedia.org/wiki/Lesbarkeitsindex

    Attributes
    ----------
    _name : string
        corresponding name of the implemented attribute

    _text_set : set
        Contains the unique text objects from the real data.
        Initial value : None
    """

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
        """ Compute the Flesh-Reading-Ease for the german language.

        Walking through text_set and compute feature value for every text object.

        Storing feature value in text.feature hash.
        """

        for text in self._text_set:
            asl = float(len(text.wordlist)) / float(len(text.sentencelist))
            syl = self.count_syllables(text.wordlist)
            asw = float(syl) / float(len(text.wordlist))
            text.features["readability"] = (float(180) - float(asl) - (58.5 * float(asw)))

    def count_syllables(self, wordlist):
        """ Count quantity of all syllables in the text

        Parameters
        ----------
        wordlist : array, shape = [word1, word2, word3, ...]
            Extracted wordlist, contains only words, no special character

        Returns
        -------
        syl : int
            Contains number of all syllables in the correspsonding wordlist
            from the text object.
        """
        syl = 0
        lang_dict = pyphen.Pyphen(lang='de_DE')
        for word in wordlist:
            count_syl = len(lang_dict.inserted(word).split("-"))
            syl += count_syl
        return syl
