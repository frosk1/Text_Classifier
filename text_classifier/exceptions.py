"""
Exception-Module for Text-Classifier-System

Containing all exceptions for the text-classification system.
"""

# Author Jan Wessling


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


class WrongAnnoFileFormatException(Exception):

    def __init__(self, korpus_file, line):
        self.korpus_file = korpus_file
        self.line = line

    def __str__(self):
        return "Invalid Format in Korpus-File: " + self.korpus_file + "line is: " + self.line


class WrongKorpusFileFormatException(Exception):

    def __init__(self, korpus_file):
        self.korpus_file = korpus_file

    def __str__(self):
        return "Invalid Format in Korpus-File: " + self.korpus_file


class NoAnnotationException(Exception):

    def __init__(self, korpus_name):
        self.korpus_name = korpus_name

    def __str__(self):
        return "No Annotation set for korpus '" + self.korpus_name + "'. Please add_anno first."


class ClassifierNotExistException(Exception):

    def __init__(self, clf_name):
        self.clf_name = clf_name

    def __str__(self):
        return "The Classifier " + str(self.clf_name) + " does not exist. Lookup Model.classifier_list."


class NoClassifierException(Exception):

    def __str__(self):
        return "Set an classifier first. Call Model.set_classifier."


class EmptyFeaturesEmptyTargetsException(Exception):

    def __str__(self):
        return "Fill features and targets first. Call Model.fill_feature_target"


class FoldSizeToBigException(Exception):

    def __init__(self, folds, samples):
        self.folds = folds
        self.samples = samples

    def __str__(self):
        return "Fold size " + str(self.folds) + " is to big. The folds has to be even or less than Sample size "\
               + str(len(self.samples)) + "."


class ModelNotSetException(Exception):

    def __str__(self):
        return "Build model first. Call Model.build_model() for that."


class DFModelNotSetException(Exception):

    def __str__(self):
        return "Build df_model first. Call Model.build_df_model() for that."


class TFModelNotSetException(Exception):

    def __str__(self):
        return "Build tf_model first. Call Model.build_tf_model() for that."
