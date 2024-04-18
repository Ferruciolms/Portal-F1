import pandas as pd
import os
processed = "./processed"
file = "qualifying.csv"
dataframe = pd.read_csv("./data/" + file, header=0)

dataframe = dataframe.fillna("\\N")
dataframe = dataframe[['qualifyId', 'number', 'position', 'raceId', 'driverId', 'constructorId']]
print(dataframe)


if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/10_" + file, index=False, sep=";")


