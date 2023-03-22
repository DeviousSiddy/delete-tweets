import json
import tweepy

# read keys and tokens from file
with open("keys.txt", "r") as f:
    lines = f.readlines()
    consumer_key = lines[0].strip()
    consumer_secret = lines[1].strip()
    access_token = lines[2].strip()
    access_token_secret = lines[3].strip()

# authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the tweepy API client
api = tweepy.API(auth)

# Load the tweets from the backup file
with open('tweets.js', 'r', encoding='utf-8') as f:
    content = f.read() # Remove "window.YTD." and semicolon
    tweets = json.loads(content)

# Define the keyword(s) to search for
keywords = ['thank', 'following me']

# Loop through the tweets and delete those that contain the keyword(s)
for tweet in tweets:
    text = tweet['tweet']['full_text'].lower()
    if all(keyword.lower() in text for keyword in keywords):
        try:
            api.destroy_status(tweet['tweet']['id_str'])
            print(f"Tweet deleted: {tweet['tweet']['id_str']}")
        except Exception as e:
            print(f'Error deleting tweet: {str(e)}')
