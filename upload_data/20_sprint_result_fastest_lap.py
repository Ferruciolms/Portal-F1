import pandas as pd
import os
processed = "./processed"
file = "sprint_results.csv"
dataframe = pd.read_csv("./data/" + file, header=0)
dataframe =dataframe[["fastestLap","fastestLapTime","resultId"]]
dataframe = dataframe.drop(dataframe[dataframe["fastestLap"] == "\\N"].index)


print(dataframe)

if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/" + "20_sprint_result_fastest_lap.csv", index=True, sep=";", index_label="id")