from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize

antonyms = set()

# for syn in wordnet.synsets("good" , pos = None):
#     #print(syn)
#     for lemma in syn.lemmas():
#         print(lemma)
#         for antonym in lemma.antonyms():
#             print("anto name is " + antonym.name())
#             antonyms.add(antonym.name())
#     print("End of syn")

#print(antonyms)

commonFilePath = "../TextFiles/Outputs/"
AllSentences = []

try:
   directing = open(commonFilePath + "directing.txt", "r").read()
   acting = open(commonFilePath + "acting.txt", "r").read()
   storyline = open(commonFilePath + "storyline.txt", "r").read()
except Exception as e:
   print(e)

#print(storyline)


sentencesDictionary = {}

def GetAllSentecesListWithCats(file , cat):
    tokenized_sents = sent_tokenize(file)

    count = 0
    sentList = []
    for f in tokenized_sents:
        if cat == 'a':
            sentencesDictionary[0][count] = file
        elif cat == 's':
            sentencesDictionary[1][count] = file
        elif cat == 'd':
            sentencesDictionary[2][count] = file

        count += count

#GetAllSentecesListWithCats(acting , 'a' )
GetAllSentecesListWithCats(directing , 'd' )
#GetAllSentecesListWithCats(storyline , 's' )

import ast

#NEGLIST = ast.literal_eval(a)

for n in NEGLIST:
    print(n + "next")




