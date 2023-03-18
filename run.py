import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
def load_data(filename):
    mylist=[]
    with open(filename) as numbers:
        numbers_data=csv.reader(numbers, delimiter=",")
        next(numbers_data)
        for row in numbers_data:
            mylist.append(row)
        return mylist

new_list = load_data('numbers.csv')
for row in new_list:
    print(row)

df = pd.read_csv("numbers.csv")

#df['Year'] = df['Time Date'].apply(lambda x: str(x)[-4:])
#df['Month'] = df['Time Date'].apply(lambda x: str(x)[-6:-4])
#df['Day'] = df['Time Date'].apply(lambda x: str(x)[:-6])
#df['ds'] = pd.DatetimeIndex(df['Year']+'-'+df['Month']+'-'+df['Day'])

#df = df.loc[(df['Product']==2667437) & (df['Store']=='QLD_CW_ST0203')]
#df.drop(['Time Date', 'Product', 'Store', 'Year', 'Month', 'Day'], axis=1, inplace=True)
#df.columns = ['y', 'ds']

df.head()
