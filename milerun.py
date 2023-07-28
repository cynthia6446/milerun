# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:43:04 2023

@author: be
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:38:47 2023

@author: 16617
fit a non-linear function

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import chdir
from scipy.optimize import minimize

chdir("C:/Users/16617/Documents/AVC/CIS111")


dataRun = pd.read_csv("mileRecords.csv")

t = np.array(dataRun['time'])
y = np.array(dataRun['year'])

y = y - y[0] # make numbers smaller, less roundoff error


K = 3.6
r = -0.25
 
param = (K,r)

def f3min(param):
    K = param[0]
    r = param[1]
    
    e=t-r*t*(1-t/K)*y
    return(np.dot(e,e.T))

err = f3min(param)
print(err)

x0 = param
opt = minimize(f3min, x0)
print(opt.x)
    
    
    