import pandas as pd
import analyze_mosquito_data_lib as mosquito
import statsmodels.api as sm
import matplotlib.pyplot as plt

filename = "A1_mosquito_data.csv"

data = pd.csv_read(filename)
print data.head()

# c:/anaconda/scripts/ipython.exe analyze_mosquito_data_script.py

# mosquito.fahr_to_celsius(data["temperature"])
# mosquito.analyze(data)
