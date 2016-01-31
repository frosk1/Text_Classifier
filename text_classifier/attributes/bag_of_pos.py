"""
attribute class BagOfPos
"""

from text_classifier.attributes.attribute import Attribute
import treetaggerwrapper

# Author Jan Wessling


class BagOfPos(Attribute):
    """
    attribute class BagOfPos

    Compute a Bag of Pos Tag Model for the entirely text_set.

    Parameters
    ----------
    bow_model : hash, shape = {string Pos Tag : int 0}
        The variable bow_model can be None if there was no seen training data
        before or it is a hash representing a Bag of Pos Tag skeleton from the
        already seen training data.

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

    model : hash, shape = {string word : int 0}
        This hash contains the Bag of Words skeleton for all unique words in
        the text_set.
    """

    def __init__(self, bow_model):
        self._name = "bag_of_pos"
        self._text_set = None
        self.tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
        self.model = {}
        self.bow_model = bow_model

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
        """ Compute the feature value for attribute Bag of Pos Tag

        First check whether there is a seen BoP skeleton or not. If
        there isn't build_model().Walking through text_set and compute
        feature value for every text object. Counting every Pos Tag appearance
        from the text_set.

        Storing feature value in text.feature hash.
        """

        if self.bow_model is not None:
            print "BOW not None"

            for text in self._text_set:
                temp_model = dict(self.bow_model)
                tags = treetaggerwrapper.make_tags(self.tagger.tag_text(text.text.decode("utf-8")))
                for tag in tags:
                    try:
                        temp_model[tag[1]] += 1
                    except KeyError:
                        continue
                text.features["bag_of_pos"] = temp_model.values()

        else:
            print "BOW is None"
            self.build_model()

            for text in self._text_set:
                # for test_case ''' test__bag_of_words__compute ''' use the OrderedDict
                # to check the values with the term_frequency in test_suitcase.resource
                #
                # temp_model = collections.OrderedDict(sorted(self.model.items()))

                temp_model = dict(self.model)
                tags = treetaggerwrapper.make_tags(self.tagger.tag_text(text.text.decode("utf-8")))
                for tag in tags:
                    try:
                        temp_model[tag[1]] += 1
                    except KeyError:
                        continue
                text.features["bag_of_pos"] = temp_model.values()

            self.bow_model = self.model


    def build_model(self):
        """ Building a Bag of Pos Tag Skeleton.

        A Bag of Pos Tag Skeleton is a hash containing every unique
        Pos Tag, that is in a text from the text_set, as key.
        Initial value is an integer(0).
        """
        for text in self._text_set:
            tags = treetaggerwrapper.make_tags(self.tagger.tag_text(text.text.decode("utf-8")))
            for tag in tags:
                self.model[tag[1]] = 0
