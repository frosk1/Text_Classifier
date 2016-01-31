"""
attribute class BagOfWords
"""

from text_classifier.attributes.attribute import Attribute
from nltk.corpus import stopwords

# Author Jan Wessling


class BagOfWords(Attribute):
    """
    attribute class BagOfWords

    Compute a Bag of Words Model for the entirely text_set.

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

    stopwords : array, shape = [string stopdword1, string stopword2, ...]
        Contains list of stopwords from the nltk.corpus for german language.

    model : hash, shape = {string word : int 0}
        This hash contains the Bag of Words skeleton for all unique words in
        the text_set.
    """

    def __init__(self, bow_model):
        self._name = "bag_of_words"
        self._text_set = None
        self.model = {}
        self.stopwords = stopwords.words("german")
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
        """ Compute the feature value for attribute Bag of Words

        First check whether there is a seen BoW skeleton or not. If
        there isn't build_model().Walking through text_set and compute
        feature value for every text object. Counting every word appearance
        from the text_set.

        Storing feature value in text.feature hash.
        """

        if self.bow_model is not None:
            print "BOW not None"

            for text in self._text_set:
                temp_model = dict(self.bow_model)

                for word in text.wordlist_lower:
                    try:
                        temp_model[word] += 1
                    except KeyError:
                        continue

                text.features["bag_of_words"] = temp_model.values()

        else:
            print "BOW is None"
            self.build_model()

            for text in self._text_set:
                temp_model = dict(self.model)

                for word in text.wordlist_lower:
                    try:
                        temp_model[word] += 1
                    except KeyError:
                        continue

                text.features["bag_of_words"] = temp_model.values()

            self.bow_model = self.model

    def build_model(self):
        """ Building a Bag of Words Skeleton.

        A Bag of Words Skeleton is a hash containing every unique
        word, that is in a text from the text_set, as key.
        Initial value is an integer(0).
        """
        for text in self._text_set:
            for word in text.wordlist_lower:
                if word not in self.stopwords:
                    self.model[word] = 0
