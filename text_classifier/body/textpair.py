__author__ = 'jan'



'''
Class Textpair :


'''

class TextPair(object):

    def __init__(self, text1, text2, target):
        self.text1 = text1
        self.text2 = text2
        self.target = target
        self.name = str(self.text1.id)+"_"+str(self.text2.id)

    def __str__(self):
        return "Textpair "+self.name+"   Target "+str(self.target)+"\n"+\
               "ID: "+str(self.text1.id) + " Text: " + self.text1.text+"\n"+\
               "Atrtibute:   "+str(self.text1.features)+"\n"+\
               "ID: "+str(self.text2.id) + " Text: " + self.text2.text+"\n"+\
               "Atrtibute:   "+str(self.text2.features)
