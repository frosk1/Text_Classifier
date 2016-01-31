"""
attribute class ModalVerb
"""

from text_classifier.attributes.attribute import Attribute
import treetaggerwrapper

# Author Jan Wessling


class ModalVerb(Attribute):
    """
    attribute class ModalVerb

    Compute the quantity of ModalVerb appearance in the text.

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

    tag_list : array, shape = [unicode tag1, unicode tag2,... ]
        Contaings Pos Tags for every ModalVerb.

    """

    def __init__(self):
        self._name = "modal_verb"
        self._text_set = None
        self.tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
        self.tag_list = [u"VMFIN", u"VMINF", u"VMPP"]

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
        """ Compute the quantity of ModalVerbs in every text from the text_set

        Walking through text_set and compute feature value for every text object.

        Storing feature value in text.feature hash.
        """
        for text in self._text_set:
            count_modal = 0
            tags = treetaggerwrapper.make_tags(self.tagger.tag_text(text.text.decode("utf-8")))
            for tag in tags:
                if tag[1] in self.tag_list:
                    count_modal += 1
            text.features[self._name] = count_modal
