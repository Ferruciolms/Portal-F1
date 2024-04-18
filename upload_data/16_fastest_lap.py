import pandas as pd
import os
processed = "./processed"
file = "results.csv"
dataframe = pd.read_csv("./data/" + file, header=0)
dataframe = dataframe[['fastestLap','rank', 'fastestLapTime', 'fastestLapSpeed', 'resultId']]
dataframe = dataframe.drop(dataframe[dataframe['fastestLap'] == "\\N"].index)
print

if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/" + '16_fastest_lap.csv', index=True, sep=";", index_label="id")