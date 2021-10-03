from __future__ import division
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from pandas_datareader import DataReader
from datetime import datetime

tech_list = ['AAPLE','GOOGLE','MICROSOFT','AMAZON']

end = datetime.now()
start = datetime(end.year-1,end.month,end.day)

globals()['AAPLE'] = DataReader('AAPLE','iex',start,end)
globals()['GOOGLE'] = DataReader('GOOGLE','iex',start,end)
globals()['MICROSOFT'] = DataReader('MICROSOFT','iex',start,end)
globals()['AMAZON'] = DataReader('AMAZON','iex',start,end)

# get some basic stats
AAPLE.head()
AAPLE.describe()
AAPLE.info()
MA_day = [1,7,10,20,50]

for period in MA_day:
    column_name = 'MA for %s days' %(str(period))
    AAPLE[column_name] = AAPLE['close'].rolling(window=period,center=False).mean()

# for period in MA_day:
#     column_name = 'MA for %s days' %(str(period))
#     AAPLE[column_name] = AAPLE['close'].rolling(window=period).mean()

# EMA
MA_day = [1,7,10,20]

for period in MA_day:
    column_name = 'EMA for %s days' %(str(period))
    AAPLE[column_name] = AAPLE['close'].ewm(span=20,min_periods=period,adjust=False).mean()