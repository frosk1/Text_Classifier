__author__ = 'jan'

import abc
from random import randint
'''
abstract Class Atrtibute :

'''

class attribute(object):
    __metaclass__ = abc.ABCMeta


    @abc.abstractproperty
    def name(self):
        return

    @name.setter
    def name(self, new_value):
        return

    @abc.abstractproperty
    def data(self):
        return

    @data.setter
    def data(self, new_value):
        return






# class testabstract(attribute):
#
#     #name = " "
#
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#     def huhu(self, der):
#         self._name = 3

class testabstract2(object):
    liste = [2,3,4,5]
    #name = " "

    def __init__(self,day, month=4):
        self.day = day
        self.month = month
        self._name = None


if __name__ == '__main__':

    #t = testabstract()
    #t2 = testabstract2()
    #t4 = testabstract2(5)
    dic = {1:3,4:5,6:7}
    for i in dic.items():
        print i
        i = 5
    print dic
