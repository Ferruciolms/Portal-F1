import pandas as pd
import os

file = "pit_stops.csv"
processed = "./processed"
dataframe = pd.read_csv("./data/" + file, header=0)
dataframe =dataframe.drop("duration", axis=1)
dataframe = dataframe[['stop','lap','milliseconds','raceId','driverId']]
# raceId;driverId;stop;lap;time;milliseconds


if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/9_" + file, index=False, sep=";")

