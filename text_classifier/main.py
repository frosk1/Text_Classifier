__author__ = 'jan'
from text_classifier.body.text import Text
from text_classifier.body.korpus import Korpus
from text_classifier.body.textpair import TextPair
from text_classifier.head.data import Data
import os

if __name__ == '__main__':
    text_1 = Text(1, "Tim mag viele tolle sachen,)%$.")
    text_2 = Text(2,"Hallo heute ist ein schoener tag")
    file = "/home/jan/Development/Korpus/ZA/Finales_Korpus/Text_Korpus_aktuell.txt"
    file2 = "/home/jan/annotation_test.txt"
    k1 = Korpus("Test")
    k1.insert_from_file(file)
    #print k1.size
    #print text_1
    #print k1.get_text(50)
    #print k1.get_text(50).get_tokenlist()
    #pair1 = TextPair(text_1, text_2, 1)
    #print pair1
    data1 = Data(k1)
    data1.add_anno(file2)
    #print data1.real_data_size
    #print data1
    data1.attach_feature("standard_attribute")
    for i in data1.real_data.values():
        print i

    print data1.real_data

