import abc
__author__ = 'jan'


'''
abstract Class Atrtibute :

'''


class Attribute(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def name(self):
        """
        Name of the feature.
        """
        return

    @name.setter
    def name(self, new_value):
        """
        Setter method for attribute 'name'.
        """
        return

    @abc.abstractproperty
    def data(self):
        """
        Annotated Data, given by the Data class
        """
        return

    @data.setter
    def data(self, new_value):
        """
        Setter method for attribute 'data'.
        """
        return

    @abc.abstractmethod
    def compute(self):
        """
        Compute the feature value and attach it to the data.
        """
        return
