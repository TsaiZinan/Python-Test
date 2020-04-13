# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:32:38 2020

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

def post_function (url, p):
    headers = {"Content-Type":"application/json"}
    r=requests.post(url, data=p, headers=headers)
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


def mass_test(api_key, timestamp, sign, symbol):
    url = 'https://openapi.goko.com/open/api/mass_replace'
    
    p={}
    p["api_key"]=api_key
    p["time"]=timestamp
    p["sign"]=sign
    p["symbol"]=symbol
    data = [{'side':"BUY",'type':"1",'volume':"1",'price':"0.000002",'fee_is_user_exchange_coin':"0"}]
    p["mass_place"]=data
    
    print(p)
    print(post_function(url, p))
    
    
def create_order(side, type, volume, price, symbol, api_key, timestamp, sign):
    url = 'https://openapi.goko.com/open/api/create_order'
    p={}
    p["api_key"]=api_key
    p["price"]=price
    p["side"]=side
    p["symbol"]=symbol
    p["time"]=timestamp
    p["type"]=type
    p["volume"]=volume
    p["sign"]=sign
    print(p)
    print(post_function(url, p))
    

create_order("BUY", 1, 1, '0.000002', 'gsbusdt', api_key, timestamp, sign)

#mass_test(api_key, timestamp, sign, 'gsb')