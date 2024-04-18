import pandas as pd
import os
processed = "./processed"
file = "results.csv"
dataframe = pd.read_csv("./data/" + file, header=0)
dataframe = dataframe[['resultId', 'number', 'grid', 'position', 'positionText', 'positionOrder', 'points', 'laps', 'raceId', 'driverId', 'constructorId', 'statusId']]
#resultId;number;grid;position;;;points;laps;fastestLap;rank;fastestLapTime;fastestLapSpeed;;;;

if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/15_" + file, index=False, sep=";")

