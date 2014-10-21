import sys
import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib

filename = sys.argv[1]

# read the data
data = pd.read_csv(filename)
print "Analyzing", filename

# celsius to fahrenheit
data["temperature"] = mosquito_lib.fahr_to_celsius(data["temperature"])

print "Running analyze"
parameters = mosquito_lib.analyze(data,filename.replace("csv","png"))

print "Saving parameters"
# save parameters to file
parameters.to_csv(filename.replace("data","parameters"))

# c:/anaconda/scripts/ipython.exe analyze_mosquito_data_script.py

# mosquito.fahr_to_celsius(data["temperature"])
# mosquito.analyze(data)
