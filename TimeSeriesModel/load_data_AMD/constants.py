import warnings;
warnings.simplefilter("ignore")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import QuantLib as ql



# Load data from csv file in to a dataframe
file_name = 'Amd.csv'

# Name the dataframe
data = pd.read_csv(file_name)

# Calculae how many columns are in teh dataFrame
x = (len(data))

#Define teh dataframe
df = pd.DataFrame(data)
