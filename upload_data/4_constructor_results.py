import pandas as pd
import os
processed = "./processed"
file = "constructor_results.csv"
dataframe = pd.read_csv("./data/" + file, header=0)
dataframe = dataframe[['constructorResultsId','points','status','constructorId','raceId']]
dataframe = dataframe.replace("\\N", 0)
dataframe = dataframe.fillna(0)
if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/4_" + file, index=False, sep=";")
