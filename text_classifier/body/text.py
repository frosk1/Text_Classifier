__author__ = 'jan'
from nltk.tokenize import wordpunct_tokenize


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
        self.features = {}
        self.feature_vector = []
        self.__feature_vector_init = False

    def __str__(self):
        return "ID: "+str(self.id) + " Text: " + self.text

    def get_tokenlist(self):
        if self.text == "":
            return "text is empty"
        else:
            return self.tokenlist

    def vectorize(self):

        if not self.__feature_vector_init:
            if len(self.features) == 0:
                print "Please attach features first. Need to call data.py for that."
            else:
                for value in self.features.values():
                    if isinstance(value, list):
                        self.feature_vector = self.feature_vector + value
                    else:
                        self.feature_vector.append(value)
                self.__feature_vector_init = True
