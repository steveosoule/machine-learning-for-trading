import pandas as pd

df = pd.read_csv("data/AAPL.csv")

print('head()')
print(df.head())

print('tail()');
print(df.tail())

print('slice');
print(df[10:21]);