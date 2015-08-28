__author__ = 'jan'
import numpy as np
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.cross_validation import KFold
from sklearn.metrics import accuracy_score

'''
Class Model :

'''


class Model(object):

    def __init__(self, data):
        self.clf = None
        self.data = data
        self.feature_samples, self.targets = self.fill_feature_target()

    def fill_feature_target(self):
        """

        :return:
        """

        sample_list = []
        target_list = []

        for textpair in self.data.real_data.values():
            textpair.vectorize()
            target_list.append(textpair.target)
            sample_list.append(textpair.feature_vector)

        return np.array(sample_list), np.array(target_list)

    def set_classifier(self, classifier_name):
        """

        :param classifier_name:
        :return:
        """
        if classifier_name == "svm":
            self.clf = svm.SVC()
        elif classifier_name == "naive_bayes":
            self.clf = GaussianNB()
        elif classifier_name == "decision_tree":
            self.clf = tree.DecisionTreeClassifier()
        elif classifier_name == "nearest_centroid":
            self.clf = NearestCentroid()

    def train(self, fraction):
        """

        :param fraction:0
        :return:
        """
        if self.clf is None and self.feature_samples is None:
            print "please set an classifier first and fill feature, target"
        else:
            count = int(round((float(len(self.targets))/float(100))*float(fraction), 0))
            self.clf.fit(self.feature_samples[:count], self.targets[:count])

    def predict(self, sample):
        """

        :param sample:
        :return:
        """
        if self.clf is None:
            print "please set an classifier first and fill feature, target"
        else:
            print self.clf.predict(sample)

    def evaluate(self, folds):
        """

        :param folds:
        :return:
        """
        kf = KFold(len(self.feature_samples), n_folds=folds)
        accuracy_list = []

        for train, test in kf:

            x_train, x_test, y_train, y_test = self.feature_samples[train], self.feature_samples[test], \
                                               self.targets[train], self.targets[test]

            self.clf.fit(x_train, y_train)
            accuracy_list.append(accuracy_score(np.array(y_test), np.array(self.clf.predict(x_test))))

        n = 0
        sum_values = 0

        for acc_value in accuracy_list:

            sum_values = sum_values + acc_value
            n += 1

        acc_mean = (sum_values/n)

        return accuracy_list, acc_mean


