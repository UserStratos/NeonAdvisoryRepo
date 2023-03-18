import pandas as pd
import numpy as np

#Functions that are going to help calculations
from ProjectStructure.pythonpackage1 import constants as c1
def is_prime(num):
    if num>1:
        for n in range(2, num):
            if num % n !=0:
                continue
            else:
                return False
    return True

def calculate_primes(start, finish):
    primes=[]
    for n in range (start, finish):
        if is_prime(n) and n not in c1.SKIP_RANGE:
            primes.append(n)
    return primes
