import nltk
import ast

commonFilePath = "E:/CDAP/FlaskProject/TextFiles/Outputs/"
negatedSentences = open(commonFilePath + "inputNegations.txt", "r").read()
list = []
#list = eval('[' + negatedSentences + ']')
list = ast.literal_eval(negatedSentences)

for l in list:
    print(l[0])