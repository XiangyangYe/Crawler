import requests
import json

url = 'https://www.feixiaohao.com/'
r = requests.get(url)

response_dicts = r.json()