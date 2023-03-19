import warnings;
warnings.simplefilter("ignore")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#plt.style.use('ggplot')
#pd.set_option('max_columns', 200)
from TimeSeriesModel.load_data_AMD.constants import r
from TimeSeriesModel.load_data_AMD.constants import file_name, data
#from TimeSeriesModel.load_data_AMD.constants import data

#Functions that are going to help calculations

#Function 1: Loading data from csv and plot a graph

def opencsv(file_name):
    data = pd.read_csv(file_name)
    print(data)
    print("Data loaded successfully")

    #print(data.to_string())

def data_info():
    print('Summary of the DataFrame')
    print(data.info())

    #print(data.head())
    #print(data.tail())
def data_shape():
    print(data.shape)

def data_description():
    print(data.describe())

def data_columns():
    print(data.columns)

def data_dtypes():
    print(data.dtypes)


#Missing values
def data_missing_values():
    print(data.isna().sum())

#Missing values
def duplicated_data():
    print(data.loc[data.duplicated()])

def data_head():
    print(data.head())

def data_column():
      for x in data:
          data.head()
          print('all good')

def data_size():
    print(data.size)

def data_empty():
    print(data_empty)

def data_duplicated():
    columns = data.head()
    for x in columns:
        print(data.loc[data.duplicated(subset=[x])])



def remove_dollar():
    data['Close/Last'] = data['Close/Last'].str.replace('$','')
    data['High'] = data['High'].str.replace('$', '')
    data['Open'] = data['Open'].str.replace('$', '')
    data['Low'] = data['Low'].str.replace('$', '')
    #print(data.to_string(index=False))
    # using dictionary to convert specific columns
    convert_dict = {'Volume': float,
                    'High': float,
                    'Low': float,
                    'Open': float,
                    'Close/Last': float,
                    }

    #print(data[['High']].to_string(index=False))
    #print(data[['Open']].to_string(index=False))
    #print(data[['Low']].to_string(index=False))
    #print(data[['Close/Last']].to_string(index=False))
    #print(data[['Date']].to_string(index=False))


# x axis values
x = data['Low']
# corresponding y axis values

y = data['High']

# plotting the points
plt.scatter(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Scatter plot')

# function to show the plot
plt.show()