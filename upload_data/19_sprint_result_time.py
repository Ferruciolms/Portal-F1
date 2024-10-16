import pandas as pd
import os
processed = "./processed"
file = "sprint_results.csv"
dataframe = pd.read_csv("./data/" + file, header=0)
dataframe = dataframe[['milliseconds','resultId']]
dataframe = dataframe.drop(dataframe[dataframe['milliseconds'] == "\\N"].index)


if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/" + "19_sprint_result_time.csv", index=True, sep=";",index_label="id")