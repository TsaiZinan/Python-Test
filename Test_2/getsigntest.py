# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 07:34:50 2020

@author: czn82
"""

import requests
import json
import time
import hashlib





def get_function (url):
    r = requests.get(url)
    result = json.loads(r.text)
    return result

def get_sign (api_key, secret_key, timestamp):
    presign = "api_key" + api_key + "time" + timestamp + secret_key
    sign = hashlib.md5(presign.encode('utf-8')).hexdigest()
    return sign




def getnewsign (symbol):
    api_key = '6bfedf3b9581028b869530663295da5f'
    timestamp = str(int(time.time()))
    secret_key = 'c16f9979441643b220f54c1d0eafc4df'
    
    newsign = 'api_key' + api_key + 'symbol' + symbol + 'time' + timestamp + secret_key
    #print(newsign)
    newsign = hashlib.md5(newsign.encode('utf-8')).hexdigest()
    return newsign



api_key = '6bfedf3b9581028b869530663295da5f'
secret_key = 'c16f9979441643b220f54c1d0eafc4df'
timestamp = str(int(time.time()))
#sign = get_sign (api_key, secret_key, timestamp)



def all_order(symbol, api_key, timestamp):
    newsign = getnewsign(symbol)
    url = 'https://openapi.goko.vip/open/api/all_trade?symbol=' + symbol + '&api_key=' + api_key + '&time=' + timestamp + '&sign=' + newsign
    print(url)
    print(get_function(url))
    
#print(getnewsign('gsb'))  
    
all_order('gsbusdt', api_key, timestamp)