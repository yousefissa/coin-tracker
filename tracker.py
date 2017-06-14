from requests import get
import tweepy
from json import loads
import time

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
	while abs((old_btc_price/new_eth_price) - 1) < .05 and abs((old_eth_price/new_eth_price) -1) < .05:
		sleep(60)
		new_btc_price, new_eth_price = get_prices()
	# send tweet when it breaks out, then restart.
	tweet_api.update_status('Change in price! \n\nBTC: {} USD, {}\nETH: {},{}'.format(new_btc_price['USD'], new_btc_price['EUR'], new_eth_price['USD'], new_eth_price['EUR']))
	monitor()


if __name__ == "__main__":
	monitor()