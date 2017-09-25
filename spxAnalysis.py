# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:07:27 2017

@author: dexter
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

"""titles = ['underlying_symbol','quote_datetime','root','expiration','strike','option_type','open','high','low','close','trade_volume','bid_size','bid','ask_size','ask','underlying_bid','underlying_ask','implied_underlying_price','active_underlying_price','implied_volatility	delta','gamma','theta','vega','rho']"""
data = pd.read_csv('UnderlyingOptionsIntervalsCalcs_900sec_2016-06-01.csv',sep=',')
data['hash'] = data['root'] + '|' +data['expiration']+'|'+data['strike'].astype(str)+'|'+data['option_type']

#data[['underlying_symbol','root','option_type']].astype(basestring)
data['quote_datetime']= pd.to_datetime(data['quote_datetime'])
data['expiration'] = pd.to_datetime(data['expiration'],format='%m/%d/%Y')

plt.plot(data['quote_datetime'][(data['hash']==data['hash'].get(1))],data['active_underlying_price'][(data['hash']==data['hash'].get(1))])

optionD = {} 

for index, row in data.iterrows(): 
    if not row['hash'] in optionD:
        stack = []
        stack.append(row)
        optionD[row['hash']]=row 
    else:
        stack = optionD[row['hash']]
        stack.append(row)
