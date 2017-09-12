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


class CatClassF(object):
    def __init__(self):
        self.short_pos = open("E:/CDAP/FlaskProject/TextFiles/Datasets/SentimentReviews/positive.txt", "r").read()
        self.short_neg = open("E:/CDAP/FlaskProject/TextFiles/Datasets/SentimentReviews/negative.txt", "r").read()

        self.acting = open("E:/CDAP/FlaskProject/TextFiles/Datasets/Categories/acting.txt", "r").read()
        self.directing = open("E:/CDAP/FlaskProject/TextFiles/Datasets/Categories/directing.txt", "r").read()
        self.storyline = open("E:/CDAP/FlaskProject/TextFiles/Datasets/Categories/story.txt", "r").read()

        self.documents = []
        self.all_words = []

        for p in self.directing.split('\n'):
            self.documents.append((p, "directing"))
        for p in self.acting.split('\n'):
            self.documents.append((p, "acting"))
        for p in self.storyline.split('\n'):
            self.documents.append((p, "storyline"))

        self.short_acting = word_tokenize(self.acting)
        self.short_directing = word_tokenize(self.directing)
        self.short_storyline = word_tokenize(self.storyline)

        for w in self.short_acting:
            self.all_words.append(w.lower())

        for w in self.short_directing:
            self.all_words.append(w.lower())

        for w in self.short_storyline:
            self.all_words.append(w.lower())

        self.all_words = nltk.FreqDist(self.all_words)
        self.word_features = list(self.all_words.keys())[:5000]
        # print(self.word_features)


        # print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
        self.featuresets = [(self.find_features(rev), category) for (rev, category) in self.documents]
        random.shuffle(self.featuresets)

        # posterior = prior occurences x liklihood / evidence

        # positive data example
        self.training_set = self.featuresets[:900]
        self.testing_set = self.featuresets[900:]



    """
        Method to find features
    """
    def find_features(self, document):
        # words = set(document)
        words = word_tokenize(document)
        features = {}
        for w in self.word_features:
            features[w] = (w in words)

        return features

    def loadClassifiers(self):

        classiferFilePath = "E:/CDAP/FlaskProject/SavedClassifiers/CategoryClassifiers/"

        # classifier = nltk.NaiveBayesClassifier.train(training_set)
        classifier_f = open(classiferFilePath + "naivebayes.pickle", "rb")
        self.classifier = pickle.load(classifier_f)
        classifier_f.close()

        print(" Original Naive Bayes Algo accuracy percent: ", (nltk.classify.accuracy(self.classifier, self.testing_set)) * 100)
        self.classifier.show_most_informative_features(40)
        # save_classifier = open("naivebayes.pickle" , "wb")
        # pickle.dump(classifier , save_classifier)
        # save_classifier.close()

        #
        ##
        ####

        # MNB_classifier = SklearnClassifier(MultinomialNB())
        # MNB_classifier.train(training_set)
        MNB_classifier_f = open(classiferFilePath + "MNB.pickle", "rb")
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
        BernoulliNB_classifier_f = open(classiferFilePath + "Bernouli.pickle", "rb")
        self.BernoulliNB_classifier = pickle.load(BernoulliNB_classifier_f)
        BernoulliNB_classifier_f.close()
        print(" BernoulliNB_classifier accuracy percent: ",
              (nltk.classify.accuracy(self.BernoulliNB_classifier, self.testing_set)) * 100)
        # save_Bernouliclassifier = open("Bernouli.pickle" , "wb")
        # pickle.dump(BernoulliNB_classifier , save_Bernouliclassifier)
        # save_Bernouliclassifier.close()


        # LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
        # LogisticRegression_classifier.train(training_set)
        LogisticRegression_classifier_f = open(classiferFilePath + "Logistic.pickle", "rb")
        self.LogisticRegression_classifier = pickle.load(LogisticRegression_classifier_f)
        LogisticRegression_classifier_f.close()
        print(" LogisticRegression_classifier accuracy percent: ",
              (nltk.classify.accuracy(self.LogisticRegression_classifier, self.testing_set)) * 100)
        # save_LogisticRegression = open("Logistic.pickle" , "wb")
        # pickle.dump(LogisticRegression_classifier , save_LogisticRegression)
        # save_LogisticRegression.close()


        # SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
        # SGDClassifier_classifier.train(training_set)
        SGDClassifier_classifier_f = open(classiferFilePath + "SGD.pickle", "rb")
        self.SGDClassifier_classifier = pickle.load(SGDClassifier_classifier_f)
        SGDClassifier_classifier_f.close()
        print(" SGDClassifier_classifier accuracy percent: ",
              (nltk.classify.accuracy(self.SGDClassifier_classifier, self.testing_set)) * 100)
        # save_SGDClassifier_classifier = open("SGD.pickle" , "wb")
        # pickle.dump(SGDClassifier_classifier , save_SGDClassifier_classifier)
        # save_SGDClassifier_classifier.close()


        # SVC_classifier = SklearnClassifier(SVC())
        # SVC_classifier.train(training_set)
        SVC_classifier_f = open(classiferFilePath + "SVC.pickle", "rb")
        self.SVC_classifier = pickle.load(SVC_classifier_f)
        SVC_classifier_f.close()
        print(" SVC_classifier accuracy percent: ", (nltk.classify.accuracy(self.SVC_classifier, self.testing_set)) * 100)
        # save_SVC_classifier = open("SVC.pickle" , "wb")
        # pickle.dump(SVC_classifier , save_SVC_classifier)
        # save_SVC_classifier.close()

    def VoteCFs(self):
        self.voted_classifier = VoteClassifier(self.classifier,
                                          self.SGDClassifier_classifier,
                                          self.MNB_classifier,
                                          self.BernoulliNB_classifier,
                                          self.LogisticRegression_classifier
                                          )

    def categoryClassification(self,text):
        features = self.find_features(text)
        return self.voted_classifier.classify(features), self.voted_classifier.confidence(features)

    def extractSentenceToFile(self,text):
        fileTobeWritten = 'E:/CDAP/FlaskProject/TextFiles/Outputs/'
        sent_text = nltk.sent_tokenize(text)  # this gives us a list of sentences
        # now loop over each sentence and tokenize it separately
        for sentence in sent_text:
            cat, conf = self.categoryClassification(sentence)
            if conf >= 0.5:
                fileTobeWritten = fileTobeWritten + cat + '.txt'
                # print(fileTobeWritten)
            else:
                fileTobeWritten = 'other.txt'
            with open(fileTobeWritten, "a+") as text_file:
                # tokenized_text_string = ' '.join(sentence)
                print(sentence, file=text_file)
            print("category is " + str(cat) + "confidence is " + str(conf))


    def DoClassification(self):
        self.loadClassifiers()
        self.VoteCFs()

        #review = open("E:/CDAP/FlaskProject/Testing/TestInputs/reviewToBeTested.txt", "r").read()
        #self.extractSentenceToFile(review)
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












# print("Voted classifier accuracy:", (nltk.classify.accuracy(voted_classifier, testing_set)) * 100)
#
# print("Classfication: ", voted_classifier.classify(testing_set[0][0]), "Confidence : ",
#       voted_classifier.confidence(testing_set[0][0]) * 100)
# print("Classfication: ", voted_classifier.classify(testing_set[1][0]), "Confidence : ",
#       voted_classifier.confidence(testing_set[1][0]) * 100)
# print("Classfication: ", voted_classifier.classify(testing_set[2][0]), "Confidence : ",
#       voted_classifier.confidence(testing_set[2][0]) * 100)
# print("Classfication: ", voted_classifier.classify(testing_set[3][0]), "Confidence : ",
#       voted_classifier.confidence(testing_set[3][0]) * 100)





#from textblob.classifiers import NaiveBayesClassifier
#cl = NaiveBayesClassifier(documents)

#def categoryClassificationNB(text):
    #return cl.classify(text) , 2







#print ("review sentence is " + str(categoryClassification("acting was below average.")))