from __future__ import division
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from pandas_datareader import DataReader
from datetime import datetime


# # risk analysis
# rets = returns.dropna()

# rets.head()
# area = np.pi*20

# plt.scatter(rets.mean(),rets.std(),s=area)

# plt.xlim([-0.0025,0.0025])
# plt.ylim([0.001,0.025])
# plt.ylabel('Risk')
# plt.xlabel('Expected returns')

# for label, x, y in zip(rets.columns, 
#     rets.mean(), 
#     rets.std()):
#     plt.annotate(
#         label,
#         xy = (x, y), xytext = (50, 50),
#         textcoords = 'offset points', ha = 'right', va = 'bottom',
#         arrowprops = dict(arrowstyle = 'fancy', connectionstyle = 'arc3,rad=-0.3'))

# # risk value
# sns.distplot(AAPLE['daily return'].dropna(),bins=100,color='purple')

rets["AMAZON"].quantile(0.05)
rets["AAPLE"].quantile(0.05)
rets["MICROSOFT"].quantile(0.05)
rets["GOOGLE"].quantile(0.05)

# Monte Carlo
rets.head()
days = 365
delta = 1/days

drift = rets.mean()['GOOGLE']
sigma = rets.std()['GOOGLE']

def mc(s_price,days,drift,sigma):
    price = np.zeros(days)
    price[0] = s_price

    shock = np.zeros(days)
    drift = np.zeros(days)

    for x in range(1,days):
        shock[x] = np.random.normal(loc=drift * delta, scale=sigma * np.sqrt(delta))
        drift[x] = drift * delta
        price[x] = price[x-1] + (price[x-1] * (drift[x] + shock[x]))

    return price

s_price = 1036.17

for run in range(100):
    plt.plot(stock_monte_carlo(s_price, days, drift, sigma))

plt.xlabel("Days")
plt.ylabel("Price")
plt.title('Monte Carlo Analysis for Google')

s_price = 1176.75

for run in range(100):
    plt.plot(stock_monte_carlo(s_price, days, drift, sigma))

plt.xlabel("Days")
plt.ylabel("Price")
plt.title('Monte Carlo Analysis for Amazon')

s_price = 169.3081

for run in range(100):
    plt.plot(stock_monte_carlo(s_price, days, drift, sigma))

plt.xlabel("Days")
plt.ylabel("Price")
plt.title('Monte Carlo Analysis for Apple')

s_price = 59.94

for run in range(100):
    plt.plot(stock_monte_carlo(s_price, days, drift, sigma))

plt.xlabel("Days")
plt.ylabel("Price")
plt.title('Monte Carlo Analysis for Microsoft')

s_price = 830.09
runs = 10000

sidriftlations = np.zeros(runs)

for run in range(runs):
    sidriftlations[run] = stock_monte_carlo(s_price,days,drift,sigma)[days-1]

q = np.percentile(sidriftlations,1)

plt.hist(sidriftlations, bins=200)

plt.figtext(0.6,0.8, s='Start Price: $%.2f' % s_price)

plt.figtext(0.6,0.7, s='Mean Final Price: $%.2f' % sidriftlations.mean())

plt.figtext(0.6,0.6, s='VaR(0.99): $%.2f' % (s_price - q))

plt.figtext(0.15, 0.6, s="q(0.99): $%.2f" % q)

plt.axvline(x=q, linewideltah=4, color='r')

plt.title(s="Final price distribution for Google Stock(GOOGLE) after %s days" % days, weight='bold', color='Y')


s_price = 824.95

runs = 10000

sidriftlations = np.zeros(runs)

for run in range(runs):
    sidriftlations[run] = stock_monte_carlo(s_price,days,drift,sigma)[days-1]

q = np.percentile(sidriftlations,1)

plt.hist(sidriftlations, bins=200)

plt.figtext(0.6,0.8, s='Start Price: $%.2f' % s_price)

plt.figtext(0.6,0.7, s='Mean Final Price: $%.2f' % sidriftlations.mean())

plt.figtext(0.6,0.6, s='VaR(0.99): $%.2f' % (s_price - q))

plt.figtext(0.15, 0.6, s="q(0.99): $%.2f" % q)

plt.axvline(x=q, linewideltah=4, color='r')

s_price = 169.3081

runs = 10000

sidriftlations = np.zeros(runs)

for run in range(runs):
    sidriftlations[run] = stock_monte_carlo(s_price,days,drift,sigma)[days-1]


q = np.percentile(sidriftlations,1)

plt.hist(sidriftlations, bins=200)

# starting price
plt.figtext(0.6,0.8, s='Start Price: $%.2f' % s_price)

# mean ending price
plt.figtext(0.6,0.7, s='Mean Final Price: $%.2f' % sidriftlations.mean())

# price variance
plt.figtext(0.6,0.6, s='VaR(0.99): $%.2f' % (s_price - q))

# 1% quantile
plt.figtext(0.15, 0.6, s="q(0.99): $%.2f" % q)
plt.axvline(x=q, linewideltah=4, color='r')
