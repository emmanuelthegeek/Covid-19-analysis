import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
#load in the data with 'read.csv()'
filepath = 'covid.csv'
digits = pd.read_csv(filepath)
print(digits)
digits.set_index('Date', inplace = True)
digits.index = pd.to_datetime(digits.index)
print(digits.index)
plt.bar(digits.index, height=84000, width=0.8)
plt.xlabel('Date')
plt.ylabel('No of confirmed cases')
plt.show()
