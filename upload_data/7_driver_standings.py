import pandas as pd
import os
file = "driver_standings.csv"
processed = "./processed"
dataframe = pd.read_csv("./data/" + file, header=0)
dataframe = dataframe[['driverStandingsId','points','position','positionText','wins','raceId','driverId']]
# driverStandingsId;raceId;driverId;points;position;positionText;wins
if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/7_" + file, index=False, sep=";")
