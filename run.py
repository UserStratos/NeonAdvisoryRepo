import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv


with open("./Book.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)

