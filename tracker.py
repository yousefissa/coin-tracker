from requests import get
from bs4 import BeautifulSoup
import tweepy
import json

# url to scrape from. don't abuse my key or ill make you enter your own :/

# get the json content of cryptos
btc = json.loads(requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR').text)


