import nltk
from nltk import word_tokenize
from Scripts.NegationAnalyzing import NegationAnalyzer
from Scripts.NegationAnalyzing import NegationEndpoint
from nltk.tokenize import sent_tokenize

"""
Creating the Antonym Replacer object
"""
a = NegationAnalyzer.AntonymReplacer()
b = NegationAnalyzer.AntonymReplacer()
#print(a.replace('good'))
#print(a.replace('agree'))
sent = "Let's not disagree on this"
tokenizedSent = word_tokenize(sent)
words = a.replace_negations(tokenizedSent)
#print(words)



text = word_tokenize("Let's not disagree on this")
#print(text)
#print(nltk.pos_tag(text))

def mod_join(s):
    return "".join([s[0]] + ["{}".format(x)if x[0].lower() not in list('abcdefghijklmnopqrstuvwxyz') else" {}".format(x)  for x in s[1:] ])


def retriveAdjectives(sent , antonymReplacer):
    tokenizedSent = word_tokenize(sent)
    posTagged = (nltk.pos_tag(tokenizedSent))
    for t in posTagged:
        if t[1] == "ADJ" or t[1] =="VB" or t[1] == "JJ":
            antonymReplacer.replace(t[0])
    print(mod_join(a.replace_negations(tokenizedSent)))


def ConvertNegations1(text):
    endpoint = NegationEndpoint.EndPoint
    tokenized_sent = sent_tokenize(text)

    for t in tokenized_sent:
        print(t)


def ConvertNegations(text):
    covertedSentencs = []
    convertedOutput = []
    a = NegationAnalyzer.AntonymReplacer()

    endpoint = NegationEndpoint.EndPoint()
    tokenized_sent = sent_tokenize(text)

    for t in tokenized_sent:
        if (endpoint.retriveImportantTags(t, a)is not None and endpoint.retriveImportantTags(t, a)[0] != endpoint.retriveImportantTags(t, a)[1] ):
            covertedSentencs.append(endpoint.retriveImportantTags(t, a))
            convertedOutput.append(endpoint.retriveImportantTags(t, a)[0])
        else:
            convertedOutput.append(endpoint.retriveImportantTags(t, a)[1])
    print(convertedOutput)


#retriveAdjectives("Let's not disagree on this. " , b )
s= "Let's not disagree on this. Kevin has directed many movies in a good way. actors have done a tremendous job. acting of Niel Grass is remarkable. Actions are well planed and very much likable. There is no thrilling moments in the plot. The story of this movie is very poor storywriting."

ConvertNegations(s)