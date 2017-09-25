from Scripts.SentimentClassifying import SentimentAnalyzer

s = SentimentAnalyzer.Analyzer()
s.PrintclassierAccuracies()




########################################################################################
####
####
# get the reviews from text files
####
####
########################################################################################

commonFilePath  = "E:/CDAP/FlaskProject/TextFiles/Outputs/"

ActingReview = open(commonFilePath  + "acting.txt", "r").read()
DirectingReview = open(commonFilePath  + "directing.txt", "r").read()
StoryReview = open(commonFilePath  + "storyline.txt", "r").read()
OtherReview = open(commonFilePath  + "other.txt", "r").read()

#print("setiment analysis for acting " + str(s.sentiment(ActingReview)))
#print("setiment analysis for directing " + str(s.sentiment(DirectingReview)))
#print("setiment analysis for story " + str(s.sentiment(StoryReview)))
#print("setiment analysis for other " + str(s.sentiment(OtherReview)))

print("setiment analysis for other " + str(s.sentiment("It's bad. but it is a good movie. cant say it's the best")))


