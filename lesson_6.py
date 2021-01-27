"""Lesson 6: Joins and Merges"""

import pandas as pd
import numpy as np
# import datetime as dt

import io

DATA_PATH = "C:/Users/johnp/Development/tutorials/data/"
#%%Creating some dummy data

prc = pd.read_csv(
    io.StringIO('ticker,open,date,close\nAAPL,426.23,2018-01-04,435.23\nMSFT,42.3,2018-01-04,51.3\nAAPL,436.23,2018-01-05,\nMSFT,52.3,2018-01-05,\n'),
    parse_dates=['date']
)
prc2 = prc.assign(
    date=pd.to_datetime('2018-01-06'),
    close=prc.open + np.random.randn(len(prc.open))
).drop('open', axis=1)

volume = pd.DataFrame({
    'ticker': ['AAPL', 'MSFT', 'IBM', 'YHOO', 'GOOG'],
    'volume': [1954.73,  335.83,  362.79,  858.18,  629.79]
}).assign(date=pd.to_datetime('2018-01-05'))
#%%Left Join Example

merged = pd.merge(prc, volume, on='ticker', how='left')
#%%Understanding append and concat

#Append method stacks one dataframe on top of another


#Concat allows us to bind both vertically and horizontally
df1 = pd.DataFrame({'a': [0, 1],
                    'b': [0, 1]})
df2 = pd.DataFrame({'c': [0, 1],
                    'd': [0, 1]})
#Concat is a outer join along the concatenation axis
vertical_merge = pd.concat([df1, df2], axis=1)


