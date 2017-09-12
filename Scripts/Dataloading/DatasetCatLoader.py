import nltk

class CategoryDatasetCreator(object):

    def __init__(self):
        self.storyline = ['story', 'storyline', 'plot']
        self.acting = ['acting', 'actors', 'act', 'roles', 'role playing', 'cast', 'acted']
        self.directing = ['directing', 'directors', 'direct', 'directed']

        self.storyfile = 'E:/CDAP/FlaskProject/TextFiles/Datasets/Categories/story.txt'
        self.actingfile = 'E:/CDAP/FlaskProject/TextFiles/Datasets/Categories/acting.txt'
        self.directingfile = 'E:/CDAP/FlaskProject/TextFiles/Datasets/Categories/directing.txt'

        self.short_pos = open("E:/CDAP/FlaskProject/TextFiles/Datasets/SentimentReviews/positive.txt", "r").read()
        self.short_neg = open("E:/CDAP/FlaskProject/TextFiles/Datasets/SentimentReviews/negative.txt", "r").read()

    """
    My method to extract sentence which have specific word
    """

    def ExtractSentenceToFile(self, text , testwordlist , file):
        sent_text = nltk.sent_tokenize(text) # this gives us a list of sentences
        # now loop over each sentence and tokenize it separately
        for sentence in sent_text:
                tokenized_text = nltk.word_tokenize(sentence)
                for word in tokenized_text:
                    if word in testwordlist:
                        print (tokenized_text)
                        with open(file, "a+") as text_file:
                            tokenized_text_string = ' '.join(tokenized_text)
                            print(tokenized_text_string, file=text_file)
                        break

    def ClearFiles(self):
        open(self.storyfile, "w").close()
        open(self.actingfile, "w").close()
        open(self.directingfile, "w").close()

    def DoExtractionToTextFiles(self):
        """
            First clearing the existing data on the data set files
        """
        self.ClearFiles()

        """
            Loading data set text files
        """
        self.ExtractSentenceToFile(self.short_pos, self.directing, self.directingfile)
        self.ExtractSentenceToFile(self.short_pos, self.acting, self.actingfile)
        self.ExtractSentenceToFile(self.short_pos, self.storyline, self.storyfile)
        self.ExtractSentenceToFile(self.short_neg, self.directing, self.directingfile)
        self.ExtractSentenceToFile(self.short_neg, self.acting, self.actingfile)
        self.ExtractSentenceToFile(self.short_neg, self.storyline, self.storyfile)

