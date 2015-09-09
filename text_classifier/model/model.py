import numpy as np
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.cross_validation import KFold
from sklearn.metrics import accuracy_score
from sklearn import metrics
from text_classifier.exceptions import ClassifierNotExistException
from text_classifier.exceptions import EmptyFeaturesEmptyTargetsException
from text_classifier.exceptions import NoClassifierException
from text_classifier.exceptions import FoldSizeToBigException

__author__ = 'jan'

'''
Class Model :

'''


class Model(object):
    def __init__(self, data):
        self.clf = None
        self.data = data
        self.feature_samples, self.targets = self.fill_feature_target()
        self.classifier_list = ["svm_linear", "svm_poly", "naive_bayes", "decision_tree", "nearest_centroid",
                                "k_neighbors", "radius_neighbors"]

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
        if classifier_name == "svm_linear":
            self.clf = svm.SVC(kernel="linear")
        elif classifier_name == "svm_poly":
            self.clf = svm.SVC(kernel="poly")
        elif classifier_name == "naive_bayes":
            self.clf = GaussianNB()
        elif classifier_name == "decision_tree":
            self.clf = tree.DecisionTreeClassifier()
        elif classifier_name == "nearest_centroid":
            self.clf = NearestCentroid()
        elif classifier_name == "k_neighbors":
            self.clf = KNeighborsClassifier(n_neighbors=100)
        elif classifier_name == "radius_neighbors":
            self.clf = RadiusNeighborsClassifier(radius=1.0, outlier_label=1)
        else:
            raise ClassifierNotExistException(classifier_name)

    def train(self, fraction):
        """

        :param fraction:0
        :return:
        """
        if self.clf is None:
            raise NoClassifierException
        elif self.targets.size == 0 and self.feature_samples.size == 0:
            raise EmptyFeaturesEmptyTargetsException
        else:
            count = int(round((float(len(self.targets)) / float(100)) * float(fraction), 0))
            self.clf.fit(self.feature_samples[:count], self.targets[:count])

    def predict(self, sample):
        """

        :param sample:
        :return:
        """
        if self.clf is None:
            raise NoClassifierException
        elif self.targets.size == 0 and self.feature_samples.size == 0:
            raise EmptyFeaturesEmptyTargetsException
        else:
            print self.clf.predict(sample)

    def evaluate_cross_validation(self, folds):
        """

        :param folds:
        :return:
        """
        if self.clf is None:
            raise NoClassifierException

        elif self.targets.size == 0 and self.feature_samples.size == 0:
            raise EmptyFeaturesEmptyTargetsException

        elif folds > len(self.feature_samples):
            raise FoldSizeToBigException(folds, self.feature_samples)

        else:
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

            acc_mean = (sum_values / n)

            return accuracy_list, acc_mean

    def evaluate_classification_report(self, fraction):
        if self.clf is None:
            raise NoClassifierException

        elif self.targets.size == 0 and self.feature_samples.size == 0:
            raise EmptyFeaturesEmptyTargetsException

        else:
            count = int(round((float(len(self.targets)) / float(100)) * float(fraction), 0))
            count2 = len(self.targets) - count

            # sollte auf 100 % /fraction trainiert werden, wird auch auf 100% getestet
            # wenn count2 0 ist (bei 100% count), dann wird self.targets[-count2:] zu self.targets[:]
            self.clf.fit(self.feature_samples[:count], self.targets[:count])
            predicted = self.clf.predict(self.feature_samples[-count2:])
            print(metrics.classification_report(self.targets[-count2:], predicted, target_names=["0", "1"]))
