import requests
#import json
import time
import hashlib
#import random

import ast

api_key = '87d55079-86c4-456a-b4bb-4d2369ba02de'
secret_key = 'VYVXLVTDYGPNWHRGPF2EACIADDYO8S6PCEWK'

currentMillisTime = int(round(time.time() * 1000))
currentTime = int(time.time())

def get_function (url, dict={}):
    r = requests.get(url,verify=False, params=dict)
    #result = json.loads(r.text)
    #return result
    return r.json()

def post_function (url, sign, dict={}):
    print(dict)
    
    headers = {'sign': sign}
    r = requests.post(url, headers = headers, verify=False, json=dict)
    
    #result = json.loads(r.text)
    #return result
    return r

def sign_gen (parameters, secret_key):
    #print(parameters)
    parameters = str(parameters).replace("': '","=").replace("{","[").replace("}","]")
    #print(parameters)
    parameters = ast.literal_eval(parameters)
    #print(parameters)
    parameters.sort()
    #print(parameters)
    pre_sign = '&'.join(parameters) + '&secret_key=' + secret_key
    #print(pre_sign)
    sign = hashlib.md5(pre_sign.encode('utf-8')).hexdigest()
    #print(sign)
    return sign.upper()
    

#timestamp = str(int(time.time()))




parameters=['api_key=c821db84-6fbd-11e4-a9e3-c86000d26d7c', 'symbol=btc_cny','type=0','price=680','amount=1.0']

#print(sign_gen(parameters, secret_key))

#print(currentTime)
#print(currentMillisTime)

def returnTicker():
    params = locals()
    url = 'http://api.coinw.to/api/v1/public'
    
    params['command']='returnTicker'
    return get_function(url, params)

def returnCurrencies():
    params = locals()
    url = 'http://api.coinw.to/api/v1/public'
    
    params['command']='returnCurrencies'
    return get_function(url, params)

def returnOrderBook(size, symbol):
    params = locals()
    
    url = 'https://api.coinw.to/api/v1/public'
    
    params['command']='returnOrderBook'
    return get_function(url, params)
    
def returnTradeHistory(symbol, start, end):
    params = locals()
    
    url = 'https://api.coinw.to/api/v1/public'
    
    params['command']='returnTradeHistory'
    return get_function(url, params)   

def returnChartData(period, currencyPair, start, end):
    params = locals()
    
    url = 'https://api.coinw.to/api/v1/public'
    
    params['command']='returnChartData'
    print(params)
    return get_function(url, params) 

def return24hVolume():
    params = locals()
    url = 'https://api.coinw.to/api/v1/public'
    
    params['command']='return24hVolume'
    return get_function(url, params)

def returnOpenOrders(currencyPair):
    params = locals()
    
    url = 'http://api.coinw.to/api/v1/private?command=returnOpenOrders'
    
    preSign = params
    preSign['api_key'] = api_key
    #print(preSign)
    sign = sign_gen (preSign, secret_key)
    #print(sign)
    return post_function(url, sign, params)

#print(returnTicker())

#print(returnCurrencies())

#print(returnOrderBook(20, 'BTC_CNYT'))

#Not Work
#print(returnTradeHistory('BTC_CNYT', currentTime, currentTime+300))

#print(returnChartData(7200, 'BTC_CNYT', currentTime, currentTime+1000))
    
#Not Work
#print(returnChartData(7200, 'BTC_CNYT', None, None))

#print(return24hVolume())

#Not Work
print(returnOpenOrders('BTC_CNYT'))