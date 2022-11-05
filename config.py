import os

from dotenv import load_dotenv

load_dotenv()

class Config(object):
    API_KEY = os.environ.get("API_KEY")
    API_SECRET = os.environ.get("API_SECRET")
    BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

    api_url = ['https://superhero-quotes.herokuapp.com/grab?banner=mcu&size=1', 'https://superhero-search.herokuapp.com/api/quotes/random/qty/1'] # dont change this

    REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", None)
    REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", None)
    REPLIT = f"https://{REPLIT_APP_NAME.lower()}.{REPLIT_USERNAME}.repl.co" if REPLIT_APP_NAME and REPLIT_USERNAME else False
    PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))

    template = "\"{dialogue}\"\n\nBy - #{author}\n\n@marvel #marvel"