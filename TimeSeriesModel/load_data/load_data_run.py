import warnings;
warnings.simplefilter("ignore")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from TimeSeriesModel.load_data.functions import interest
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

#print(data)
#print(new_data)

#Data cleaning / droping columns from teh data sample
#new_data = data.drop(['Time Date'], axis=1)
#print(new_data)
#print(new_data.shape)


#Missing values
#print(data.isna().sum())

#Missing values
#print(data.loc[data.duplicated()])

#Check for duplicates on a subset of data
#print(data.loc[data.duplicated(subset=['Product'])])
#checking an example duplicate
#print(data.query('Product== 2667437'))

#ax = data['Year'].value_counts()\
#    .head(10)\
#    .plot(kind='bar', title = 'Stratos example graph')
#ax.set_xlabel("x-axis")
#ax.set_ylabel('y-axis')
#x = data['Year']
#y =  data['Value']

#plot the graph
#plt.plot(x, y)
#plt.show()

# use a gray background
x = np.random.randn(100000)

from matplotlib import cycler
colors = cycler('color',
                ['#EE6666', '#3388BB', '#9988DD',
                 '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none',
       axisbelow=True, grid=True, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('xtick', direction='out', color='gray')
plt.rc('ytick', direction='out', color='gray')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)

plt.hist(x)
plt.show()
# Open a txt file

#f = open('/Users/stratos/Desktop/Neon-Advisory/Rental Contract Amsterdam Desk Company/example.txt')
#print(f.read(50))
#def open_txt_file():
 #f  = open('/Users/stratos/Desktop/Neon-Advisory/Rental Contract Amsterdam Desk Company/example.txt')
#print(f.read(50))
# Get input from the user
p = int(input("Enter the principal amount: "))
n = int(input("Enter the number of years: "))
# Calling a function of constants.py file with p and n as an  arguments
#print("Interest accrued for the principal",p, "for",n, "years at the rate of 5% is 1000000",interest(p,n))
print('answer is  ',interest(p,n))


