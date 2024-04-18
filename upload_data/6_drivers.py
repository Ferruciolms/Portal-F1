import pandas as pd
import os
processed = "./processed"
file = "drivers.csv"
dataframe = pd.read_csv("./data/" + file, header=0)

dataframe = dataframe.replace("\\N", 0)
dataframe = dataframe.fillna(0)
if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/6_" + file, index=False, sep=";")
