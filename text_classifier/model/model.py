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
        self.feature_samples = None
        self.targets = None

    def fill_feature_target(self):
        """

        :return:
        """
        sample_list = []
        target_list = []
        for textpair in self.data.real_data.values():
            f_list =[]
            target_list.append(textpair.target)
            for feature_name in textpair.text1.features.keys():
                f_list.append(textpair.text1.features[feature_name])
                f_list.append(textpair.text2.features[feature_name])
            sample_list.append(f_list)
        self.feature_samples = np.array(sample_list)
        self.targets = np.array(target_list)

    def set_classifier(self, classifier_name):
        """

        :param classifier_name:
        :return:
        """
        if classifier_name == "svm":
            self.clf = svm.SVC(gamma=0.001, C=100)

    def train(self, fraction):
        """

        :param fraction:
        :return:
        """
        if self.clf is None and self.feature_samples is None:
            print "please set an classifier first and fill feature, target"
        else:
            count = int(round((float(len(self.targets))/float(100))*float(fraction),0))
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

    def evaluate(self):
        kf = KFold(len(self.feature_samples), n_folds=10)
        predict_list = []
        true_list = []
        for train, test in kf:
            x_train, x_test, y_train, y_test = self.feature_samples[train], self.feature_samples[test], self.targets[train], self.targets[test]
            self.clf.fit(x_train, y_train)
            predict_list.append(self.clf.predict(x_test))
            true_list.append(y_test)
        return accuracy_score(predict_list,true_list)





if __name__ == '__main__':
    X = np.array([[0., 0.], [1., 1.], [-1., -1.], [2., 2.]])
    y = np.array([0, 1, 0, 1])
    kf = KFold(4, n_folds=2)
    for train, test in kf:
        X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
        print X_train#, X_test
        #print y_train, y_test
        print y_train
        break