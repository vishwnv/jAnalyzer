import nltk
from nltk import word_tokenize
from Scripts.NegationAnalyzing import NegationAnalyzer


class EndPoint(object):

    def __init__(self):
        """
        Creating the Antonym Replacer object
        """

        self.b = NegationAnalyzer.AntonymReplacer()


    def mod_join(self , s):
        return "".join([s[0]] + ["{}".format(x)if x[0].lower() not in list('abcdefghijklmnopqrstuvwxyz') else" {}".format(x)  for x in s[1:] ])


    def retriveImportantTags(self, sent , antonymReplacer):
        tokenizedSent = word_tokenize(sent)
        posTagged = (nltk.pos_tag(tokenizedSent))
        for t in posTagged:
            if t[1] == "ADJ" or t[1] =="VB" or t[1] == "JJ":
                antonymReplacer.replace(t[0])
        return self.mod_join(self.b.replace_negations(tokenizedSent)) , sent


