from sklearn.metrics.pairwise import pairwise_distances

__author__ = 'jan'

'''
Class Textpair :


'''


class TextPair(object):

    def __init__(self, text1, text2, target):
        self.text1 = text1
        self.text2 = text2
        self.target = target
        self.name = str(self.text1.id) + "_" + str(self.text2.id)
        self.feature_vector = []

    def __str__(self):
        return "Textpair " + self.name+"   Target " + str(self.target) + "\n" +\
               "ID: " + str(self.text1.id) + " Text: " + self.text1.text + "\n" +\
               "Atrtibute:   " + str(self.text1.features) + "\n" +\
               "ID: " + str(self.text2.id) + " Text: " + self.text2.text + "\n" +\
               "Atrtibute:   " + str(self.text2.features)

    def iter_feature_values(self):
        self.text1.vectorize()
        self.text2.vectorize()

        if len(self.text1.feature_vector) == len(self.text2.feature_vector):
            for i in range(len(self.text1.feature_vector)):
                yield (self.text1.feature_vector[i], self.text2.feature_vector[i])
        else:
            print "Error in attribute class. Feature vectors has unequal size. textpair: " + self.name

    def vectorize(self):
        """
        method vectorizer :

        feature vector in a textpair object ist the
        differential between text1 and text2.
        """
        for value1, value2 in TextPair.iter_feature_values(self):
            self.feature_vector.append(value1 - value2)

        # Eculidean distance instead

        # for i in pairwise_distances(self.text1.features.values(), self.text2.features.values(),metric='euclidean'):
        #    for x in i:
        #        self.feature_vector.append(x)
