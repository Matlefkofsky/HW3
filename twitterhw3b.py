# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

consumer_key = 'K8TBYVBBnz5IDUHQCv5iQRhiI'
consumer_secret = 'j8Y2BydLgNewQYN80z61ozzhafHhMaAeIBSKSnjYRBSPEz5Agg'
access_token = '796398976190844928-QTvOn7z0vzCBfrWyTx8dXkHHhpL8BYk'
access_token_secret = 'awAsuLWQwjZARUDf5Q9aO2L4Zv5UVzcLm9ZqQ9hc7C1qx' #my tokens for twitter account

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search_term = input("Enter a term to search on twitter ") ##uses an input to prompt user for twitter term to search for
for each in tweepy.Cursor(api.search, q=search_term, result_type = 'recent', include_entities=True,lang = 'en').items(100): #takes top 100 tweets using my search_term
  print (each.text) #searches terms and returns results
  

text = TextBlob(each.text) #puts all the text in a blob
subjectivity = text.sentiment.subjectivity #finds subjectivity
polarity = text.sentiment.polarity #finds polarity
print("Average subjectivity is ", subjectivity)
print("Average polarity is ", polarity)