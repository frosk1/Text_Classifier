__author__ = 'jan'
from text_classifier.body.text import Text
from text_classifier.body.korpus import Korpus
from text_classifier.body.textpair import TextPair
import os

if __name__ == '__main__':
    text_1 = Text(1, "Tim mag viele tolle sachen,)%$.")
    text_2 = Text(2,"Hallo heute ist ein schoener tag")
    file = "/home/jan/Development/Korpus/ZA/Finales_Korpus/Text_Korpus_aktuell.txt"
    k1 = Korpus("Test")
    k1.insert_from_file(file)
    print k1.size
    print text_1
    print k1.get_text(50)
    print k1.get_text(50).get_tokenlist()
    pair1 = TextPair(text_1, text_2, 1)
    print pair1