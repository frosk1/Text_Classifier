from text_classifier.attributes.attribute import Attribute
import collections
import treetaggerwrapper
__author__ = 'jan'


class SentenceStart(Attribute):

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
        count_lemma = 0
        counter_lemma = collections.Counter(self.tuple_list_lemma)
        if 2 in counter_lemma.values():
                count_lemma = 1
        return count_lemma

    def count_tag(self):
        count_tag = 0
        counter_tag = collections.Counter(self.tuple_list_tag)
        for i in counter_tag.values():
                if i > 2:
                    count_tag = 1
        return count_tag
