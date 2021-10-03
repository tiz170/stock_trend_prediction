from __future__ import division
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from pandas_datareader import DataReader
from datetime import datetime

end = datetime.now()
start = datetime(end.year-1,end.month,end.day)

globals()['AAPLE'] = DataReader('AAPLE','iex',start,end)
globals()['GOOGLE'] = DataReader('GOOGLE','iex',start,end)
globals()['MICROSOFT'] = DataReader('MICROSOFT','iex',start,end)
globals()['AMAZON'] = DataReader('AMAZON','iex',start,end)


AAPLE['Daily Return'] = AAPLE['close'].pct_change()
AAPLE['Daily Return'].plot(figsize=(12,4), legend=True, linestyle='--', marker='o')
tech_list = ['AAPLE','GOOGLE','MICROSOFT','AMAZON']
close_price_diff = DataReader(tech_list, 'iex', start, end)['close']

# close price
close_price_diff.head(10)
returns = close_price_diff.pct_change()
returns.head()

# risk analysis
rets = returns.dropna()

rets.head()

# risk value
sns.distplot(AAPLE['daily return'].dropna(),bins=100,color='purple')

rets["AMAZON"].quantile(0.05)
rets["AAPLE"].quantile(0.05)
rets["MICROSOFT"].quantile(0.05)
rets["GOOGLE"].quantile(0.05)