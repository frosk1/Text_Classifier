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

    def __str__(self):
        return "ID: "+str(self.id) + " Text: " + self.text

    def get_tokenlist(self):
        if self.text == "":
            return "text is empty"
        else:
            return self.tokenlist

    def get_feature(self, feature_name):
        try:
            return self.features[feature_name]
        except KeyError:
            print "feature "+feature_name+" does not exist"

    def set_feature(self, feature_name, feature_value):
        self.features[feature_name] = feature_value

