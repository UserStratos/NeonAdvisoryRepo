from ProjectStructure.pythonpackage1 import constants as c1
from ProjectStructure.pythonpackage2 import constants as c2
from ProjectStructure.pythonpackage1 import functions as h1
from ProjectStructure.pythonpackage2 import functions as h2
import pandas as pd
import numpy as np
import openpyxl

from openpyxl import load_workbook

book=load_workbook('numbers.xlsx')
sheet=book.active


rows=sheet.rows

headers=next(rows)

headers=[cell.value for cell in next(rows)]
print(headers)



for row in rows:
    data={}
    for title, cell in zip(headers, row):
        data[title] = cell.value
    print(data)



# Triggering the entire project
# Do this by python run.py


# enter a fictitious function for example
