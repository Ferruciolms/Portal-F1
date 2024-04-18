import pandas as pd
import os
processed = "./processed"
file = "constructor_standings.csv"
dataframe = pd.read_csv("./data/" + file, header=0)
dataframe = dataframe[['constructorStandingsId','points','position','positionText','wins','raceId','constructorId']]
# constructorStandingsId;raceId;constructorId;points;position;positionText;wins

dataframe = dataframe.replace("\\N", 0)
dataframe = dataframe.fillna(0)
if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/5_" + file, index=False, sep=";")
