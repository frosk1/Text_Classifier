from text_classifier.attributes.attribute import Attribute
import treetaggerwrapper
__author__ = 'jan'


class ModalVerb(Attribute):

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

        for text in self._text_set:
            count_modal = 0
            tags = treetaggerwrapper.make_tags(self.tagger.tag_text(text.text.decode("utf-8")))
            for tag in tags:
                if tag[1] in self.tag_list:
                    count_modal += 1
            text.features[self._name] = count_modal
