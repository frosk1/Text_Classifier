from test_suit import TestSuits

__author__ = 'jan'

"""
+++++++++++++++++++++++++++++++++++++++++++++++++++
Main-Module for testing the Text-Classifier-System
+++++++++++++++++++++++++++++++++++++++++++++++++++

Set up your testing environment here.
-------------------------------------

"""

if __name__ == '__main__':
    system_test = TestSuits(test_name="system_test")
    attribute_test = TestSuits(test_name="attribute_test")
    system_test.run_test()
    # attribute_test.run_test()
