import nltk
import random
import pickle
from nltk.corpus import movie_reviews

from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.tokenize import word_tokenize

class CategoryClassf(object):
    def __init__(self):
        self.acting = open("E:/CDAP/FlaskProject/TextFiles/Datasets/Categories/acting.txt", "r").read()
        self.directing = open("E:/CDAP/FlaskProject/TextFiles/Datasets/Categories/directing.txt", "r").read()
        self.storyline = open("E:/CDAP/FlaskProject/TextFiles/Datasets/Categories/story.txt", "r").read()

        self.documents = []
        self.all_words = []

        self.loadDocument()


        self.all_words = nltk.FreqDist(self.all_words)

        word_features = list(self.all_words.keys())[:5000]

        def find_features(document):
            # words = set(document)
            words = word_tokenize(document)
            features = {}
            for w in word_features:
                features[w] = (w in words)

            return features

        # print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
        featuresets = [(find_features(rev), category) for (rev, category) in self.documents]
        random.shuffle(featuresets)
        # posterior = prior occurences x liklihood / evidence

        # positive data example
        print(len(featuresets))

        self.training_set = featuresets[:900]
        self.testing_set = featuresets[900:]




    def loadDocument(self):
        for p in self.directing.split('\n'):
            self.documents.append((p, "directing"))

        for p in self.storyline.split('\n'):
            self.documents.append((p, "storyline"))

        for p in self.acting.split('\n'):
            self.documents.append((p, "acting"))

        self.short_acting = word_tokenize(self.acting)
        self.short_directing = word_tokenize(self.directing)
        self.short_storyline = word_tokenize(self.storyline)

        for w in self.short_acting:
            self.all_words.append(w.lower())

        for w in self.short_directing:
            self.all_words.append(w.lower())

        for w in self.short_storyline:
            self.all_words.append(w.lower())


    def saveClassifiers(self):

        """
        Saving classifiers with pickling
        :return: 
        """

        classifierFilePath = "E:/CDAP/FlaskProject/SavedClassifiers/CategoryClassifiers/"

        classifier = nltk.NaiveBayesClassifier.train(self.training_set)
        save_classifier = open( classifierFilePath + "naivebayes.pickle", "wb")
        pickle.dump(classifier, save_classifier)
        save_classifier.close()

        MNB_classifier = SklearnClassifier(MultinomialNB())
        MNB_classifier.train(self.training_set)
        save_MNBclassifier = open(classifierFilePath + "MNB.pickle", "wb")
        pickle.dump(MNB_classifier, save_MNBclassifier)
        save_MNBclassifier.close()

        BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
        BernoulliNB_classifier.train(self.training_set)
        save_Bernouliclassifier = open(classifierFilePath + "Bernouli.pickle", "wb")
        pickle.dump(BernoulliNB_classifier, save_Bernouliclassifier)
        save_Bernouliclassifier.close()

        LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
        LogisticRegression_classifier.train(self.training_set)
        save_LogisticRegression = open(classifierFilePath + "Logistic.pickle", "wb")
        pickle.dump(LogisticRegression_classifier, save_LogisticRegression)
        save_LogisticRegression.close()

        SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
        SGDClassifier_classifier.train(self.training_set)
        save_SGDClassifier_classifier = open(classifierFilePath + "SGD.pickle", "wb")
        pickle.dump(SGDClassifier_classifier, save_SGDClassifier_classifier)
        save_SGDClassifier_classifier.close()

        SVC_classifier = SklearnClassifier(SVC())
        SVC_classifier.train(self.training_set)
        save_SVC_classifier = open(classifierFilePath + "SVC.pickle", "wb")
        pickle.dump(SVC_classifier, save_SVC_classifier)
        save_SVC_classifier.close()

        # LinearSVC_classifier = SklearnClassifier(LinearSVC())
        # LinearSVC_classifier.train(training_set)
        # save_LinearSVC_classifier = open("LinearSVC.pickle" , "wb")
        # pickle.dump(LinearSVC_classifier , save_LinearSVC_classifier)
        # save_LinearSVC_classifier.close()
        #
        # NuSVC_classifier = SklearnClassifier(NuSVC())
        # NuSVC_classifier.train(training_set)
        # save_NuSVC_classifier = open("NuSVC.pickle" , "wb")
        # pickle.dump(NuSVC_classifier , save_NuSVC_classifier)
        # save_NuSVC_classifier.close()



