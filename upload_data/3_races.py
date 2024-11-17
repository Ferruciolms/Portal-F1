import pandas as pd
import os
processed = "./processed"
file = "races.csv"
dataframe = pd.read_csv("./data/" + file, header=0)
dataframe = dataframe[['raceId','year','round','name','date','time','url','circuitId']]
dataframe["time"] = dataframe["time"].replace("\\N","00:00:00")
dataframe["time"] = dataframe["time"].fillna("00:00:00")
dataframe = dataframe.replace("\\N",0)

if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/3_" + file, index=False, sep=";")
