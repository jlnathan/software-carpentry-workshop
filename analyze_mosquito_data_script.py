import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib
import statsmodels.api as sm
import matplotlib.pyplot as plt

filename = "A1_mosquito_data.csv"

# read the data
data = pd.read_csv(filename)
print data.head()

# celsius to fahrenheit
data["temperature"] = mosquito_lib.fahr_to_celsius(data["temperature"])
parameters = mosquito_lib.analyze(data)

# save parameters to file
parameters.to_csv("parameters.csv")

# c:/anaconda/scripts/ipython.exe analyze_mosquito_data_script.py

# mosquito.fahr_to_celsius(data["temperature"])
# mosquito.analyze(data)
