import warnings;
warnings.simplefilter("ignore")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from TimeSeriesModel.load_data_AMD.constants import file_name, data
from datetime import datetime
from TimeSeriesModel.load_data_AMD.constants import file_name
from datetime import datetime

#Functions that are going to help calculations
def opencsv(file_name):
    data = pd.read_csv(file_name)
    print(data.head())



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



