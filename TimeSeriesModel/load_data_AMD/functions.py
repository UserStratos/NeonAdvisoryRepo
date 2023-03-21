import warnings;
warnings.simplefilter("ignore")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from TimeSeriesModel.load_data_AMD.constants import file_name, data, df



#Functions that are going to help calculations
def opencsv(file_name):
    data = pd.read_csv(file_name)


def replace_dollar_sign():
    df['High'] = df['High'].str.replace('$', '')
    df['Low'] = df['Low'].str.replace('$', '')
    df['Open'] = df['Open'].str.replace('$', '')
    df['Close/Last'] = df['Close/Last'].str.replace('$', '')

def change_data_type():
    df['Open'] = df["Open"].astype(float)
    df['Volume'] = df["Volume"].astype(float)
    df['High'] = df["High"].astype(float)
    df['Low'] = df["Low"].astype(float)
    df['Close/Last'] = df["Close/Last"].astype(float)
    df['Date'] = df['Date'].astype('datetime64[ns]')

    print(df)

def sort_data_by_column():
    shor_data = df.sort_values(by= "Open", ascending = False)
    print(df)

def data_info():
    print('Summary of the DataFrame')
    print(df.info())

def data_shape():
    print(df.shape)

def data_description():
    print(df.describe())

def data_columns():
    print(df.columns)

def data_dtypes():
    print(df.dtypes)


#Missing values
def data_missing_values():
    print(df.isna().sum())

#Missing values
def duplicated_data():
    print(df.loc[data.duplicated()])

def data_head():
    print(df.head())


def data_size():
    print(df.size)

def data_empty():
    print(data_empty)

def data_duplicated():
    columns = df.head()
    for x in columns:
        print(df.loc[df.duplicated(subset=[x])])


def plot_allgraphs_in_one():
    x = df['Date']
    l = df['Close/Last']
    h = df['High']
    o = df['Open']
    v = df['Volume']
    # Plot with differently-colored markers.
    plt.plot(df['Date'], l, 'b-', label='Close\Last')
    plt.plot(df['Date'], h, 'g-', label='High')
    plt.plot(df['Date'], o, 'g-', label='Open')
    #plt.plot(df['Date'], v, 'g-', label='Volume')

    # Create legend.
    plt.legend(loc='upper left')
    plt.xlabel('Date')
    plt.ylabel('Prices')
    plt.show()

def plot_Close_Last():
    x = df['Date']
    y = df['Close/Last']
    # Plot lists 'x' and 'y'
    plt.plot(x, y)
    #Plot axes labels and show the plot
    plt.xlabel('Date')
    plt.ylabel('Close/Last')
    plt.show()

def plot_Volume():
    x = df['Date']
    y = df['Volume']
    # Plot lists 'x' and 'y'
    plt.plot(x, y)
    # Plot axes labels and show the plot
    plt.xlabel('Date')
    plt.ylabel('Volume')

    plt.show()

def all_graphs_inone_subplots():
    df.plot(subplots=True)
    df.plot(subplots=True, layout=(4, 5))
    plt.tight_layout()
    plt.show()
def plot_histogramgraph():
    x = df['Volume']
    plt.hist([x], color=['g', ], alpha=0.8, bins=50)
    plt.show()




