# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 08:19:20 2020

@author: czn82
"""

import requests
import json
import time
import hashlib


api_key = '6bfedf3b9581028b869530663295da5f'
secret_key = 'c16f9979441643b220f54c1d0eafc4df'
timestamp = str(int(time.time()))

def get_function (url):
    r = requests.get(url)
    result = json.loads(r.text)
    return result

def post_function (url, p):
    headers = {"Content-Type":"application/json"}
    r=requests.post(url, data=p, headers=headers)
    result = json.loads(r.text)
    return result


def get_sign (key_value):
    order = sorted(key_value.items(), key=lambda d: d[0])
    translation_table = dict.fromkeys(map(ord, "(,[' ])"), None)
    keyvalue_str = str(order).translate(translation_table)
    presign = "api_key" + api_key + keyvalue_str + secret_key
    sign = hashlib.md5(presign.encode('utf-8')).hexdigest()
    return sign

def all_order(symbol, page=None):
    key_value = {"time" : timestamp}
    key_value["symbol"] = symbol
    
    if page:
        key_value["page"] = page
    else:
        page = ""
    
    #print(key_value)
    #new = sorted(key_value.items(), key=lambda d: d[0])
    #print(new)
    #translation_table = dict.fromkeys(map(ord, "(,[' ])"), None)
    #new = str(new).translate(translation_table)
    sign = get_sign(key_value)
    url = 'https://openapi.goko.vip/open/api/all_trade?symbol=' + symbol + '&api_key=' + api_key + '&time=' + timestamp + '&page=' + page + '&sign=' + sign
    print(url)
    print(get_function(url))
    
    #print(sign)
    
    #newsign = getnewsign(symbol)
    #url = 'https://openapi.goko.vip/open/api/all_trade?symbol=' + symbol + '&api_key=' + api_key + '&time=' + timestamp + '&sign=' + newsign
    
def create_order(side, type, volume, price, symbol):
    url = 'https://openapi.goko.vip/open/api/create_order'
    p={}
    
    p["price"]=price
    p["side"]=side
    p["symbol"]=symbol
    p["time"]=timestamp
    p["type"]=type
    p["volume"]=volume
    
    sign = get_sign(p)
    
    p["api_key"]=api_key
    p["sign"]=sign
    
    p = json.dumps(p)
    
    print(p)
    print(post_function(url, p))
    

create_order("BUY", 1, 1, '0.000002', 'gsbusdt')
    
#all_order('gsbusdt')







