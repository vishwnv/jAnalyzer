import nltk
import random
import pickle
from nltk.corpus import movie_reviews

from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.tokenize import word_tokenize

from nltk.classify import ClassifierI
from statistics import mode

class SMClassfier(object):
    def __init__(self):
        self.short_pos = open("E:/CDAP/FlaskProject/TextFiles/Datasets/SentimentReviews/positive.txt", "r").read()
        self.short_neg = open("E:/CDAP/FlaskProject/TextFiles/Datasets/SentimentReviews/negative.txt", "r").read()

        self.documents = []

        # j is adject, r is adverb, and v is verb
        # allowed_word_types = ["J" , "R" , "V"]
        allowed_word_types = ["J"]
        self.all_words = []

        for p in self.short_pos.split('\n'):
            self.documents.append((p, "pos"))
            words = word_tokenize(p)
            pos = nltk.pos_tag(words)
            for w in pos:
                if w[1][0] in allowed_word_types:
                    self.all_words.append(w[0].lower())

        for p in self.short_neg.split('\n'):
            self.documents.append((p, "neg"))
            words = word_tokenize(p)
            pos = nltk.pos_tag(words)
            for w in pos:
                if w[1][0] in allowed_word_types:
                    self.all_words.append(w[0].lower())

        self.all_words = nltk.FreqDist(self.all_words)

        self.word_features = list(self.all_words.keys())[:5000]

        # print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
        self.featuresets = [(self.find_features(rev), category) for (rev, category) in self.documents]
        random.shuffle(self.featuresets)

        # posterior = prior occurences x liklihood / evidence

        # positive data example
        self.training_set = self.featuresets[:10000]
        self.testing_set = self.featuresets[10000:]


    def find_features(self,document):
        # words = set(document)
        words = word_tokenize(document)
        features = {}
        for w in self.word_features:
            features[w] = (w in words)

        return features



    def saveClassifiers(self):

        """
            Saving classifiers with pickling
        """
        classiferFilePath = "E:/CDAP/FlaskProject/SavedClassifiers/SentimentClassifiers/"


        classifier = nltk.NaiveBayesClassifier.train(self.training_set)
        save_classifier = open(classiferFilePath + "naivebayes.pickle", "wb")
        pickle.dump(classifier, save_classifier)
        save_classifier.close()

        MNB_classifier = SklearnClassifier(MultinomialNB())
        MNB_classifier.train(self.training_set)
        save_MNBclassifier = open(classiferFilePath + "MNB.pickle", "wb")
        pickle.dump(MNB_classifier, save_MNBclassifier)
        save_MNBclassifier.close()

        BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
        BernoulliNB_classifier.train(self.training_set)
        save_Bernouliclassifier = open(classiferFilePath + "Bernouli.pickle", "wb")
        pickle.dump(BernoulliNB_classifier, save_Bernouliclassifier)
        save_Bernouliclassifier.close()

        LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
        LogisticRegression_classifier.train(self.training_set)
        save_LogisticRegression = open(classiferFilePath + "Logistic.pickle", "wb")
        pickle.dump(LogisticRegression_classifier, save_LogisticRegression)
        save_LogisticRegression.close()

        SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
        SGDClassifier_classifier.train(self.training_set)
        save_SGDClassifier_classifier = open("classiferFilePath + .pickle", "wb")
        pickle.dump(SGDClassifier_classifier, save_SGDClassifier_classifier)
        save_SGDClassifier_classifier.close()

        SVC_classifier = SklearnClassifier(SVC())
        SVC_classifier.train(self.training_set)
        save_SVC_classifier = open(classiferFilePath + "SVC.pickle", "wb")
        pickle.dump(SVC_classifier, save_SVC_classifier)
        save_SVC_classifier.close()

        LinearSVC_classifier = SklearnClassifier(LinearSVC())
        LinearSVC_classifier.train(self.training_set)
        save_LinearSVC_classifier = open(classiferFilePath + "LinearSVC.pickle", "wb")
        pickle.dump(LinearSVC_classifier, save_LinearSVC_classifier)
        save_LinearSVC_classifier.close()

        NuSVC_classifier = SklearnClassifier(NuSVC())
        NuSVC_classifier.train(self.training_set)
        save_NuSVC_classifier = open(classiferFilePath + "NuSVC.pickle", "wb")
        pickle.dump(NuSVC_classifier, save_NuSVC_classifier)
        save_NuSVC_classifier.close()