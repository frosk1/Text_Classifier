from subprocess import *
import re
import os
__author__ = 'jan'

"""
Interface for Dependency-Parser ParZu - University of Zurich.
Dependency Parser for German.
"""


def parse_analyses(text_set):
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
    ######################################################################################
    # read analyses from analyses_list into analyses_dict, to look for passive constructions.
    #######################################################################################
    analyses_dict = {}
    start = 0

    for tupl in id_len_tuples:
        text_id = tupl[0]
        length = tupl[1]
        end = start + (length - 1) + 1
        tmp_list = []

        for analyses in analyses_list[start:end]:
            tmp_list.append(analyses)

        analyses_dict[text_id] = tmp_list
        start = end

    return analyses_dict

