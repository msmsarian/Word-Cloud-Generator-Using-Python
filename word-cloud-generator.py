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

#Clean the Text

#Create a function to clean the tweets
def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) # Remove @mentions
    text = re.sub(r'#', '', text) # Remove the '#' symbol
    text = re.sub(r'RT[\s]+', '', text) # Remove RT
    text = re.sub(r'https?:\/\/\S+', '', text) # Remove the Hyper Link

    return text

# Cleaning the text

df['Tweets']= df['Tweets'].apply(cleanTxt)

#Show the cleaned text
df

# Create a function to get the subjectivity
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

# Get polarity

def getPolarity(text):
    return TextBlob(text).sentiment.polarity

# Create two new columns

df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
df['Polarity'] = df['Tweets'].apply(getPolarity)

# Show the new dataframe with the new columns
df

# Word Cloud
allWords = ' '.join( [twts for twts in df['Tweets']])
wordCloud = WordCloud(width = 500, height = 300, random_state = 21, max_font_size = 119).generate(allWords)

plt.imshow(wordCloud, interpolation = "bilinear")
plt.axis('off')
plt.show()  
