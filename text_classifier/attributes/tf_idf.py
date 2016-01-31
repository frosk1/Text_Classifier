"""
attribute class TfIdf
"""

from text_classifier.attributes.attribute import Attribute
from text_classifier.exceptions import ModelNotSetException
from text_classifier.exceptions import TFModelNotSetException
from text_classifier.exceptions import DFModelNotSetException
from nltk.corpus import stopwords
import math

# Author Jan Wessling


class TfIdf(Attribute):
    """
    attribute class TfIdf

    Compute TfIdf weighting for the entirely text_set.
    A Bag of Words Model is the fundament for the TfIdf weighting.
    See reference for formulas:
    http://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html

    Parameters
    ----------
    bow_model : hash, shape = {string word : int 0}
        The variable bow_model can be None if there was no seen training data
        before or it is a hash representing a Bag of Words skeleton from the
        already seen training data.

    Attributes
    ----------
    _name : string
        corresponding name of the implemented attribute

    _text_set : set
        Contains the unique text objects from the real data.
        Initial value : None

    model : hash, shape = {string word : int 0}
        This hash contains the Bag of Words skeleton for all unique words in
        the text_set.

    number_of_texts : int
        Contains the number of all texts in the text_set.

    stopwords : array, shape = [string stopdword1, string stopword2, ...]
        Contains list of stopwords from the nltk.corpus for german language.
    """

    def __init__(self, bow_model):
        self._name = "tf_idf"
        self._text_set = None
        self.model = {}
        self.bow_model = bow_model
        self.number_of_texts = 0
        self.stopwords = stopwords.words("german")

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
        """ Compute the feature value for attribute TfIdf

        First check whether there is a seen BoW skeleton or not. If
        there isn't build_model(). Walking through text_set and compute
        feature value for every text object. First build all models and
        compute TfIdf weighting.

        Storing feature value in text.feature hash.
        """


        if self.bow_model is None:
            print "bow_model is None"
            self.build_model()
            df_model = self.build_df_model()

            for text in self._text_set:
                tf_model = self.build_tf_model(text.wordlist_lower)
                tf_idf_model = self.build_tf_idf_model(tf_model, df_model)
                text.features["tf_idf"] = tf_idf_model.values()

        else:
            print "bow_model is not None"
            self.number_of_texts = len(self.text_set)
            df_model = self.build_df_model()

            for text in self._text_set:
                tf_model = self.build_tf_model(text.wordlist_lower)
                tf_idf_model = self.build_tf_idf_model(tf_model, df_model)
                text.features["tf_idf"] = tf_idf_model.values()

    def build_model(self):
        """ Building a Bag of Words Skeleton.

        A Bag of Words Skeleton is a hash containing every unique
        word, that is in a text from the text_set, as key.
        Initial value is an integer(0).
        """
        self.bow_model = {}
        for text in self._text_set:
            for word in text.wordlist_lower:
                if word not in self.stopwords:
                    self.bow_model[word] = 0

        self.number_of_texts = len(self.text_set)

    def build_df_model(self):
        """ Compute the document frequency.

        Count the number of documents within the collection
        that are containing the word. A collection contains all texts
        from the text_set.

        Return
        ------
        df_model : hash, shape = {string word : int df_count}
            Contains every unique word and it's number within
            the collection.
        """
        if len(self.bow_model) == 0:
            raise ModelNotSetException

        else:
            df_model = dict(self.bow_model)

            for text in self.text_set:
                for word in df_model.keys():
                    if word in text.wordlist_lower:
                        df_model[word] +=1
            return df_model

    def build_tf_model(self, wordlist_lower):
        """ Compute the term frequency.

        Count the appearance of words within the text.

        Return
        ------
        tf_model : hash, shape = {string word : int tf_count}
        """
        if len(self.bow_model) == 0:
            raise ModelNotSetException

        else:
            tf_model = dict(self.bow_model)

            for word in wordlist_lower:
                try:
                    tf_model[word] += 1
                except KeyError:
                    continue
            return tf_model

    def build_tf_idf_model(self, tf_model, df_model):
        """ Compute the TfIdf weighting.

        The basis for computing the TfIdf weighting is
        the document frequency and the term frequency.

        Return
        ------
        tf_idf_model : hash, shape = {string word : float TfIdf weighting}
        """

        if len(self.bow_model) == 0:
            raise ModelNotSetException
        elif len(tf_model) == 0:
            raise TFModelNotSetException
        elif len(df_model) == 0:
            raise DFModelNotSetException

        else:

            tf_idf_model = dict(self.bow_model)

            for word in self.bow_model.keys():
                if tf_model[word] == 0:
                    w_tf = 0
                else:
                    w_tf = (1 + math.log10(tf_model[word]))

                if df_model[word] == 0:
                    idf = 0
                else:
                    idf = (math.log10(float(self.number_of_texts) / float(df_model[word])))

                tf_idf_model[word] = (w_tf * idf)

            return tf_idf_model

            # for test_case ''' test__tf_idf__compute ''' use the OrderedDict
            # to check the values with the tf_idf_weight in test_suitcase.resource
            #
            # return collections.OrderedDict(sorted(tf_idf_model.items()))
