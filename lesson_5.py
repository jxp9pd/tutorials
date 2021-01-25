"""Lesson 5: Time Series Analysis Pandas"""

import pandas as pd
import numpy as np
import datetime as dt

np.random.seed(252)

DATA_PATH = "C:/Users/johnp/Development/tutorials/data/"
#%%Read in titanic and SP 500 data

titanic_df = pd.read_csv(DATA_PATH + 'titanic_train.csv')
sp500 = pd.read_csv(DATA_PATH + 'sp500.csv')

#The colon thing is an annotation, indicating functions expects that type
def random_series(dti: pd.DatetimeIndex):
    '''Generates a time series of random values'''
    
    values = np.random.randn(len(dti))
    return pd.Series(values, index=dti)

def make_series_5():
    dts = pd.date_range('2000-01-01', '2000-01-05', freq='D')
    rv = pd.Series(np.random.randn(len(dts)), index=dts)
    rv[1:] = np.nan
    return rv

#%%Generating some time series data

#Specifies a range of date times using the business calendar (M-F only)
dts = pd.date_range('2000-01-01', '2001-12-31', freq='B')
#Generates n random vals between 0-1, with the dates as the index
ts = pd.Series(np.random.randn(len(dts)), index=dts)

#Selecting data out of the time series
ts['2000-03-20']
ts['2000-03-20':'2000-03-30']

#Select by month or year
ts['2000-03']
ts['2000']
#%%Applying lead or lag operations

ts2k = ts['2000-01'].copy()
#Lag or lead the data by one day.
ts2k.shift(1).iloc[[0, 1, 2, -2, -1]]
ts2k.shift(-1).iloc[[0, 1, 2, -2, -1]]


#tshift method. More clever version that takes the calendar into account.
ts2k.tshift(-1).iloc[[0, 1, 2, -2, -1]]
#%%Resampling a time series

#Daily frequency (already the default)
dts = pd.date_range('2000-01-01', '2000-03-31', freq='D')
ts = random_series(dts)
#The resample function is much like the groupby aggregator.
grp = ts.resample('M')
grp.agg(['mean', 'std'])
#%%Interpolating and filling missing data

ts = make_series_5()

#Forward or backfill data. Limit parameter used to set a ceiling on ffill
ts.ffill(limit=2)
ts.bfill()
#%%Generate some misaligned data

dts_m = pd.bdate_range('2000-01', periods=2, freq='MS')
t_bill = pd.Series([0.012, 0.023], index=dts_m)

dts_d = pd.bdate_range('2000-01-01', periods=8, freq='W')
sp_weekly = random_series(dts_d)

#How to realign, weekly data with monthly data. Forward fill is necessary, as
#they don't share any dates.
t_bill.reindex(sp_weekly.index, method='ffill')
#%%Applying rolling calculations

#First create a rolling object with period of 2
roll = sp_weekly.rolling(3)

#Get a rolling average
roll.median()
roll.mean()
 