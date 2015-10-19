import re
from text_classifier.body.text import Text
from text_classifier.exceptions import TextNotExistException
from text_classifier.exceptions import WrongKorpusFileFormatException
__author__ = 'jan'


'''
Class Korpus :


'''


class Korpus(object):
    """
    Constructor
    """

    def __init__(self, name):
        self.name = name
        self.content = {}
        self.size = 0

    def __str__(self):
        return self.name + " Korpus mit " + str(self.size) + " Texten"

    def get_text(self, text_id):
        try:
            return self.content[text_id]
        except KeyError:
            raise TextNotExistException(text_id)

    def insert_from_file(self, file_name):
        with open(file_name, "r") as f:
            for line in f.readlines():
                pattern = re.search("(\d+)\t(\w+)\t(.*)", line)
                if pattern is not None and len(pattern.groups()) == 3:
                    text = Text(int(pattern.group(1)), pattern.group(2), pattern.group(3))
                    self.content[int(pattern.group(1))] = text
                else:
                    raise WrongKorpusFileFormatException(file_name)

        self.size = len(self.content)
        f.close()
