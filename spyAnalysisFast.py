# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:07:27 2017

@author: dexter
"""
import csv 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime

"""titles = ['underlying_symbol','quote_datetime','root','expiration','strike','option_type','open','high','low','close','trade_volume','bid_size','bid','ask_size','ask','underlying_bid','underlying_ask','implied_underlying_price','active_underlying_price','implied_volatility	delta','gamma','theta','vega','rho']"""
#data[['underlying_symbol','root','option_type']].astype(basestring)

titles = ['underlying_symbol','quote_datetime','root','expiration','strike','option_type','open','high','low','close','trade_volume','bid_size','bid','ask_size','ask','underlying_bid','underlying_ask','implied_underlying_price','active_underlying_price','implied_volatility	delta','gamma','theta','vega','rho']
i  = 0 
csvD = {}
optionD = {} 
for i in range(0, len(titles)): 
    csvD[titles[i]] = i
j = 0 
with open('UnderlyingOptionsIntervalsCalcs_900sec_2016-06-01.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if (j ==0):  #skips the first header line 
            j = 1 
            continue 
        hashValue =  row[csvD['root']]  + '|' +row[csvD['expiration']]+ '|'+row[csvD['strike']]+'|'+row[csvD['option_type']]
        row[csvD['quote_datetime']] = datetime.strptime(row[csvD['quote_datetime']] ,'%m/%d/%Y %H:%S')
        row[csvD['expiration']] = datetime.strptime(row[csvD['expiration']] +' 16:00','%m/%d/%Y %H:%S') #assumes 4:00 est close
        for i in range(csvD['strike'],csvD['rho']+1):
            if i != csvD['option_type']:
                row[i] = float(row[i])
      
        if not hashValue in optionD:
            stack = []
            stack.append(row) 
            optionD[hashValue]=row 
        else:
            stack = optionD[hashValue] 
            stack.append(row)
            