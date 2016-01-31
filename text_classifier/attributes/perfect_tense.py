"""
attribute class PerfectTense
"""
# -*- coding: utf-8 -*-

from text_classifier.attributes.attribute import Attribute
from text_classifier.parzu import *

# Author Jan Wessling


class PerfectTense(Attribute):
    """
    attribute class PerfectTense

    Compute the quantity of complex verb perfect tense forms in the text
    with Dependency Parser Parzu from University Zurich.
    https://github.com/rsennrich/ParZu

    Using Parzu interface from parzu.py .

    A perfect tense verb form in german is build with VAFIN and VVPP.
    We define a complex perfect tense verb form as a from with the distance
    of more than three words between VAFIN and VVPP.

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

    analyses_dict : hash, shape = {int text object id : string analysis of all
    sentence within the text object}
        Contains a hash with all sentence analysis for the corresponding text
        object.
    """
    def __init__(self):
        self._name = "perfect_tense"
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
        """ Compute the quantity of complex perfect tense verb forms in
        every text from the text_set

        Generate analysis with the Parzu interface and fill analyses_dict.
        Walking through text_set and compute feature value for every text object.

        Storing feature value in text.feature hash.
        """

        self.id_len_tuples, self.analyses_list = parse_analyses(self._text_set)
        self.analyses_dict = fill_analyses_dict(self.id_len_tuples, self.analyses_list)

        for text in self._text_set:
            text.features["perfect_tense"] = self.count_perfect(text.id)

    def count_perfect(self, text_id):
        """ Looking for a complex perfect tense verb form in analyses_dict

        Look into the analyses_dict value and search in the string for VAFIN
        and VVPP forms. Afterwards check their distance.

        Parameters
        ----------
        text_id : int
        Contains the corresponding id from the text object.

        Returns
        -------
        count : int
            Contains the quantitiy of complex perfect tense verb forms found.
        """

        perf_count = 0
        for analyses in self.analyses_dict[text_id]:
            pattern = re.search("<-',\[mainclause,(\w+)_VAFIN,(\w+)_VVPP]", analyses)
            if pattern:
                s1 = pattern.group(1)
                s2 = pattern.group(2)
                pattern2 = re.search(".*" + s1 + "#(\d+).*" + s2 + "#(\d+).*", analyses)
                if pattern2:
                    if int(pattern2.group(2)) - int(pattern2.group(1)) > 3:
                        perf_count += 1

        return perf_count
