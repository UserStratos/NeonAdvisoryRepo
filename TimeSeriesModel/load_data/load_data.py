import warnings;
warnings.simplefilter("ignore")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import csv



#Load csv data file
def load_series(filename):
    mylist=[]
    with open(filename) as numbers:
        numbers_data = csv.reader(numbers, delimiter=",")
        next(numbers_data)
        for row in numbers_data:
            mylist.append(row)
        return mylist

new_list = load_series('numbers.csv')
for row in new_list:
    print(row)




