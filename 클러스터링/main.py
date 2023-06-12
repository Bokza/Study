import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as py
import plotly.graph_objs as go
from sklearn.cluster import KMeans
import warnings
import os
warnings.filterwarnings('ignore')

df = pd.read_csv('Mall_Customers.csv')
print(df)
# print(df.shape)
# print(df.describe())
# print(df.dtypes)
# print(df.isna().sum())

plt.style.use('fivethirtyeight')

'''
plt.figure(1, figsize=(15, 6))
n = 0
for x in ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']:
    n += 1
    plt.subplot(1, 3, n)
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    sns.distplot(df[x], bins=20)
    plt.title(f'Distplot of {x}')
plt.show()
'''
