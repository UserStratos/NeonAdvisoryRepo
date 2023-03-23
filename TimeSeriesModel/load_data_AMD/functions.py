import warnings
warnings.simplefilter("ignore")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pmdarima
from TimeSeriesModel.load_data_AMD.constants import file_name, data, df
from pmdarima.arima import auto_arima
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf



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


def plot_histogramgraph():
    x = df['Volume']
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram Volume')
    plt.hist([x], color=['g', ], alpha=0.8, bins=50)
    plt.grid(True)
    plt.show()


def plot_scatter_plot():
    plt.scatter(df['Volume'], df['Close/Last'])
    plt.xlabel('Volume')
    plt.ylabel('Close/Last')
    plt.title('Scatter plot Volume, Last\Close price')
    plt.grid(True)
    plt.show()

def plot_multi_graphs():

    # Get the angles from 0 to 2 pie (360 degree) in narray object
    x = df['Close/Last']
    y = df["Volume"]
    z = df["Open"]
    d = df['Low']
    k = df["Date"]

    # Initialise the subplot function using number of rows and columns
    figure, axis = plt.subplots(2, 2)

    # For Close\Last price
    axis[0, 0].plot(k, x, color='r')
    axis[0, 0].set_title("Close\Last Graph", color='r')


    # For Volume
    axis[0, 1].plot(k, y, color='c')
    axis[0, 1].set_title("Volume Graph", color='c')


    # For Open price
    axis[1, 0].plot(k, z, color='y')
    axis[1, 0].set_title("Open price Graph", color='y')

    # For Low price
    axis[1, 1].plot(k, d, color='b')
    axis[1, 1].set_title("Low price Graph", color='b')

    plt.tight_layout()
    # Combine all the operations and display
    plt.show()
def ACF_PACF():
    variable = df['Volume']
    # acf = acf(data, nlags=40)
    # pacf = pacf(data,nlags=40,method='ols')

    # plt.stem(acf)
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    plot_acf(variable, lags=40, title="ACF on levels", ax=ax[0])
    # plt.show()
    plot_pacf(variable, lags=40, title="PACF on levels", ax=ax[1])
    plt.show()

    first_difference = variable.diff(periods=1).values[1:]
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    plot_acf(first_difference, lags=40, title="ACF on the first differences", ax=ax[0])
    # plt.show()
    plot_pacf(first_difference, lags=40, title="PACF on the first differences", ax=ax[1])
    plt.show()

def Dickey_Fuller():
    adft = adfuller(df['Volume'], autolag='AIC')
    output_df = pd.DataFrame(
        {"Values": [adft[0], adft[1], adft[2], adft[3], adft[4]['1%'], adft[4]['5%'], adft[4]['10%']],
         "Metric": ["Test Statistics", "p-value", "No. of lags used", "Number of observations used",
                    "critical value (1%)", "critical value (5%)", "critical value (10%)"]})
    print(output_df)

def Autocorrelation():
    autocorrelation_lag1 = df['Volume'].autocorr(lag=1)
    print("One Month Lag: ", autocorrelation_lag1)

    autocorrelation_lag3 = df['Volume'].autocorr(lag=3)
    print("Three Month Lag: ", autocorrelation_lag3)

    autocorrelation_lag6 = df['Volume'].autocorr(lag=6)
    print("Six Month Lag: ", autocorrelation_lag6)

    autocorrelation_lag9 = df['Volume'].autocorr(lag=9)
    print("Nine Month Lag: ", autocorrelation_lag9)

def correlation_matrix():
    corr_matrix = df.corr()
    print(corr_matrix)