import pandas as pd
from math import ceil
from pathlib import Path

# df = pd.read_csv('data\student-dataset.csv')
# # print(df.info())
# print(df.iloc[:5,[0,1,8,-1]])

df2 = pd.read_csv('data\sorted_by_age.csv')
print(df2.iloc[[0,10,500],[0,1,8]])

