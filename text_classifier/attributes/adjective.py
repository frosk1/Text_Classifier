from text_classifier.attributes.attribute import Attribute
import treetaggerwrapper
__author__ = 'jan'


class Adjective(Attribute):

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
        for text in self._text_set:
            tag_list = treetaggerwrapper.make_tags(self.tagger.tag_text(text.text.decode("utf-8")))
            text.features["adjective"] = self.count_adj(tag_list)

    def count_adj(self, tag_list):
        count = 0

        for tuple_tag in tag_list:
            if tuple_tag[1] in self.adj_tag_list:
                count += 1

        if count >= 7:
            adj = 1
        else:
            adj = 0

        return adj
