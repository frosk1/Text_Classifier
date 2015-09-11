from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import sent_tokenize
from text_classifier.exceptions import EmptyTextException
from text_classifier.exceptions import EmptyFeatureException
import re
__author__ = 'jan'


'''
Class Text :


'''


class Text(object):
    """
    Constructor
    """

    def __init__(self, text_id, text_string):
        self.text = text_string
        self.id = text_id
        self.tokenlist = wordpunct_tokenize(self.text.decode("utf8"))
        self.sentencelist = sent_tokenize(self.text.decode("utf-8"))
        self.wordlist = self.set_wordlist()
        self.wordlist_lower = map(unicode.lower, self.wordlist)
        self.features = {}
        self.feature_vector = []
        self.__feature_vector_init = False

    def __str__(self):
        return "ID: " + str(self.id) + " Text: " + self.text

    def get_tokenlist(self):
        if self.text == "":
            raise EmptyTextException(self.id)

        else:
            return self.tokenlist

    def set_wordlist(self):
        if self.text == "":
            raise EmptyTextException(self.id)
        else:
            wordlist = []
            for token in self.tokenlist:
                if re.sub("\W", "", token):
                    wordlist.append(token)
            return wordlist

    def vectorize(self):

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
