"""
attribute class SentenceStart
"""

from text_classifier.attributes.attribute import Attribute
import collections
import treetaggerwrapper

# Author Jan Wessling


class SentenceStart(Attribute):
    """
    attribute class SentenceStart

    Compute the variety of the sentence start for every
    sentence in the text. If there are the same two lemmatas
    and or Pos Tags in the beginning of a sentence the feature
    value will be 1.

    Attributes
    ----------
    _name : string
        corresponding name of the implemented attribute

    _text_set : set
        Contains the unique text objects from the real data.
        Initial value : None

    tagger : TreeTaggerWrapper with TAGLANG= de
        Python Wrapper for the TreeTagger of Helmudt Schmidt.
        http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/
        Python Wrapper was developed by Laurent Pointal
        http://treetaggerwrapper.readthedocs.org/en/latest/

    tuple_list_lemma : array, shape = [(unicode sent1.word1, unicode
    sent1.word2), ...]
        Contains the first and the second word of every sentence from the text.

    tuple_list_tag : array, shape = [(unicode sent1.tag1, unicode
    sent1.tag2), ...]
        Contains the first and the second Pos Tag of every sentence from the text.
    """

    def __init__(self):
        self._name = "sentence_start"
        self._text_set = None
        self.tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
        self.tuple_list_lemma = []
        self.tuple_list_tag = []

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
        """ Compute the feature value for attribute SentenceStart

        Building lemmatas and tags with TreeTagger. Walking through
        text_set and compute feature value for every text object.

        Storing faeture value in text.feature hash.
        """

        for text in self._text_set:
            for sent in text.sentencelist:
                tags = treetaggerwrapper.make_tags(self.tagger.tag_text(sent))[0:2]
                try:
                    self.tuple_list_lemma.append((tags[0][2], tags[1][2]))
                    self.tuple_list_tag.append((tags[0][1], tags[1][1]))
                except IndexError:
                    continue
            text.features["sentence_start"] = [self.count_lemma(), self.count_tag()]

            self.tuple_list_tag = []
            self.tuple_list_lemma = []

    def count_lemma(self):
        """ Looking for duplicate lemmata in the text

        Building Counter object from collections to search for
        duplicate lemmatas.

        Returns
        -------
        count_lemma : int
            0 means no duplicate entry and 1 means there is a duplicate entry.
        """
        count_lemma = 0
        counter_lemma = collections.Counter(self.tuple_list_lemma)
        if 2 in counter_lemma.values():
                count_lemma = 1
        return count_lemma

    def count_tag(self):
        """ Looking for duplicate Pos Tag in the text

        Building Counter object from collections to search for
        duplicate Pos Tag.

        Returns
        -------
        count_lemma : int
            0 means no duplicate entry and 1 means there is a duplicate entry.
        """
        count_tag = 0
        counter_tag = collections.Counter(self.tuple_list_tag)
        for i in counter_tag.values():
                if i > 2:
                    count_tag = 1
        return count_tag
