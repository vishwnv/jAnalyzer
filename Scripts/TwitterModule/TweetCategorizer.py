import nltk

class TweetCategorizer(object):

    ########################################################################
    #####
    #####
    #Mwthod to extract sentence which have specific word
    #####
    #####
    #########################################################################
    def extractSentenceToFile(text , testwordlist , file):
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

    ###########################################################################
    #####
    #####
    #Testing variables instantiazion
    #####
    #####
    ###########################################################################

    def categorize(self, text):

        storyline = ['story', 'storyline', 'plot']
        acting = ['acting', 'actors', 'act', 'roles', 'role playing', 'cast', 'acted']
        directing = ['directing', 'directors', 'direct', 'directed']

        storyfile = 'story_tweets.txt'
        actingfile = 'acting_tweets.txt'
        directingfile = 'directing_tweets.txt'

        TweetCategorizer.extractSentenceToFile(text, directing, directingfile)
        TweetCategorizer.extractSentenceToFile(text, acting, actingfile)
        TweetCategorizer.extractSentenceToFile(text, storyline, storyfile)

