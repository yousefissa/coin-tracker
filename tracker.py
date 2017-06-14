from requests import get
from json import loads
from config import *
import tweepy
from time import sleep

# authorization from values inputted earlier, do not change.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

btc = ('BTC', 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
eth = ('ETH', 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')

# gets prices from api
def get_prices():
	return loads(get(btc[1]).text), loads(get(eth[1]).text)

# monitors for a 5% change or greater every minute
def monitor():
	old_btc_price, old_eth_price = get_prices()
	new_btc_price, new_eth_price = old_btc_price, old_eth_price
	# look for the price differnece
	while abs((old_btc_price['USD']/new_btc_price['USD']) - 1) < .05 and abs((old_eth_price['USD']/new_eth_price['USD']) -1) < .05:
		sleep(60)
		new_btc_price, new_eth_price = get_prices()
	# send tweet when it breaks out, then restart.
	api.update_status('Change in price! \n\nBTC: {} USD, {} EUR\nETH: {} USD, {} EUR'.format(new_btc_price['USD'], new_btc_price['EUR'], new_eth_price['USD'], new_eth_price['EUR']))
	print('Price change tweeted!')
	monitor()

# tweet price initially
def first_tweet():
	btc_price, eth_price = get_prices()
	api.update_status('Prices! \n\nBTC: {} USD, {} EUR\nETH: {} USD, {} EUR'.format(btc_price['USD'], btc_price['EUR'], eth_price['USD'], eth_price['EUR']))
	print('Initial price tweeted!')

# someone asked me to have the monitor tweet every minute. 
def tweet_every_minute():
	btc_price, eth_price = get_prices()
	api.update_status('Prices! \n\nBTC: {} USD, {} EUR\nETH: {} USD, {} EUR'.format(btc_price['USD'], btc_price['EUR'], eth_price['USD'], eth_price['EUR']))
	sleep(60)
	tweet_every_minute()


if __name__ == "__main__":
	print('Coin monitor started!')
	first_tweet()
	monitor()

# if you want the monitor to tweet every minute, comment the above if __name__ == "__main__"
# then uncomment this
# if __name__ == "__main__":
# 	print('Tweeting price every minute.')
# 	tweet_every_minute()


