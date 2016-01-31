"""
Korpus class for text structure from file
"""

import re
from text_classifier.body.text import Text
from text_classifier.exceptions import TextNotExistException
from text_classifier.exceptions import WrongKorpusFileFormatException

# Author: Jan Wessling


class Korpus(object):
    """
    corpus-structure

    Build a data-structure for reading text from corpus-file

    Parameters
    ----------
    name : string, obligatory
        No Korpus without a name.

    Attributes
    -----------
    content : hash, shape = {text_id: text object}
        Python dictionary for storing the text objects from corpus file.

    size : int
        Defines the quantity of the corpus content.
    """

    def __init__(self, name):
        self.name = name
        self.content = {}
        self.size = 0

    def __str__(self):
        return self.name + " Korpus mit " + str(self.size) + " Texten"

    def get_text(self, text_id):
        """ Get the text object from teh corpus content.

        Parameters
        ----------
        text_id : int
            The corresponding text id.

        Returns
        -------
        text object : Text
            The wanted text object for the corresponding text id.
        """
        try:
            return self.content[text_id]
        except KeyError:
            raise TextNotExistException(text_id)

    def insert_from_file(self, file_name):
        """ Insert data from corpus file.

        Parameters
        ----------
        file_name : string
            Path from the corpus file.
        """
        with open(file_name, "r") as f:

            for line in f.readlines():

                # Pattern of the corpus file structure
                pattern = re.search("(\d+)\t(\w+)\t(.*)", line)

                if pattern is not None and len(pattern.groups()) == 3:

                    text = Text(int(pattern.group(1)), pattern.group(2), pattern.group(3))
                    self.content[int(pattern.group(1))] = text

                else:
                    raise WrongKorpusFileFormatException(file_name)

        self.size = len(self.content)
        f.close()
