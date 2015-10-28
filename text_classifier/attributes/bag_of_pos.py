
from text_classifier.attributes.attribute import Attribute
import treetaggerwrapper
__author__ = 'jan'


class BagOfPos(Attribute):

    def __init__(self, bow_model):
        self._name = "test_attribute"
        self._text_set = None
        self.tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
        self.model = {}
        self.bow_model = bow_model
        self.tag_list = [u'$.', u'PAV', u'KON', u'PWAV', u'APPR', u'VMFIN', u'ADJA', u'PTKNEG', u'VVIZU', u'PRF', u'NN',
                         u'PDAT', u'NE', u'PIAT', u'ADJD', u'VVINF', u'FM', u'PTKVZ', u'PRELS', u'PIS', u'VVFIN', u'TRUNC',
                         u'ADV', u'$,', u'PPOSAT', u'ART', u'$(', u'KOUS', u'PDS', u'VVPP', u'VMPP', u'PTKANT', u'PTKZU',
                         u'CARD', u'VMINF', u'KOUI', u'VVIMP', u'ITJ', u'PWS', u'VAFIN', u'VAINF', u'APPRART', u'KOKOM',
                         u'PTKA', u'XY', u'PPER', u'APZR']

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

    # def compute(self):
    #     self.build_model()
    #     print len(self.model.keys())
    #     for text in self._text_set:
    #         temp_model = dict(self.model)
    #         tags = treetaggerwrapper.make_tags(self.tagger.tag_text(text.text.decode("utf-8")))
    #         for i in tags:
    #             temp_model[i[1]] += 1
    #
    #         text.features["test_attribute"] = temp_model.values()
    #
    # def build_model(self):
    #     self.model = {tag: 0 for tag in self.tag_list}
    def compute(self):

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
                text.features["test_attribute"] = temp_model.values()

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
                text.features["test_attribute"] = temp_model.values()

            self.bow_model = self.model


    def build_model(self):
        for text in self._text_set:
            tags = treetaggerwrapper.make_tags(self.tagger.tag_text(text.text.decode("utf-8")))
            for tag in tags:
                self.model[tag[1]] = 0