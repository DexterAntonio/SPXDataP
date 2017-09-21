# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:07:27 2017

@author: dexter
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

s = pd.Series([1,3,5,np.nan,6,8])
dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
df2 = pd.DataFrame({ 'A' : 1.,'B' : pd.Timestamp('20130102'),'C' : pd.Series(1,index=list(range(4)),dtype='float32'),'D' : np.array([3] * 4,dtype='int32'),'E' : pd.Categorical(["test","train","test","train"]),'F' : 'foo' })

"""titles = ['underlying_symbol','quote_datetime','root','expiration','strike','option_type','open','high','low','close','trade_volume','bid_size','bid','ask_size','ask','underlying_bid','underlying_ask','implied_underlying_price','active_underlying_price','implied_volatility	delta','gamma','theta','vega','rho']"""
practiceData = pd.read_csv('UnderlyingOptionsIntervalsCalcs_900sec_2016-06-01.csv',sep=',')
movies = practiceData 
movies['hash'] = movies['root'] + '|' +movies['expiration']+'|'+movies['strike'].astype(str)+'|'+movies['option_type']


movies['strike'].astype(float)

"""print movies.dtypes"""

movies[['underlying_symbol','root','option_type']].astype(basestring)
movies['quote_datetime']= pd.to_datetime(movies['quote_datetime'])
movies['expiration'] = pd.to_datetime(movies['expiration'],format='%m/%d/%Y')

plt.plot(movies['quote_datetime'][(movies['hash']==movies['hash'].get(2))],movies['active_underlying_price'][(movies['hash']==movies['hash'].get(2))])
print movies.dtypes
