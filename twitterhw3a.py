# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth) #uses my tokens to access twitter API

def main():
  cfg = { 
  "consumer_key"        : "K8TBYVBBnz5IDUHQCv5iQRhiI",
  "consumer_secret"     : "j8Y2BydLgNewQYN80z61ozzhafHhMaAeIBSKSnjYRBSPEz5Agg",
  "access_token"        : "796398976190844928-QTvOn7z0vzCBfrWyTx8dXkHHhpL8BYk",
  "access_token_secret" : "awAsuLWQwjZARUDf5Q9aO2L4Zv5UVzcLm9ZqQ9hc7C1qx" 
  }#All my access codes

  api = get_api(cfg) #access API
  tweet = "Mat Lefkofsky #UMSI-206 #Proj3" #words in the tweet
  status = api.update_with_media("Mat.png", tweet) #image in the tweet


if __name__ == "__main__":
  main()