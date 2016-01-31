"""
Model class
"""

import numpy as np
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.cross_validation import KFold
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from text_classifier.exceptions import ClassifierNotExistException
from text_classifier.exceptions import EmptyFeaturesEmptyTargetsException
from text_classifier.exceptions import NoClassifierException
from text_classifier.exceptions import FoldSizeToBigException
from text_classifier.head.data import Data, summarize_text, summarize_textpair

# Author Jan Wessling


class Model(object):
    """
    Text-classification-system with scikit-learn.
    For reference see: http://scikit-learn.org/stable/

    This Model class is based on Data class. Defines training
    and test data. Build classification model. Provides
    evaluation methods.

    Parameter
    ---------
    data : Data, optional
        Contains a data object with filled data.real_data.

    data_list : array, shape = [data1 object, data2 object, ...]
        Contains data objects with filled data.real_data.

    Attributes
    ----------
    clf : classifier object from sklean moduls.
        Contains a selected classifier object from sklean modul.
        see reference: http://scikit-learn.org/stable/supervised_learning.html#supervised-learning

    classifier_list : array, shape = [string classifier1 name, ...]
        Contains names of all available classification algorithms.

    __train_data_set : boolean
        Contains bolloean value that describes if train_data is set.

    train_data : Data
        Contains the data object that is set as training data.

    test_data : Data
        Contains the data object that is set as test data.

    train_targets : numpy array of shape [n_samples]
        Contains the class labels of training data. A sample is
        a textpair object, it's class label is found in textpair.target.

    train_samples : numpy array of shape [n_samples,n_features]
        Contains the feature values of the training data. A sample is
        a textpair object, it's feature values are found in textpair.features
        hash. After vectorize() them, they are stored in
        textpair.feature_vector.

    test_targets : numpy array of shape [n_samples]
        Contains the class labels of test data. A sample is
        a textpair object, it's class label is found in textpair.target.

    test_samples : numpy array of shape [n_samples,n_features]
        Contains the feature values of the test data. A sample is
        a textpair object, it's feature values are found in textpair.features
        hash. After vectorize() them, they are stored in
        textpair.feature_vector.
    """

    def __init__(self, data=None, data_list=None):
        self.clf = None

        if data is not None:
            self.data_list = [data]
        elif data_list is not None:
            self.data_list = data_list

        self.classifier_list = ["svm_linear", "svm_poly", "naive_bayes", "decision_tree", "nearest_centroid",
                                "k_neighbors", "radius_neighbors"]

        self.__train_data_set = False

    def set_train_data(self, data_name):
        """Setter for training data

        Walk through data_list and set data object with
        data.name as train_data.

        Parameter
        ---------
        data_name : string
            Contains the name of the data object, that should
            be set as train_data for the model.
        """
        data_in_list = False
        for data in self.data_list:
            if data.name == data_name:
                print data_name + " is in model_data_list"
                self.train_data = data
                self.train_samples, self.train_targets = self.fill_feature_target(data)
                print data_name + " is set as train_data"
                data_in_list = True
        if data_in_list:
            self.__train_data_set = True
        else:
            print data_name + " not in model_data_list "

    def set_test_data(self, data_name):
        """Setter for test data

        Walk through data_list and set data object with
        data.name as test_data.

        Notes
        -----
        Training data has to be set before test data, due to the fact
        that some features need skeletons that have to be build before seeing
        the test data.

        see reference: bag_of_pos.py, bag_of_words.py, tf_idf.py

        Parameter
        ---------
        data_name : string
            Contains the name of the data object, that should
            be set as test_data for the model.
        """
        if self.__train_data_set and self.train_data.name == data_name:
            self.test_data = self.train_data
            print "train_data and test_data from one data_set"
        elif not self.__train_data_set:
            print "please set train_data first"
        else:
            data_in_list = False
            for data in self.data_list:
                if data.name == data_name:
                    print data_name + " is in model_data_list"
                    self.test_data = data
                    self.test_samples, self.test_targets = self.fill_feature_target(data)
                    data_in_list = True
                    print data_name + " is set as test_data"
            if not data_in_list:
                print data_name + " not in model_data_list "

    def fill_feature_target(self, data):
        """ Fill the feature samples and target values.

        The classifier objects from sklearn need a numpy array for
        classification.

        Shape of the data class labels : numpy array of shape [n_samples]
        Shape of the data feature values : numpy array of shape [n_samples,n_features]

        Vectorize() textpair feature values, for building required numpy arrays.

        Note
        ----
        Check __train_data_set first, cause there is no need to attache the
        same features for test data manually in main.py. This will be performed
        automatically in here.

        Parameter
        ---------
        data : Data
            Contains a Data object that data.real_data should be vectorized.
        """
        sample_list = []
        target_list = []

        if self.__train_data_set:
            for feature in self.train_data.features_fit:
                if feature == "bag_of_words" or feature == "bag_of_pos" or feature == "tf_idf":
                    data.bow_model = self.train_data.bow_model

            print self.train_data.features_fit
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
        """ Setter for clf

        Building instances of classifier objects with corresponding name.

        Parameter
        ---------
        classifier_name : string
            Contains the corresponding name of the wanted classifier from
            sklearn.
        """
        if classifier_name == "svm_linear":
            self.clf = svm.SVC(kernel="linear", class_weight="auto")
        elif classifier_name == "svm_poly":
            self.clf = svm.SVC(kernel="poly", class_weight="auto")
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
        """ Train the model

        Training the classifier with the wanted fraction of the training data.

        Parameter
        -------
        fraction : int
            Contains a number from 0 to 100. Defines the fraction of the
            training data that will be used for training the classifier.
        """
        if self.clf is None:
            raise NoClassifierException
        elif self.train_targets.size == 0 and self.train_samples.size == 0:
            raise EmptyFeaturesEmptyTargetsException
        else:
            count = int(round((float(len(self.train_targets)) / float(100)) * float(fraction), 0))
            self.clf.fit(self.train_samples[:count], self.train_targets[:count])

    def predict(self, sample):
        """ Predict a given sample.

        Make a prediction for a given sample. Classifier needs a numpy array
        with the feature values of a sample.

        Note
        ----
        Requires a trained(fitted) model.

        Parameters
        ----------
        samples : numpy array of shape [n_samples,n_features]

        Returns
        -------
        self.clf.predict(sample) : int
            Contains the prediction value from the model. It is the predicted
            class label. For a textpair object it can be 0 or 1.
        """
        if self.clf is None:
            raise NoClassifierException
        elif self.test_targets.size == 0 and self.test_samples.size == 0:
            raise EmptyFeaturesEmptyTargetsException
        else:
            return self.clf.predict(sample)

    def evaluate_cross_validation(self, folds):
        """ Evaluation through a cross-validation

        Perform a cross-validation on the set training data
        with measured accuracy.
        It requires a given number of folds.

        Note
        ----
        cross validation is performed on the training data, not
        on the test data. So set your data as training data, if you
        want to perform a cross validation.

        Parameter
        ---------
        folds : int
            Contains the number of folds for the cross-validation.

        Returns
        -------
        accuracy_list : array, shape = [float acc score1, float acc score2, ...]
            Contains the accuracy scores of all iterations.

        acc_mean : float
            Contains the accuracy mean of the all iterations.
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
        """ A detailed classification report

        For an easy use to measure how well your trained model performs,
        the given method uses your set data objects and gives an accuracy
        score output on the shell.

        Note
        ----
        There are two scenarios :

            1. training data and test data are from the same data object.
                (means there names are the same !)
                - Normalization
            2. training data and test data are from different data objects.
                + Normalization

        The first scenario will use given fraction and divide the training
        data in train and test data for the classification. If fraction is
        100 then it will be trained and tested on the same data object.
        With a number of 80 fraction it will be trained on 80 percent and
        tested on 20 percent of the given data object. There is no
        Normalization for this scenario implemented !

        The second scenario needs a number of 100 fraction, to use the
        whole training data for the training ! Working with normalized
        values.

        Parameter
        ---------
        fraction : int
            Contains a number from 0 to 100. Defines the fraction of the
            training data that will be used for training the classifier.
        """
        if self.clf is None:
            raise NoClassifierException

        elif self.train_targets.size == 0 and self.train_samples.size == 0:
            raise EmptyFeaturesEmptyTargetsException

        else:
            # if trained on 100 % fraction, it will be tested on 100 %
            # fraction, than train and test data are the same

            # if count_predict is 0 (with 100% count_train), than
            # self.targets[-count_predict:] == self.targets[:] = True
            if self.test_data.name == self.train_data.name:

                print "train_data and test_data from one data_set"
                count_train = int(round((float(len(self.train_targets)) / float(100)) * float(fraction), 0))
                count_predict = len(self.train_targets) - count_train

                print "count_train:", count_train
                print "count_predict:", count_predict

                # Summarize placed in here, cause data objects are equal and
                # dived in this method. So training and test data are defined
                # in here.
                print "##########train_data summarize##########"
                summarize_textpair(self.train_data.real_data.values()[:count_train])

                print "##########test_data summarize##########"
                summarize_textpair(self.train_data.real_data.values()[-count_predict:])

                # setting train and test data
                train_samples = self.train_samples[:count_train]
                train_targets = self.train_targets[:count_train]
                test_samples = self.train_samples[-count_predict:]
                test_targets = self.train_targets[-count_predict:]

                # Training
                self.clf.fit(train_samples, train_targets)

                # Testing
                test_targets_predicted = self.clf.predict(test_samples)

                # calculating baseline
                null = 0
                eins = 0
                for i in test_targets:
                    if i == 0:
                        null += 1
                    else:
                        eins += 1
                if null > eins:
                    baseline = float(null)/(float(null)+float(eins))
                else:
                    baseline = float(eins)/(float(null)+float(eins))

                print "Anzahl 0:", null
                print "Anzahl 1:", eins
                print "Baseline:", baseline
                print "-------------------------------"

                # Calculating accuracy score of predicted samples
                print "accuracy_score: ", accuracy_score(test_targets, test_targets_predicted)

            else:
                # Normalization
                norma = preprocessing.normalize(self.train_samples)

                count_train = int(round((float(len(self.train_targets)) / float(100)) * float(fraction), 0))
                print "count_train:", count_train
                print "count_predict:", len(self.test_targets)

                # Setting train and test data

                # without normalization take this one instead
                # train_samples = self.train_samples[:count_train]
                train_samples = norma[:count_train]
                train_targets = self.train_targets[:count_train]

                # without normalization take this one instead
                # test_samples = self.test_samples
                test_samples = preprocessing.normalize(self.test_samples)
                test_targets = self.test_targets

                # Training
                self.clf.fit(train_samples, train_targets)

                # Testing
                test_targets_predicted = self.clf.predict(test_samples)

                # Calculating baseline
                null = 0
                eins = 0
                for i in test_targets:
                    if i == 0:
                        null += 1
                    else:
                        eins += 1
                if null > eins:
                    baseline = float(null)/(float(null)+float(eins))
                else:
                    baseline = float(eins)/(float(null)+float(eins))

                print "Anzahl 0:", null
                print "Anzahl 1:", eins
                print "Baseline:", baseline
                print "-------------------------------"

                # Calculating accuracy score of predicted samples
                print "accuracy_score: ", accuracy_score(test_targets, test_targets_predicted)
