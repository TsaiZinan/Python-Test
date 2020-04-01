# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:34:31 2020

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

def get_sign (api_key, secret_key, time):
    presign = "api_key" + api_key + "time" + time + secret_key
    sign = hashlib.md5(presign.encode('utf-8')).hexdigest()
    return sign

api_key = '6bfedf3b9581028b869530663295da5f'
secret_key = 'c16f9979441643b220f54c1d0eafc4df'
time = str(int(time.time()))
sign = get_sign (api_key, secret_key, time)






def get_allticker():
    url = 'https://openapi.goko.com/open/api/get_allticker'
    print(get_function(url))

def get_ticker(symbol):
    url = 'https://openapi.goko.com/open/api/get_ticker?symbol=' + symbol
    print(get_function(url))

def get_records(symbol, period):
    url = 'https://openapi.goko.com/open/api/get_records?symbol=' + symbol + '&period=' + period
    print(get_function(url))
    
def get_account(api_key, time, sign):
    url = 'https://openapi.goko.com/open/api/user/account?api_key=' + api_key + '&time=' + time + '&sign=' + sign
    print(get_function(url))


get_allticker()

get_ticker('btcusdt')

get_records('btcusdt','1440')

get_account(api_key, time, sign)




