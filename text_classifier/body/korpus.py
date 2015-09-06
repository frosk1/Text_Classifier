import re
from text_classifier.body.text import Text
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
        return self.name+" Korpus mit "+str(self.size)+" Texten"

    # def get_text(self, text_id):
    #     try:
    #         return self.content[text_id]
    #     except KeyError:
    #         print "text with ID "+text_id+" does not exist"

    def insert_from_file(self, file_name):
        with open(file_name, "r") as f:
            for line in f.readlines():
                pattern = re.search("(\d+)\t\t(.*)", line)
                text = Text(int(pattern.group(1)),pattern.group(2))
                # print text.group(1) + " " + text.group(2)
                self.content[int(pattern.group(1))] = text
        self.size = len(self.content)
        f.close()




