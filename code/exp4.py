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
area = np.pi*20

plt.scatter(rets.mean(),rets.std(),s=area)

plt.xlim([-0.0025,0.0025])
plt.ylim([0.001,0.025])
plt.ylabel('Risk')
plt.xlabel('Expected returns')

for label, x, y in zip(rets.columns, 
    rets.mean(), 
    rets.std()):
    plt.annotate(
        label,
        xy = (x, y), xytext = (50, 50),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        arrowprops = dict(arrowstyle = 'fancy', connectionstyle = 'arc3,rad=-0.3'))
