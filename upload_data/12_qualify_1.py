import pandas as pd
import os
processed = "./processed"
file = "qualifying.csv"
dataframe = pd.read_csv("./data/" + file, header=0)

dataframe = dataframe.fillna("\\N")
dataframe = dataframe[['q1','qualifyId']]
dataframe = dataframe.drop(dataframe[dataframe['q1'] == "\\N"].index)
print(dataframe)


if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/" + "12_Q1.csv", index=True, sep=";", index_label="id")