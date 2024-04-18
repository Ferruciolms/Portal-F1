import pandas as pd
import os
processed = "./processed"
file = "circuits.csv"
dataframe = pd.read_csv("./data/" + file, header=0)

dataframe = dataframe.replace("\\N", 0)
dataframe = dataframe.fillna(0)
if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/1_" + file, index=False, sep=";")
