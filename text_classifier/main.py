__author__ = 'jan'
from text_classifier.body.text import Text
from text_classifier.body.korpus import Korpus
from text_classifier.body.textpair import TextPair
from text_classifier.head.data import Data
from text_classifier.model.model import Model
from sklearn.datasets.twenty_newsgroups import fetch_20newsgroups
from sklearn import metrics
from sklearn.cross_validation import KFold
from sklearn.cross_validation import PredefinedSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
import math
import os
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from text_classifier.attributes.bag_of_words import BagOfWords#
import re

if __name__ == '__main__':
    text_1 = Text(1, "Tim mag viele tolle sachen,)%$.")
    text_2 = Text(2, "Hallo heute ist ein schoener tag")
    file = "/home/jan/Development/Korpus/ZA/Finales_Korpus/Text_Korpus_aktuell.txt"
    file2 = "/home/jan/annotation_test.txt"
    file3 = "/home/jan/annotation_test_jan.txt"



    k1 = Korpus("Test")
    k1.insert_from_file(file)
    #print k1.size
    #print text_1
    #print k1.get_text(50)
    #print k1.get_text(50).get_tokenlist()
    #pair1 = TextPair(text_1, text_2, 1)
    #print pair1
    data1 = Data(k1)
    data1.add_anno(file2)
    #print data1.real_data_size
    #print data1
    #data1.attach_feature("standard_attribute")
    data1.attach_feature("bag_of_words")
    #feature_list = ["bag_of_words", "tf_idf"]
    #data1.attach_feature_list(feature_list)
    #data1.attach_feature("tf_idf")

    #for i in data1.real_data.values():
    #    print i.text1.features
    #    print i.text2.features
    # print data1.real_data.values()[1].text1.features
    # print data1.real_data.values()[1].text2.features
    # data1.real_data.values()[0].text1.vectorize()
    # print data1.real_data.values()[0].text1.feature_vector
    #data1.real_data.values()[0].text1.vectorize()
    #data1.real_data.values()[0].text2.vectorize()
    #print(data1.real_data.values()[0].text1.feature_vector)
    #print(data1.real_data.values()[0].text2.feature_vector)
    #(data1.real_data.values()[0].vectorize())
    #print(data1.real_data.values()[0].feature_vector)
    #for i in data1.real_data.values():
     #   print i

    #print data1.real_data
    model1 = Model(data1)
    model1.set_classifier("svm")





    #np.mean(predicted == twenty_test.target)
    #model1.set_classifier("naive_bayes")
    #model1.set_classifier("decision_tree")
    #model1.set_classifier("nearest_centroid")

    y = model1.evaluate_classification_report(80)
    x = model1.evaluate_cross_validation(10)

    print y
    print x[0]
    print x[1]
    # kf = KFold(13, n_folds=4)
    #
    # for train, test in kf:
    #     print "train",train," test ",test
    #     print "len train", len(train), "test",len(test)
    # X = np.array([[1, 2], [3, 4], [2, 7], [5, 6]])
    # y = np.array([0, 0, 1, 1])
    # ps = PredefinedSplit(test_fold=[-1,0,-1,1])
    # print len(ps)
    #
    # print(ps)
    #
    # for train_index, test_index in ps:
    #     print("TRAIN:", train_index, "TEST:", test_index)
    #     X_train, X_test = X[train_index], X[test_index]
    #     y_train, y_test = y[train_index], y[test_index]
    #     #print("X_Train: ", X_train, "Y_train", y_train)
    #     #print("X_Test: ", X_test, "Y_test", y_test)
    # X_train, X_test, y_train, y_test = cross_validation.train_test_split(
    # model1.feature_samples, model1.targets, test_size=0.4, random_state=0)
    #
    #
    #
    # clf = model1.clf.fit(X_train, y_train)
    # print clf.score(X_test, y_test)

    #scores = cross_validation.cross_val_score(
    #model1.clf, model1.feature_samples, model1.targets, cv=10, scoring='accuracy')
    #print scores
    #print scores.mean()

    #print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    #set2 = set()
    #set1 = {"red","yellow"}
    #set1.add("red")
    #print set2.add("hallo")
    #print set2

    #textpair = data1.real_data.values()[0]
    #text1 = textpair.text1
    #text = textpair.text1.text
    #print text
    #corpus = [text]
    #corpus.append("new it was")
    #text_decode = text.decode("utf-8")
    #vectorizer = CountVectorizer(min_df=1)
    #X = vectorizer.fit_transform(corpus)
    #print type(X)
    #print X.toarray()
    #print vectorizer.get_feature_names()
    #print vectorizer.transform(['new it was']).toarray()
    #dict = {"bagofwords":1,"attribute":1.5}
    #vec = DictVectorizer()
    #fe = vec.fit_transform(dict).toarray()
    #print fe
    #fe_list = [fe]
    #s = X.toarray()
    #s1= np.array(((2,3),(2,3)))
    #print s1
    #s2 = np.array((2,2))
    #print s2
    #s3 = np.append(s1,s2, axis=0)
    #num = np.array(list)
    #print num
    #print s3

    #dic_test = {1:0}

