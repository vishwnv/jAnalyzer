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


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            print("sentiment classifier is " + str(c))
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


class Analyzer(object):
    def __init__(self):
        self.short_pos = open("C:/Users/VISH_V/Desktop/datasets/positive.txt", "r").read()
        self.short_neg = open("C:/Users/VISH_V/Desktop/datasets/negative.txt", "r").read()

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

        ####for r in short_pos.split('\n'):
        ####    documents.append((r, "pos"))
        ####
        ####for r in short_pos.split('\n'):
        ####    documents.append((r, "neg"))
        ####
        ####all_words = []
        ####short_pos_words = word_tokenize(short_pos)
        ####short_neg_words = word_tokenize(short_neg)
        ####
        ####for w in short_pos_words:
        ####    all_words.append(w.lower())
        ####
        ####for w in short_neg_words:
        ####    all_words.append(w.lower())
        ####

        self.all_words = nltk.FreqDist(self.all_words)

        self.word_features = list(self.all_words.keys())[:5000]



        # print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
        featuresets = [(self.find_features(rev), category) for (rev, category) in self.documents]
        random.shuffle(featuresets)

        # posterior = prior occurences x liklihood / evidence

        # positive data example
        self.training_set = featuresets[:10000]
        self.testing_set = featuresets[10000:]

    def find_features(self,document):
        # words = set(document)
        words = word_tokenize(document)
        features = {}
        for w in self.word_features:
            features[w] = (w in words)

        return features

    def PrintclassierAccuracies(self):

        commonFilePath  = "E:/CDAP/FlaskProject/SavedClassifiers/SentimentClassifiers/"

        #classifier = nltk.NaiveBayesClassifier.train(training_set)
        classifier_f = open(commonFilePath + "naivebayes.pickle", "rb")
        self.classifier = pickle.load(classifier_f)
        classifier_f.close()

        print(" Original Naive Bayes Algo accuracy percent: ", (nltk.classify.accuracy(self.classifier, self.testing_set)) * 100)
        self.classifier.show_most_informative_features(15)
        # save_classifier = open("naivebayes.pickle" , "wb")
        # pickle.dump(classifier , save_classifier)
        # save_classifier.close()

        #
        ##
        ####

        # MNB_classifier = SklearnClassifier(MultinomialNB())
        # MNB_classifier.train(training_set)
        MNB_classifier_f = open(commonFilePath + "MNB.pickle", "rb")
        self.MNB_classifier = pickle.load(MNB_classifier_f)
        MNB_classifier_f.close()
        print(" MNB_classifier accuracy percent: ", (nltk.classify.accuracy(self.MNB_classifier, self.testing_set)) * 100)
        # save_MNBclassifier = open("MNB.pickle" , "wb")
        # pickle.dump(MNB_classifier , save_MNBclassifier)
        # save_MNBclassifier.close()






        # GaussianNB_classifier = SklearnClassifier(GaussianNB())
        # GaussianNB_classifier.train(training_set)
        # print (" GaussianNB_classifier accuracy percent: "  , (nltk.classify.accuracy(GaussianNB_classifier , testing_set))*100)
        ##


        # BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
        # BernoulliNB_classifier.train(training_set)
        BernoulliNB_classifier_f = open(commonFilePath + "Bernouli.pickle", "rb")
        self.BernoulliNB_classifier = pickle.load(BernoulliNB_classifier_f)
        BernoulliNB_classifier_f.close()
        print(" BernoulliNB_classifier accuracy percent: ", (nltk.classify.accuracy(self.BernoulliNB_classifier, self.testing_set)) * 100)
        # save_Bernouliclassifier = open("Bernouli.pickle" , "wb")
        # pickle.dump(BernoulliNB_classifier , save_Bernouliclassifier)
        # save_Bernouliclassifier.close()


        # LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
        # LogisticRegression_classifier.train(training_set)
        #LogisticRegression_classifier_f = open(commonFilePath + "Logistic.pickle", "rb")
        #self.LogisticRegression_classifier = pickle.load(LogisticRegression_classifier_f)
        #LogisticRegression_classifier_f.close()
        #print(" LogisticRegression_classifier accuracy percent: ",
        #      (nltk.classify.accuracy(self.LogisticRegression_classifier, self.testing_set)) * 100)
        # save_LogisticRegression = open("Logistic.pickle" , "wb")
        # pickle.dump(LogisticRegression_classifier , save_LogisticRegression)
        # save_LogisticRegression.close()


        # SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
        # SGDClassifier_classifier.train(training_set)
        #SGDClassifier_classifier_f = open(commonFilePath + "SGD.pickle", "rb")
        #self.SGDClassifier_classifier = pickle.load(SGDClassifier_classifier_f)
        #SGDClassifier_classifier_f.close()
        #print(" SGDClassifier_classifier accuracy percent: ",
        #      (nltk.classify.accuracy(self.SGDClassifier_classifier, self.testing_set)) * 100)
        # save_SGDClassifier_classifier = open("SGD.pickle" , "wb")
        # pickle.dump(SGDClassifier_classifier , save_SGDClassifier_classifier)
        # save_SGDClassifier_classifier.close()


        # SVC_classifier = SklearnClassifier(SVC())
        # SVC_classifier.train(training_set)
        #SVC_classifier_f = open(commonFilePath + "SVC.pickle", "rb")
        #self.SVC_classifier = pickle.load(SVC_classifier_f)
        #SVC_classifier_f.close()
        #print(" SVC_classifier accuracy percent: ", (nltk.classify.accuracy(self.SVC_classifier, self.testing_set)) * 100)
        # save_SVC_classifier = open("SVC.pickle" , "wb")
        # pickle.dump(SVC_classifier , save_SVC_classifier)
        # save_SVC_classifier.close()


        # LinearSVC_classifier = SklearnClassifier(LinearSVC())
        # LinearSVC_classifier.train(training_set)
        LinearSVC_classifier_f = open(commonFilePath + "LinearSVC.pickle", "rb")
        self.LinearSVC_classifier = pickle.load(LinearSVC_classifier_f)
        LinearSVC_classifier_f.close()
        print(" LinearSVC_classifier accuracy percent: ", (nltk.classify.accuracy(self.LinearSVC_classifier, self.testing_set)) * 100)
        # save_LinearSVC_classifier = open("LinearSVC.pickle" , "wb")
        # pickle.dump(LinearSVC_classifier , save_LinearSVC_classifier)
        # save_LinearSVC_classifier.close()


        # NuSVC_classifier = SklearnClassifier(NuSVC())
        # NuSVC_classifier.train(training_set)
        NuSVC_classifier_f = open(commonFilePath + "NuSVC.pickle", "rb")
        self.NuSVC_classifier = pickle.load(NuSVC_classifier_f)
        NuSVC_classifier_f.close()
        print(" NuSVC_classifier accuracy percent: ", (nltk.classify.accuracy(self.NuSVC_classifier, self.testing_set)) * 100)
        # save_NuSVC_classifier = open("NuSVC.pickle" , "wb")
        # pickle.dump(NuSVC_classifier , save_NuSVC_classifier)
        # save_NuSVC_classifier.close()

        self.voted_classifier = VoteClassifier(self.classifier,
                                          self.NuSVC_classifier,
                                          self.LinearSVC_classifier,
                                          #self.SGDClassifier_classifier,
                                          self.MNB_classifier,
                                          self.BernoulliNB_classifier
                                          #self.LogisticRegression_classifier
                                          )
    def printVotedClfAccuracies(self):

        print("Voted classifier accuracy:", (nltk.classify.accuracy(self.voted_classifier, self.testing_set)) * 100)

        print("Classfication: ", self.voted_classifier.classify(self.testing_set[0][0]), "Confidence : ",
              self.voted_classifier.confidence(self.testing_set[0][0]) * 100)
        print("Classfication: ", self.voted_classifier.classify(self.testing_set[1][0]), "Confidence : ",
              self.voted_classifier.confidence(self.testing_set[1][0]) * 100)
        print("Classfication: ", self.voted_classifier.classify(self.testing_set[2][0]), "Confidence : ",
              self.voted_classifier.confidence(self.testing_set[2][0]) * 100)
        print("Classfication: ", self.voted_classifier.classify(self.testing_set[3][0]), "Confidence : ",
              self.voted_classifier.confidence(self.testing_set[3][0]) * 100)


    def sentiment(self , text):
        feats = self.find_features(text)
        return self.voted_classifier.classify(feats), self.voted_classifier.confidence(feats)
