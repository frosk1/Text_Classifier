"""
Interface for Dependency-Parser ParZu - University of Zurich.
Dependency Parser for German.

see reference: https://github.com/rsennrich/ParZu

Notes
-----
For using the ParZu Dependency Parser change file path !!!

output = Popen('/path_to_dependency_parser/ParZu_Parser/ParZu/parzu', stdin=tmp2, stdout=PIPE).communicate()[0]

os.remove("/path_to_Text_Classifier_folder/Text_Classifier/text_classifier/tmp.txt")
"""

from subprocess import *
import re
import os

# Author Jan Wessling


def parse_analyses(text_set):
        """ Parsing text objects from text_set

        Parsing every sentence from the text objects in the text_set.

        Parameter
        ---------
        text_set : set
            Containing all text objects.

        Returns
        -------
        id_len_tuples : array, shape = [(int text1 object id, int length text1 object
        sentencelist),...]
        Contains tuples of ID and length sentencelist for the corresping
        text object from the text_set.

        analyses_list : array, shape = [string analysis output from Parzu Interface
        parzu.py]
        Contains the analysis from the Interface for the Dependeny-Parser
        Parzu, see reference in parzu.py.
        """

        tmp = open("tmp.txt", "w")
        id_len_tuples = []

        for text in text_set:
            id_len_tuples.append((text.id, len(text.sentencelist)))
            tmp.write(text.text + "\n")

        tmp.close()
        tmp2 = open("tmp.txt", "r")
        output = Popen('/home/jan/Development-Tools/ParZu_Parser/ParZu/parzu', stdin=tmp2, stdout=PIPE).communicate()[0]

        analyses_list = re.findall("analyses.*", output)
        tmp2.close()
        os.remove("/home/jan/Development/Text_Classifier/text_classifier/tmp.txt")
        return id_len_tuples, analyses_list


def fill_analyses_dict(id_len_tuples, analyses_list):
    """ Fill the analyses_dict

    Read analyses from analyses_list into analyses_dict, to look for passive constructions.

    Parameters
    ----------
    id_len_tuples : array, shape = [(int text1 object id, int length text1 object
    sentencelist),...]
        Contains tuples of ID and length sentencelist for the corresping
        text object from the text_set.

    analyses_list : array, shape = [string analysis output from Parzu Interface
    parzu.py]
        Contains the analysis from the Interface for the Dependeny-Parser
        Parzu, see reference in parzu.py.

    Returns
    -------
    analyses_dict : hash, shape = {text object id : string analysis of all
    sentence within the text object}
        Contains a hash with all sentence analysis for the corresponding text
        object.
    """

    analyses_dict = {}
    start = 0

    for tupl in id_len_tuples:
        text_id = tupl[0]
        length = tupl[1]
        # -1 +1 = 0 xD
        end = start + (length - 1) + 1
        tmp_list = []

        for analyses in analyses_list[start:end]:
            tmp_list.append(analyses)

        analyses_dict[text_id] = tmp_list
        start = end

    return analyses_dict

