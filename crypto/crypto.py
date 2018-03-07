import requests
import json

url = "https://api.coinmarketcap.com/v1/ticker/?limit=300"
reponse = requests.get(url)
reponse_dicts = reponse.json()

usd_to_cnt = 6.3257

for reponse_dict in reponse_dicts:
	if reponse_dict['id'] == 'bitcoin':
		bitcoin_price_cnt = float(reponse_dict['price_usd']) * usd_to_cnt
		print("BTC " + reponse_dict['rank'] + " " + str(bitcoin_price_cnt))
	elif reponse_dict['id'] == 'bytom':
		bitcoin_price_cnt = float(reponse_dict['price_usd']) * usd_to_cnt
		print("bytom " + reponse_dict['rank'] + " " + str(bitcoin_price_cnt))
	elif reponse_dict['id'] == 'neo':
		bitcoin_price_cnt = float(reponse_dict['price_usd']) * usd_to_cnt
		print("neo " + reponse_dict['rank'] + " " + str(bitcoin_price_cnt))
	elif reponse_dict['id'] == 'red-pulse':
		bitcoin_price_cnt = float(reponse_dict['price_usd']) * usd_to_cnt
		print("red-pulse " + reponse_dict['rank'] + " " + str(bitcoin_price_cnt))
	elif reponse_dict['id'] == 'bottos':
		bitcoin_price_cnt = float(reponse_dict['price_usd']) * usd_to_cnt
		print("bottos " + reponse_dict['rank'] + " " + str(bitcoin_price_cnt))
	elif reponse_dict['id'] == 'qlink':
		bitcoin_price_cnt = float(reponse_dict['price_usd']) * usd_to_cnt
		print("qlink " + reponse_dict['rank'] + " " + str(bitcoin_price_cnt))
