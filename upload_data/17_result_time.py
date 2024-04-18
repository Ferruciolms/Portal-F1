import pandas as pd
import os
processed = "./processed"
file = "results.csv"
dataframe = pd.read_csv("./data/" + file, header=0)
dataframe = dataframe[['milliseconds','resultId']]


if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/" + "17_result_time.csv", index=True, sep=";",index_label="id")