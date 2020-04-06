# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 06:14:14 2020

@author: czn82
"""

import api

import threading

import concurrent.futures




import time
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


with concurrent.futures.ThreadPoolExecutor() as executor:
    

threads= []
t1 = threading.Thread(target=test, args=('BUY',))  
t2 = threading.Thread(target=test, args=('SELL',))

t1.start() 
t2.start()

t1.join()
t2.join()


