__author__ = 'jan'
import numpy as np
from sklearn import svm
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
            self.clf = svm.SVC(kernel='linear')

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
        predict_list = []
        true_list = []

        for train, test in kf:
            x_train, x_test, y_train, y_test = self.feature_samples[train], self.feature_samples[test], \
                                               self.targets[train], self.targets[test]
            self.clf.fit(x_train, y_train)
            predict_list.append(self.clf.predict(x_test)[0])
            true_list.append(y_test[0])

        print "True Targets : \n%s " % true_list
        print "Model Targets : \n%s" % predict_list
        return accuracy_score(predict_list, true_list)



