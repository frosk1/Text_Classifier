from sklearn.feature_extraction.text import CountVectorizer
from text_classifier.attributes.attribute import Attribute
from nltk.corpus import stopwords
import collections
__author__ = 'jan'
'''
class BagOfWords :

'''


class BagOfWords(Attribute):

    def __init__(self, bow_model):
        self._name = "bag_of_words"
        self._text_set = None
        self.model = {}
        self.stopwords = stopwords.words("german")
        self.sentence_list = []
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

        if self.bow_model is not None:
            print "BOW not None"
            # vectorizer = self.bow_model
            # X = vectorizer.transform(self.sentence_list)
            # # print vectorizer.get_feature_names()
            # A = X.toarray()

            for text in self._text_set:
                temp_model = dict(self.bow_model)
                for word in text.wordlist_lower:
                    try:
                        temp_model[word] += 1
                    except KeyError:
                        continue
                text.features["bag_of_words"] = temp_model.values()

                # end_list = []
                # for i in A[c]:
                #     end_list.append(i)
                #
                # text.features["bag_of_words"] = end_list
                # c += 1
        else:
            print "BOW is None"
            # vectorizer = CountVectorizer(min_df=1)
            # X = vectorizer.fit_transform(self.sentence_list)
            # # print vectorizer.get_feature_names()
            # A = X.toarray()
            self.build_model()

            for text in self._text_set:
                # for test_case ''' test__bag_of_words__compute ''' use the OrderedDict
                # to check the values with the term_frequency in test_suitcase.resource
                #
                # temp_model = collections.OrderedDict(sorted(self.model.items()))

                temp_model = dict(self.model)
                for word in text.wordlist_lower:
                    try:
                        temp_model[word] += 1
                    except KeyError:
                        continue
                text.features["bag_of_words"] = temp_model.values()

            self.bow_model = self.model
            #     end_list = []
            #     for i in A[c]:
            #         end_list.append(i)
            #
            #
            #     text.features["bag_of_words"] = end_list
            #     c += 1
            # self.bow_model = vectorizer

    def build_model(self):
        for text in self._text_set:
            # self.sentence_list.append(text.text)
            for word in text.wordlist_lower:
                if word not in self.stopwords:
                    self.model[word] = 0
        # print self.sentence_list