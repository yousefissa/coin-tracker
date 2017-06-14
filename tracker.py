import requests
from bs4 import BeautifulSoup
import tweepy

# url to scrape from. don't abuse my key or ill make you enter your own :/
wci_url = 'https://www.worldcoinindex.com/apiservice/json?key=qSt7Iu0d312Ro5yqmB3m5NuZ1'

# get the web content
soup = BeautifulSoup(requests.get(wci_url).text, "html.parser")

print(soup)