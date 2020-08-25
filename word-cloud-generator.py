import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


from google.colab import files
uploaded = files.upload()

# Get the data
log = pd.read_csv('Login.csv')


# Twitter API - Get this from Twitter Developer Tools
consumerKey = "##"
consumerSecret = "#"
accessToken = "#"
accessTokenSecret = "#"

# Create the authentication object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)

# Set the access token and access token secret

authenticate.set_access_token(accessToken, accessTokenSecret)

# Create the API object while passing in the auth information
api = tweepy.API(authenticate, wait_on_rate_limit= True)

# Extract 100 tweets from a Twitter User
posts = api.user_timeline(screen_name="realDonaldTrump", count= 200, lang = "en", tweet_mode="extended")

print ("200 recent tweets")
i = 1
for tweet in posts[0:200]:
  print(str(i) + ')' + tweet.full_text + '\n')
  i = i + 1

# Create a dataframe with a column called Tweets
df = pd.DataFrame ( [tweet.full_text for tweet in posts] , columns=['Tweets'])

df.head()  
