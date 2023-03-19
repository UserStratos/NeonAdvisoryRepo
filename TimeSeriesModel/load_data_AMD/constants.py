import warnings;
warnings.simplefilter("ignore")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Constant for interest calculation - Indicative example
r = 500

# Load data from csv file in to a dataframe
file_name = 'AMD.csv'

# Name the dataframe
data = pd.read_csv(file_name)

# Calculae how many columns are in teh dataFrame
x = (len(data))



