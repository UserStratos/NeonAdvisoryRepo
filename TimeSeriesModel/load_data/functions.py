import pandas as pd
import numpy as np
from TimeSeriesModel.load_data.constants import r

#Functions that are going to help calculations

# Function to compute simple interest at fixed rate of 5%
def interest(p,n):
    print("Computing simple interest at rate of 5%")
    si=(p*r*n)/100
    return si

