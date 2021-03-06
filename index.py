from textblob import TextBlob
import tweepy

QUERY = "commodities"
CONSUMER_KEY = "YHF7RMi5tbptR48PdI4o1LSgF"
CONSUMER_SECRET = "L96FftoZYt6myWjuBKg6XThGe2mtHWfKFs73pMiVurzbEt1EUS"
ACCESS_TOKEN = "2852578340-gIkkRqfOLSbm0e4rhbqZP9IZPbFhiZVJza6sEMI"
ACCESS_TOKEN_SECRET = "RRPmryinxuZbc99gonANA5KMAHAK47aAaG2fF6QtkWbd8"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
extractor = tweepy.API(auth)

print('\n\nStrongly for(FF)')
print('\nFor(F)')
print('\nAgainst(A)')
print('\nStrongly against(AA)\n\n')

all_tweets = extractor.search(q=QUERY, count=300)
with open('dataset.csv', 'w') as file:
    for tweet in all_tweets:
        tweet = tweet._json
        tweet_text_content = str(tweet["text"])
        tweet_wiki = TextBlob(tweet_text_content)

        tweet_sentiment_subjectivity = tweet_wiki.sentiment.subjectivity
        tweet_sentiment_polarity = tweet_wiki.sentiment.polarity
        tweet_retweet_count = int(tweet["retweet_count"])
        tweet_author_followers_count = int(tweet["user"]["followers_count"])

        print(tweet_text_content+" (FF or F or A or AA) : ")
        label = input()
        label = label.upper()
        
        file.write("{},{},{},{},{}\n".format(tweet_sentiment_polarity,tweet_sentiment_subjectivity, tweet_author_followers_count, tweet_retweet_count,label))
    file.close()

print('Shoo now')