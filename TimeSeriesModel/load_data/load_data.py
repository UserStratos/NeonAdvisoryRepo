import warnings;
warnings.simplefilter("ignore")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#plt.style.use('ggplot')
#pd.set_option('max_columns', 200)


#Load data from csv file in to a dataframe
data = pd.read_csv("numbers.csv")
#print(data.to_string())

#print(data.info())
#print(data.head())
#print(data.tail())
#print(data.shape)
#print(data.describe())
#print(data.columns)
#print(data.dtypes)

data['Year'] = data['Time Date'].apply(lambda x: str(x)[-4:])
data['Month'] = data['Time Date'].apply(lambda x: str(x)[-6:-4])
data['Day'] = data['Time Date'].apply(lambda x: str(x)[:-6])
data['ds'] = pd.DatetimeIndex(data['Year']+'-'+data['Month']+'-'+data['Day'])


new_data = data.loc[(data['Product']==2667437) & (data['Store']=='QLD_CW_ST0203')]
new_data.drop(['Time Date', 'Product', 'Store', 'Year', 'Month', 'Day'], axis=1, inplace=True)
new_data.columns = ['y', 'ds']

print(data)
print(new_data)
#Data cleaning / droping columns from teh data sample
#new_data = data.drop(['Time Date'], axis=1)
#print(new_data)
#print(new_data.shape)






