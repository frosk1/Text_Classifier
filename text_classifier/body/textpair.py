"""
Textpair class for storing annotation
"""

from text_classifier.exceptions import UnequalSizeException

# Author: Jan Wessling


class TextPair(object):
    """ textpair annotation

    Storing the annotation data for a Pair of text objects.

    Parameters
    ----------
    text1 : Text, obligatory
        text object stord in the corpus class

    text2 : Text, obligatory
        text object stord in the corpus class

    target : int, obligatory
        target is the annotation value --> 0,1

    Attributes
    ----------
    name : string
        Contains the text.id from text1 and text2.

    feature_vector : array, shape = [n_feature_values]
        Represents the feature_vector of a textpair. This vector ist the
        differential between text1-vector and text2-vector.
    """
    def __init__(self, text1, text2, target):
        self.text1 = text1
        self.text2 = text2
        self.target = target
        self.name = str(self.text1.id) + "_" + str(self.text2.id)
        self.feature_vector = []

    def __str__(self):
        return "Textpair " + self.name + "   Target " + str(self.target) + "\n" + \
               "ID: " + str(self.text1.id) + " Text: " + self.text1.text + "\n" + \
               "Atrtibute:   " + str(self.text1.features) + "\n" + \
               "ID: " + str(self.text2.id) + " Text: " + self.text2.text + "\n" + \
               "Atrtibute:   " + str(self.text2.features)

    def iter_feature_values(self):
        """Generator iterates feature_vectors

        Yields every dimension of the feature_vectors for
        text1 and text2.
        """
        self.text1.vectorize()
        self.text2.vectorize()

        if len(self.text1.feature_vector) == len(self.text2.feature_vector):
            for i in range(len(self.text1.feature_vector)):
                yield (self.text1.feature_vector[i], self.text2.feature_vector[i])
        else:
            raise UnequalSizeException(self.name)

    def vectorize(self):
        """ Setter for the feature_vector

        Walking through every value in the feature_vectors of
        text1 and text2, then building the differntial.
        """
        for value1, value2 in TextPair.iter_feature_values(self):
            self.feature_vector.append(value1 - value2)

            # Eculidean distance instead

            # for i in pairwise_distances(self.text1.features.values(), self.text2.features.values(),metric='euclidean'):
            #    for x in i:
            #        self.feature_vector.append(x)
