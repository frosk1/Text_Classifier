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
from sklearn import preprocessing
from text_classifier.exceptions import ClassifierNotExistException
from text_classifier.exceptions import EmptyFeaturesEmptyTargetsException
from text_classifier.exceptions import NoClassifierException
from text_classifier.exceptions import FoldSizeToBigException
from text_classifier.head.data import Data, summarize_text, summarize_textpair

__author__ = 'jan'

'''
Class Model :

'''


class Model(object):
    def __init__(self, data=None, data_list=None):
        self.clf = None
        if data is not None:
            self.data_list = [data]
        elif data_list is not None:
            self.data_list = data_list
        # self.data_list = self.fill_data(data, data_list)

        self.classifier_list = ["svm_linear", "svm_poly", "naive_bayes", "decision_tree", "nearest_centroid",
                                "k_neighbors", "radius_neighbors"]
        self.__train_data_set = False

    def set_train_data(self, data_name):
        data_in_list = False
        for data in self.data_list:
            if data.name == data_name:
                print data_name + " is in model_data_list "
                self.train_data = data
                self.train_samples, self.train_targets = self.fill_feature_target(data)
                data_in_list = True
        if data_in_list:
            self.__train_data_set = True
        else:
            print data_name + " not in model_data_list "

    def set_test_data(self, data_name):
        if self.__train_data_set and self.train_data.name == data_name:
            self.test_data = self.train_data
            print "train_data and test_data from one data_set"
        else:
            data_in_list = False
            for data in self.data_list:
                if data.name == data_name:
                    print data_name + " is in model_data_list "
                    self.test_data = data
                    self.test_samples, self.test_targets = self.fill_feature_target(data)
                    data_in_list = True
            if not data_in_list:
                print data_name + " not in model_data_list "

    # def fill_data(self, data, data_list):
    #     if type(data) is None and type(data_list) is None:
    #         return []
    #     elif type(data) is Data and type(data_list) is None:
    #         return [data]
    #     elif type(data) is None and type(data_list) is list:
    #         return data_list

    def fill_feature_target(self, data):
        """


        :rtype : tuple
        :return:
        """
        sample_list = []
        target_list = []

        if self.__train_data_set:
            for feature in self.train_data.features_fit:
                if feature == "bag_of_words":
                    data.bow_model = self.train_data.bow_model
            data.attach_feature_list(self.train_data.features_fit)

            for textpair in data.real_data.values():
                textpair.vectorize()
                target_list.append(textpair.target)
                sample_list.append(textpair.feature_vector)

            return np.array(sample_list), np.array(target_list)
        else:

            for textpair in data.real_data.values():
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
        elif self.train_targets.size == 0 and self.train_samples.size == 0:
            raise EmptyFeaturesEmptyTargetsException
        else:
            count = int(round((float(len(self.train_targets)) / float(100)) * float(fraction), 0))
            self.clf.fit(self.train_samples[:count], self.train_targets[:count])

    def predict(self, sample):
        """

        :param sample:
        :return:
        """
        if self.clf is None:
            raise NoClassifierException
        elif self.test_targets.size == 0 and self.test_samples.size == 0:
            raise EmptyFeaturesEmptyTargetsException
        else:
            return self.clf.predict(sample)

    def evaluate_cross_validation(self, folds):
        """

        :param folds:
        :return:
        """

        if self.clf is None:
            raise NoClassifierException

        elif self.train_targets.size == 0 and self.train_samples.size == 0:
            raise EmptyFeaturesEmptyTargetsException

        elif folds > len(self.train_samples):
            raise FoldSizeToBigException(folds, self.train_samples)

        else:
            kf = KFold(len(self.train_samples), n_folds=folds)
            accuracy_list = []

            for train, test in kf:
                x_train, x_test, y_train, y_test = self.train_samples[train], self.train_samples[test], \
                                                   self.train_targets[train], self.train_targets[test]

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
        # x = preprocessing.Normalizer()
        # norma = x.fit_transform(self.feature_samples, self.targets)
        # norma = preprocessing.normalize(self.feature_samples)
        # print norma

        if self.clf is None:
            raise NoClassifierException

        elif self.train_targets.size == 0 and self.train_samples.size == 0:
            raise EmptyFeaturesEmptyTargetsException

        else:
            # sollte auf 100 % /fraction trainiert werden, wird auch auf 100% getestet
            # wenn count_predict 0 ist (bei 100% count_train), dann wird self.targets[-count_predict:] zu self.targets[:]
            if self.test_data.name == self.train_data.name:
                print "train_data and test_data from one data_set"
                count_train = int(round((float(len(self.train_targets)) / float(100)) * float(fraction), 0))
                count_predict = len(self.train_targets) - count_train
                print "count_train:", count_train
                print "count_predict:", count_predict
                print "train_data summarize"
                summarize_text(self.train_data.real_data.values()[-count_predict:])

                train_samples = self.train_samples[:count_train]
                # train_samples = norma[:count_train]
                train_targets = self.train_targets[:count_train]
                test_samples = self.train_samples[-count_predict:]
                # test_samples = norma[-count_predict:]
                test_targets = self.train_targets[-count_predict:]

                self.clf.fit(train_samples, train_targets)
                test_targets_predicted = self.clf.predict(test_samples)

                print(metrics.classification_report(test_targets, test_targets_predicted, target_names=["0", "1"]))
                print "accuracy_score: ", accuracy_score(test_targets, test_targets_predicted)
            else:
                count_train = int(round((float(len(self.train_targets)) / float(100)) * float(fraction), 0))
                print "count_train:", count_train
                print "count_predict:", len(self.test_targets)
                print "test_data summarize"
                summarize_textpair(self.test_data.real_data.values())

                train_samples = self.train_samples[:count_train]
                train_targets = self.train_targets[:count_train]

                self.clf.fit(train_samples, train_targets)
                test_targets_predicted = self.clf.predict(self.test_samples)

                print(metrics.classification_report(self.test_targets, test_targets_predicted, target_names=["0", "1"]))
                print "accuracy_score: ", accuracy_score(self.test_targets, test_targets_predicted)