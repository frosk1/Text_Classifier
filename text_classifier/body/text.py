"""
Text class for storing linguistic-parameters
"""

from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import sent_tokenize
from text_classifier.exceptions import EmptyTextException
from text_classifier.exceptions import EmptyFeatureException
import re

# Author : Jan Wessling


class Text(object):
    """
    text-information

    Storing linguistic information about the text from the corpus file.

    Parameters
    ----------
    text : string, obligatory
        Given text string within the corpus

    id : int, obligatory
        Given text id within the corpus.

    category : string, obligatory
        Given category within the corpus --> man, auto_gut, auto_schlecht

    Attributes
    -----------
    tokenlist : array, shape = [token1, token2, token3, ...]
        Extracted tokenlist with method wordpunct_tokenize from nltk-modul.

    sentencelist : array, shape = [sentenc1, sentenc2, sentence3, ...]
        Extracted sentencelist with method sent_tokenize from nltk-modul

    wordlist : array, shape = [word1, word2, word3, ...]
        Extracted wordlist, contains only words, no special character

    features : hash, shape = {feature_name : feature_value}
        Python dict to store the feature value.
        Feature name : string ; Feature values : int/float/array

    feature_vector : array, shape = [n_feature_values]
        Python list that represents feature_vector with every value of every
        attached feature.

    __feature_vector_init : boolean
        Defines the initialization of a filled feature_vector with method
        vectorize().
    """

    def __init__(self, id, category, text):
        self.text = text
        self.id = id
        self.category = category
        self.tokenlist = wordpunct_tokenize(self.text.decode("utf8"))
        self.sentencelist = sent_tokenize(self.text.decode("utf-8"))
        self.wordlist = self.set_wordlist()
        self.wordlist_lower = map(unicode.lower, self.wordlist)
        self.features = {}
        self.feature_vector = []
        self.__feature_vector_init = False

    def __str__(self):
        return "ID: " + str(self.id) + " Text: " + self.text

    def set_wordlist(self):
        """Setter for wordlist

        Filtering the tokenlist and building wordlist.

        Returns
        -------
        wordlist : array, shape = [word1, word2, word3, ...]
        """
        if self.text == "":
            raise EmptyTextException(self.id)
        else:
            wordlist = []
            for token in self.tokenlist:
                if re.sub("\W", "", token):
                    wordlist.append(token)
            return wordlist

    def vectorize(self):
        """ Setter for feature_vector

        Walking through features and picking up every value.
        """
        if not self.__feature_vector_init:
            if len(self.features) == 0:
                raise EmptyFeatureException(self.id)
            else:
                for value in self.features.values():
                    if isinstance(value, list):
                        self.feature_vector = self.feature_vector + value
                    else:
                        self.feature_vector.append(value)
                self.__feature_vector_init = True
