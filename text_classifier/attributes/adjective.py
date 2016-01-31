"""
attribute class Adjective
"""

from text_classifier.attributes.attribute import Attribute
import treetaggerwrapper

# Author Jan Wessling


class Adjective(Attribute):
    """
    attribute class Adjective

    Compute the count of adjectives in text.

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

    adj_tag_list : array, shape = [u"ADJA", u"ADJD"]
        contains the wanted adjective Pos Tags.
    """

    def __init__(self):
        self._name = "adjective"
        self._text_set = None
        self.tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
        self.adj_tag_list = [u"ADJA", u"ADJD"]

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
        """ Compute the feature value for attribute Adjective

        Walking through text_set and compute feature value for every
        text object.

        Storing faeture value in text.feature hash.
        """
        for text in self._text_set:
            tag_list = treetaggerwrapper.make_tags(self.tagger.tag_text(text.text.decode("utf-8")))
            text.features["adjective"] = self.count_adj(tag_list)

    def count_adj(self, tag_list):
        """ Counting found adjective in tag_list.

        Parameters
        ----------
        tag_list : array , shape = [unicode tag1, unicode tag2, ...]
            Contains all pos tags found in text object.

        Returns
        -------
        count : int
            Returns quantity of found adjectives.
        """
        count = 0

        for tuple_tag in tag_list:
            if tuple_tag[1] in self.adj_tag_list:
                count += 1

        return count
