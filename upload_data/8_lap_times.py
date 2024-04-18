import pandas as pd
import os
processed = "./processed"
file = "lap_times.csv"
dataframe = pd.read_csv("./data/" + file, header=0)
dataframe =dataframe.drop("time", axis=1)
dataframe = dataframe.replace("\\N", 0)
dataframe = dataframe.fillna(0)
dataframe = dataframe[['lap','position','milliseconds','raceId','driverId']]
# raceId;driverId;lap;position;milliseconds

if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/8_" + file, index=False, sep=";")
