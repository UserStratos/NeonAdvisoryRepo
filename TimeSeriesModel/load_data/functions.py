import warnings;
warnings.simplefilter("ignore")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#plt.style.use('ggplot')
#pd.set_option('max_columns', 200)
from TimeSeriesModel.load_data.constants import r
from TimeSeriesModel.load_data.constants import file_name, data
#from TimeSeriesModel.load_data.constants import data
#Functions that are going to help calculations

#Function 1: Loading data from csv and plot a graph

def opencsv(file_name):
    data = pd.read_csv(file_name)
    print(data)
    print("Data loaded successfully")

    #print(data.to_string())

def data_info():
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

    #year = data['Year'] = data['Release Date'].apply(lambda x: '20'+str(x)[-2:])
    #month = data['Month'] = data['Release Date'].apply(lambda x: str(x)[-6:-4])
    #day = data['Day'] = data['Release Date'].apply(lambda x: str(x)[:-7])

    #print(data.columns.tolist())

#Missing values
def data_missing_values():
    print(data.isna().sum())

#Missing values
def duplicated_data():
    print(data.loc[data.duplicated()])

def data_head():
    print(data.head())

#Check for duplicates on a subset of data
    #print(data.loc[data.duplicated(subset=['Artist'])])
    #print(data.loc[data.duplicated(subset=['Song'])])
    #print(data.loc[data.duplicated(subset=['Streams (Billions)'])])
    #print(data.loc[data.duplicated(subset=['Release Date'])])



#Print graph Streams (Billions) / Year

   #ax = data[['Streams (Billions)', 'Year']].plot(kind='bar', title = 'Streams (Billions)', figsize=(15, 10))
   #ax.set_xlabel("x-axis")
   #ax.set_ylabel('y-axis')
#x = data['Year']
#y = data['Streams (Billions)']

#plot the graph
#plt.plot(x, y)
#plt.show()