from text_classifier.attributes.attribute import Attribute
from text_classifier.exceptions import ModelNotSetException
from text_classifier.exceptions import TFModelNotSetException
from text_classifier.exceptions import DFModelNotSetException
import math
import collections

__author__ = 'jan'
"""
class TfIdf

"""


class TfIdf(Attribute):
    def __init__(self):
        self._name = "tf_idf"
        self._text_set = None
        self.model = {}
        self.number_of_texts = 0

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
        self.build_model()
        df_model = self.build_df_model()

        for text in self._text_set:
            tf_model = self.build_tf_model(text.tokenlist)
            tf_idf_model = self.build_tf_idf_model(tf_model, df_model)
            text.features["tf_idf"] = tf_idf_model.values()

    def build_model(self):

        for text in self._text_set:
            for word in text.wordlist:
                self.model[word.lower()] = 0

        self.number_of_texts = len(self.text_set)

    def build_df_model(self):

        if len(self.model) == 0:
            raise ModelNotSetException

        else:
            df_model = dict(self.model)

            for text in self.text_set:
                for token in text.tokenlist:
                    try:
                        df_model[token.lower()] += 1
                    except KeyError:
                        continue
            return df_model

    def build_tf_model(self, tokenlist):

        if len(self.model) == 0:
            raise ModelNotSetException

        else:
            tf_model = dict(self.model)

            for token in tokenlist:
                try:
                    tf_model[token.lower()] += 1
                except KeyError:
                    continue
            return tf_model

    def build_tf_idf_model(self, tf_model, df_model):

        if len(self.model) == 0:
            raise ModelNotSetException
        elif len(tf_model) == 0:
            raise TFModelNotSetException
        elif len(df_model) == 0:
            raise DFModelNotSetException

        else:

            tf_idf_model = dict(self.model)

            for word in self.model.keys():
                if tf_model[word] == 0:
                    w_tf = 0
                else:
                    w_tf = (1 + math.log10(tf_model[word]))

                idf = (math.log10(float(self.number_of_texts) / float(df_model[word])))
                tf_idf_model[word] = (w_tf * idf)

            return collections.OrderedDict(sorted(tf_idf_model.items()))
