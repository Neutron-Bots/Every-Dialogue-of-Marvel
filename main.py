import asyncio
import logging
import random
import sys
import time
import tweepy
from config import Config
from utils import getQoute, ping_server
import schedule
from os.path import exists

logging.getLogger().setLevel(logging.INFO)

# Credentials
api_key = Config.API_KEY
api_secret = Config.API_SECRET
bearer_token = fr"{Config.BEARER_TOKEN}"
access_token = Config.ACCESS_TOKEN
access_token_secret = Config.ACCESS_TOKEN_SECRET

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

        
async def post_qoute(tweepy: tweepy.Client):
    url = random.choice(Config.api_url)
    text = await getQoute(url)
    tweepy.create_tweet(text=text)
    tweepy.create_tweet
# 
def main():
    try:
        asyncio.run(post_qoute(client))
    except Exception as e:
        logging.error(e)
        main()

schedule.every(12).hours.do(main)

if __name__ ==  "__main__":

    if not exists("log.txt"):
        with open("log.txt", "w") as f:
            f.write(str())
            f.close()

    logging.info("Bot starting...")

    if Config.RUN_ONE_TIME:
        main()
        sys.exit()

    if Config.REPLIT:
        from utils import keep_alive
        asyncio.run(keep_alive())
        asyncio.create_task(ping_server())
        logging.info("Server Started")

    while True:
        schedule.run_pending()
        time.sleep(1)