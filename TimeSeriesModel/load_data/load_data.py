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

print(data.info())
print(data.head())
print(data.tail())
print(data.shape)
print(data.describe())
print(data.columns)
print(data.dtypes)









