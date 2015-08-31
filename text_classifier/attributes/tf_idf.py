__author__ = 'jan'
"""
class TfIdf

"""
from text_classifier.attributes.attribute import Attribute
import re
import math


class TfIdf(Attribute):

    def __init__(self):
        self._name = "tf_idf"
        self._data = None
        # self.corpus = None
        self.model = {}
        self.text_set = set()
        self.number_of_texts = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        self._data = new_value

    def compute(self):
        self.build_model()
        df_model = self.build_df_model()

        for textpair in self._data.values():
            #Text1
            tf_model = self.build_tf_model(textpair.text1.tokenlist)
            tf_idf_model = self.build_tf_idf_model(tf_model, df_model)
            textpair.text1.features["tf_idf"] = tf_idf_model.values()

            #Text2
            tf_model = self.build_tf_model(textpair.text2.tokenlist)
            tf_idf_model = self.build_tf_idf_model(tf_model, df_model)
            textpair.text2.features["tf_idf"] = tf_idf_model.values()

    def build_model(self):

        for textpair in self._data.values():
            self.text_set.add(textpair.text1)
            self.text_set.add(textpair.text2)

        for text in self.text_set:
            for token in text.tokenlist:
                if re.match("\w+", token) and not self.model.has_key(token):
                    self.model[token.lower()] = 0

        self.number_of_texts = len(self.text_set)

    def build_df_model(self):

        if len(self.model) == 0:
            print "Please build_model first."

        else:
            df_model = dict(self.model)

            for text in self.text_set:
                for token in text.tokenlist:
                    if token.lower() in df_model.keys():
                        df_model[token.lower()] += 1
            return df_model

    def build_tf_model(self, tokenlist):

        if len(self.model) == 0:
            print "Please build_model first."

        else:
            tf_model = dict(self.model)

            for token in tokenlist:
                if token.lower() in self.model.keys():
                    tf_model[token.lower()] += 1
            return tf_model

    def build_tf_idf_model(self, tf_model, df_model):

        if len(self.model) == 0:
            print "Please build_model first."
        elif len(tf_model) == 0:
            print "Please build_tf_model first."
        elif len(df_model) == 0:
            print "Please build_df_model first."

        else:

            tf_idf_model = dict(self.model)

            for word in self.model.keys():
                    if tf_model[word] == 0:
                        w_tf = 0
                    else:
                        w_tf = (1+math.log10(tf_model[word]))

                    idf = (math.log10(float(self.number_of_texts)/float(df_model[word])))
                    tf_idf_model[word] = (w_tf*idf)
            return tf_idf_model
