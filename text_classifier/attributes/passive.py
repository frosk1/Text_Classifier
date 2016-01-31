"""
attribute class Passive
"""
# -*- coding: utf-8 -*-

from text_classifier.parzu import *
from text_classifier.attributes.attribute import Attribute

# Author Jan Wessling


class Passive(Attribute):
    """
    attribute class Passive

    Compute the quantity of verb passive forms in the text
    with Dependency Parser Parzu from University Zurich.
    https://github.com/rsennrich/ParZu

    Using Parzu interface from parzu.py .

    Attributes
    ----------
    _name : string
        corresponding name of the implemented attribute

    _text_set : set
        Contains the unique text objects from the real data.
        Initial value : None

    analyses_list : array, shape = [string analysis output from Parzu Interface
    parzu.py]
        Contains the analysis from the Interface for the Dependeny-Parser
        Parzu, see reference in parzu.py.

    id_len_tuples : array, shape = [(int text1 object id, int length text1 object
    sentencelist),...]
        Contains tuples of ID and length sentencelist for the corresping
        text object from the text_set.

    analyses_dict : hash, shape = {text object id : string analysis of all
    sentence within the text object}
        Contains a hash with all sentence analysis for the corresponding text
        object.
    """
    def __init__(self):
        self._name = "passive"
        self._text_set = None
        self.analyses_list = None
        self.id_len_tuples = None
        self.analyses_dict = None

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
        """ Compute the quantity of passive verb forms in every text from the text_set

        Generate analysis with the Parzu interface and fill analyses_dict.
        Walking through text_set and compute feature value for every text object.

        Storing feature value in text.feature hash.
        """

        self.id_len_tuples, self.analyses_list = parse_analyses(self._text_set)
        self.analyses_dict = fill_analyses_dict(self.id_len_tuples, self.analyses_list)

        for text in self._text_set:
            text.features["passive"] = self.count_passive(text.id)

    def count_passive(self, text_id):
        """ Looking for passive verb form in analyses_dict

        Look into the analyses_dict value and search in the
        string for passive verb form.

        Parameters
        ----------
        text_id : int
        Contains the corresponding id from the text object.

        Returns
        -------
        count : int
            Contains the quantitiy of found passive verb forms.
        """
        count = 0
        for analyses in self.analyses_dict[text_id]:
            if "passive" in analyses:
                count += 1
        return count
