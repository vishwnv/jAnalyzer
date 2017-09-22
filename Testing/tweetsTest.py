from Scripts.TwitterModule import TwitterParser
from Scripts.TwitterModule import TweetCategorizer

def main():
    count = 0
    # creating object of TwitterClient Class
    api = TwitterParser.TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query='Superman')
    # Create tweet categorizer
    catogizer = TweetCategorizer.TweetCategorizer()


    print("\n\n tweetsss:")
    for tweet in tweets:
        count = count + 1
        # call function to categorize
        catogizer.categorize(tweet['text'])
        print(tweet['text'])
        print(count)

if __name__ == "__main__":
    # calling main function
    main()
