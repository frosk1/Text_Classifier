__author__ = 'jan'
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++
Exception-Module for Text-Classifier-System
+++++++++++++++++++++++++++++++++++++++++++++++++++
"""


class EmptyTextException(Exception):

    def __init__(self, text_id):
        self.text_id = text_id

    def __str__(self):
        return "Text_string for Text " + str(self.text_id) + " is empty. Set text_string first."


class EmptyFeatureException(Exception):

    def __init__(self, text_id):
        self.text_id = text_id

    def __str__(self):
        return "No features set for Text " + str(self.text_id) + ". Set features first."


class FeatureNotExistException(Exception):

    def __init__(self, feature_name):
        self.feature_name = feature_name

    def __str__(self):
        return "The Feature " + str(self.feature_name) + " does not exist. Lookup Data.feature_list."


class TextNotExistException(KeyError):

    def __init__(self, text_id):
        self.text_id = text_id

    def __str__(self):
        return "Text with ID " + str(self.text_id) + " does not exist."


class UnequalSizeException(Exception):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Error in attribute class. Feature-vectors has unequal size. Textpair: " + str(self.name)


class WrongFileFormatException(Exception):

    def __init__(self, anno_file):
        self.anno_file = anno_file

    def __str__(self):
        return "Invalid Format in Annotations-File: " + self.anno_file


class NoAnnotationException(Exception):

    def __init__(self, korpus_name):
        self.korpus_name = korpus_name

    def __str__(self):
        return "No Annotation set for korpus '" + self.korpus_name + "'. Please add_anno first."
