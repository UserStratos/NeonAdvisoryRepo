import warnings;
warnings.simplefilter("ignore")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from TimeSeriesModel.load_data_AMD.constants import file_name, data


#Functions that are going to help calculations
def opencsv(file_name):
    data = pd.read_csv(file_name)


def replace_dollar_sign():
    df = pd.DataFrame(data)
    df['High'] = df['High'].str.replace('$', '')
    df['Low'] = df['Low'].str.replace('$', '')
    df['Open'] = df['Open'].str.replace('$', '')
    df['Close/Last'] = df['Close/Last'].str.replace('$', '')

def change_data_type():
    df = pd.DataFrame(data)
    df['Open'] = df["Open"].astype(float)
    df['Volume'] = df["Volume"].astype(float)
    df['High'] = df["High"].astype(float)
    df['Low'] = df["Low"].astype(float)
    df['Close/Last'] = df["Close/Last"].astype(float)
    df['Date'] = df['Date'].astype('datetime64[ns]')

    print(df)

def sort_data_by_column():
    df = pd.DataFrame(data)
    shor_data = df.sort_values(by= "Open", ascending = False)
    print(df)

def data_info():
    df = pd.DataFrame(data)
    print('Summary of the DataFrame')
    print(df.info())

    #print(data.head())
    #print(data.tail())
def data_shape():
    df = pd.DataFrame(data)
    print(df.shape)

def data_description():
    df = pd.DataFrame(data)
    print(df.describe())

def data_columns():
    df = pd.DataFrame(data)
    print(df.columns)

def data_dtypes():
    df = pd.DataFrame(data)
    print(df.dtypes)


#Missing values
def data_missing_values():
    df = pd.DataFrame(data)
    print(df.isna().sum())

#Missing values
def duplicated_data():
    df = pd.DataFrame(data)
    print(df.loc[data.duplicated()])

def data_head():
    df = pd.DataFrame(data)
    print(df.head())


def data_size():
    df = pd.DataFrame(data)
    print(df.size)

def data_empty():
    df = pd.DataFrame(data)
    print(data_empty)

def data_duplicated():
    df = pd.DataFrame(data)
    columns = df.head()
    for x in columns:
        print(df.loc[df.duplicated(subset=[x])])


def plot_graph():
    df = pd.DataFrame(data)
    x = df['Date']
    y = df['Open']

    # Plot lists 'x' and 'y'
    plt.plot(x, y)

    # Plot axes labels and show the plot
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.show()
