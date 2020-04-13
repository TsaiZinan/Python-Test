# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:34:31 2020

@author: czn82
"""

import requests
import json
import time
import hashlib
import random




def get_function (url):
    r = requests.get(url)
    result = json.loads(r.text)
    return result

def get_sign (api_key, secret_key, timestamp):
    presign = "api_key" + api_key + "time" + timestamp + secret_key
    sign = hashlib.md5(presign.encode('utf-8')).hexdigest()
    return sign

api_key = '6bfedf3b9581028b869530663295da5f'
secret_key = 'c16f9979441643b220f54c1d0eafc4df'
timestamp = str(int(time.time()))
sign = get_sign (api_key, secret_key, timestamp)






def get_allticker():
    url = 'https://openapi.goko.com/open/api/get_allticker'
    print(get_function(url))

def get_ticker(symbol):
    url = 'https://openapi.goko.com/open/api/get_ticker?symbol=' + symbol
    print(get_function(url))

def get_records(symbol, period):
    url = 'https://openapi.goko.com/open/api/get_records?symbol=' + symbol + '&period=' + period
    print(get_function(url))
    
def all_order(symbol, api_key, timestamp, sign):
    url = 'https://openapi.goko.com/open/api/user/account?symbol=' + symbol + '&api_key=' + api_key + '&time=' + timestamp + '&sign=' + sign
    print(get_function(url))
    
def get_account(api_key, timestamp, sign):
    url = 'https://openapi.goko.com/open/api/user/account?api_key=' + api_key + '&time=' + timestamp + '&sign=' + sign
    print(get_function(url))

def get_market(api_key, timestamp, sign):
    url = 'https://openapi.goko.com/open/api/market?api_key=' + api_key + '&time=' + timestamp + '&sign=' + sign
    print(get_function(url))

def all_trade(symbol, api_key, timestamp, sign):
    url = 'https://openapi.goko.com/open/api/all_trade?symbol=' + symbol + '&api_key=' + api_key + '&time=' + timestamp + '&sign=' + sign
    print(url)
    print(get_function(url))

def mass_replace(api_key, timestamp, sign, symbol, action, data):
        
    if action == 'BUY':
        mass = '&mass_place='
    elif action == 'SELL':
        mass = '&mass_cancel='
        
    url = 'https://openapi.goko.com/open/api/mass_replace?api_key=' + api_key + '&time=' + timestamp + '&sign=' + sign + mass + data
    
    print(get_function(url))

def mass_test(api_key, timestamp, sign, symbol):
    url = 'https://openapi.goko.com/open/api/mass_replace?api_key=' + api_key + '&time=' + timestamp + '&sign=' + sign + '&symbol=GSB' + '&mass_place=[{side:"BUY",type:"1",volume:"1",price:"0.000002",fee_is_user_exchange_coin:"0"}]'
    print(url)
    print(get_function(url))

    
def test(option, sec):
    if option == 'BUY':
        mass = 'buy_success'
    elif option == 'SELL':
        mass = 'sell_success'
        
    timerad = random.randint(4,10)
    time.sleep(timerad)
    print(timerad)
    print(mass + str(sec))
    
#url = 'https://openapi.goko.com/open/api/user/account?symbol=gsb&api_key=6bfedf3b9581028b869530663295da5f&time=' + timestamp + '&sign=' + sign
#print(get_function(url))
    
#get_allticker()

#get_ticker('btcusdt')

#get_records('btcusdt','1440')

#get_account(api_key, time, sign)




