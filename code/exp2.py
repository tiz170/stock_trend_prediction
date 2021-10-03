from __future__ import division
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from pandas_datareader import DataReader
from datetime import datetime

# plot the daily return
AAPLE['Daily Return'] = AAPLE['close'].pct_change()
AAPLE['Daily Return'].plot(figsize=(12,4), legend=True, linestyle='--', marker='o')
close_price_diff = DataReader(tech_list, 'iex', start, end)['close']

# close price
close_price_diff.head(10)
returns = close_price_diff.pct_change()
returns.head()

# sns.jointplot('GOOGLE','AMAZON',returns, kind='hex',size=8, color='skyblue')
# sns.jointplot('GOOGLE','GOOGLE',returns,kind='scatter',color='orange')
sns.jointplot('GOOGLE','AMAZON',returns, kind='scatter',size=8, color='skyblue')