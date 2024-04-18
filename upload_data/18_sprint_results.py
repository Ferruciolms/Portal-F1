import pandas as pd
import os
processed = "./processed"
file = "sprint_results.csv"
dataframe = pd.read_csv("./data/" + file, header=0)
dataframe =dataframe.drop(["time","fastestLap","fastestLapTime","milliseconds"], axis=1)



print(dataframe)

if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/18_" + file, index=False, sep=";")
