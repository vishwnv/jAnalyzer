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



acting = open("E:/CDAP/PyCharmProjects/modules/TestScripts/acting.txt" , "r").read()
directing = open("E:/CDAP/PyCharmProjects/modules/TestScripts/directing.txt" , "r").read()
storyline = open("E:/CDAP/PyCharmProjects/modules/TestScripts/story.txt" , "r").read()


documents = []
all_words = []


for p in directing.split('\n'):
    documents.append((p, "directing"))

for p in storyline.split('\n'):
    documents.append((p, "storyline"))

for p in acting.split('\n'):
    documents.append((p, "acting"))


short_acting= word_tokenize(acting)
short_directing = word_tokenize(directing)
short_storyline = word_tokenize(storyline)

for w in short_acting:
    all_words.append(w.lower())

for w in short_directing:
    all_words.append(w.lower())

for w in short_storyline:
    all_words.append(w.lower())

#random.shuffle(documents)
with open("testdocuments.txt", "a+") as text_file:
    # tokenized_text_string = ' '.join(sentence)
    print(documents, file=text_file)

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]


def find_features(document):
    # words = set(document)
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(rev), category) for (rev, category) in documents]
random.shuffle(featuresets)
# posterior = prior occurences x liklihood / evidence

# positive data example
print(len(featuresets))
with open("featuresetdoc.txt", "a+") as text_file:
    # tokenized_text_string = ' '.join(sentence)
    print(featuresets, file=text_file)

training_set = featuresets[:900]
testing_set = featuresets[900:]



###########################################################################
#
#
#Saving classifiers with pickling
#
#
############################################################################


classifier = nltk.NaiveBayesClassifier.train(training_set)
save_classifier = open("naivebayes.pickle" , "wb")
pickle.dump(classifier , save_classifier)
save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
save_MNBclassifier = open("MNB.pickle" , "wb")
pickle.dump(MNB_classifier , save_MNBclassifier)
save_MNBclassifier.close()

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
save_Bernouliclassifier = open("Bernouli.pickle" , "wb")
pickle.dump(BernoulliNB_classifier , save_Bernouliclassifier)
save_Bernouliclassifier.close()

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
save_LogisticRegression = open("Logistic.pickle" , "wb")
pickle.dump(LogisticRegression_classifier , save_LogisticRegression)
save_LogisticRegression.close()


SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
save_SGDClassifier_classifier = open("SGD.pickle" , "wb")
pickle.dump(SGDClassifier_classifier , save_SGDClassifier_classifier)
save_SGDClassifier_classifier.close()

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
save_SVC_classifier = open("SVC.pickle" , "wb")
pickle.dump(SVC_classifier , save_SVC_classifier)
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