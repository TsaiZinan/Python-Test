# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 06:14:14 2020

@author: czn82
"""

import api
import time
import threading


api_key = '6bfedf3b9581028b869530663295da5f'
secret_key = 'c16f9979441643b220f54c1d0eafc4df'
timestamp = str(int(time.time()))
sign = api.get_sign (api_key, secret_key, timestamp)


import random

def test(option):
    if option == 'BUY':
        mass = 'buy_success'
    elif option == 'SELL':
        mass = 'sell_success'
        
    timerad = random.randint(4,10)
    time.sleep(timerad)
    print(timerad)
    print(mass)


#api.get_allticker()



#t1 = threading.Thread(target=api.test, args=('BUY',1,))  
#t2 = threading.Thread(target=api.test, args=('SELL',2,))

#t1.start() 
#t2.start()

#t1.join()
#t2.join()


#api.mass_replace(api_key, timestamp, sign, 'gsb', [{side:"BUY",type:"1",volume:"1",price:"0.001",fee_is_user_exchange_coin:"0"}])

api.get_account(api_key, timestamp, sign)

#api.all_order('gsb', api_key, timestamp, sign)

#api.mass_test(api_key, timestamp, sign, 'gsb')
    
symbol = 'gsb'
#api.all_trade('gsb', api_key, timestamp, sign)