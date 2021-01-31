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
  
# Creating the first Dataframe using dictionary 
df1 = df = pd.DataFrame({"a":[1, 2, 3, 4], 
                         "b":[5, 6, 7, 8]}) 
  
# Creating the Second Dataframe using dictionary 
# Nulls are populated when columns don't match up
df2 = pd.DataFrame({"a":[1, 2, 3], 
                    "b":[5, 6, 7]}) 

big_df = df1.append(df2, ignore_index=True)
big_df
#%%
#Concat allows us to bind both vertically and horizontally
df1 = pd.DataFrame({'a': [0, 1],
                    'b': [0, 1]})
df2 = pd.DataFrame({'c': [0, 1],
                    'd': [0, 1]})
#Concat is a outer join along the concatenation axis
vertical_merge = pd.concat([df1, df2], axis=1)

df1 = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"],
                    "B": ["B0", "B1", "B2", "B3"],
                    "C": ["C0", "C1", "C2", "C3"],
                    "D": ["D0", "D1", "D2", "D3"],
                    }, index=[0, 1, 2, 3],)

       
df2 = pd.DataFrame({"A": ["A4", "A5", "A6", "A7"],
                    "B": ["B4", "B5", "B6", "B7"],
                    "C": ["C4", "C5", "C6", "C7"],
                    "D": ["D4", "D5", "D6", "D7"],
                    }, index=[4, 5, 6, 7])


df3 = pd.DataFrame({"A": ["A8", "A9", "A10", "A11"],
                    "B": ["B8", "B9", "B10", "B11"],
                    "C": ["C8", "C9", "C10", "C11"],
                    "D": ["D8", "D9", "D10", "D11"],
                    }, index=[8, 9, 10, 11])

frames = [df1, df2, df3]
result = pd.concat(frames, ignore_index=True)
#You can retain hierarchical keys for the original dataframes
result_keys = pd.concat(frames, keys = ['A', 'B', 'C'])

#Concat also allows vertical concat. By default it will join along the indices
#Default is an outer join along the indices
df4 = pd.DataFrame({"B": ["B2", "B3", "B6", "B7"],
                    "D": ["D2", "D3", "D6", "D7"],
                    "F": ["F2", "F3", "F6", "F7"],
                    }, index=[2, 3, 6, 7])
result = pd.concat([df1, df4], axis=1)
#We can also filter to inner. It's equivalent to drop rows with any na.
result = pd.concat([df1, df4], axis=1, join="inner")
#Reindexing to df1's index drops any rows not in df1s index
result = pd.concat([df1, df4], axis=1).reindex(df1.index)
