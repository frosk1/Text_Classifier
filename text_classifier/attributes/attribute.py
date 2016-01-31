"""
base class for all implemented attributes
"""

import abc

# Author : Jan Wessling


class Attribute(object):
    """
    attribute class structure

    Defines the base class for all implemented attributes.

    Attributes
    -----------
    name : string
        Every derived attribute class needs a name.

    text_set : set
        Every derived attribute class needs a text_set.
        This set contains all unique text objects from
        the real data.

    Methods
    -------
    compute()
        Every derived attribute class needs a compute() method.
        This method provides the calculated feature value for the
        text object.
    """


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
    def text_set(self):
        """
        Annotated Data, given by the Data class
        """
        return

    @text_set.setter
    def text_set(self, new_value):
        """
        Setter method for attribute 'text_set'.
        """
        return

    @abc.abstractmethod
    def compute(self):
        """
        Compute the feature value and attach it to the data.
        """
        return
