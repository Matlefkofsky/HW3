# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy
print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  cfg = { 
  "consumer_key"        : "K8TBYVBBnz5IDUHQCv5iQRhiI",
  "consumer_secret"     : "j8Y2BydLgNewQYN80z61ozzhafHhMaAeIBSKSnjYRBSPEz5Agg",
  "access_token"        : "796398976190844928-QTvOn7z0vzCBfrWyTx8dXkHHhpL8BYk",
  "access_token_secret" : "awAsuLWQwjZARUDf5Q9aO2L4Zv5UVzcLm9ZqQ9hc7C1qx" 
  }
  api = get_api(cfg)
  tweet = "Testing 1231"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
	main()



