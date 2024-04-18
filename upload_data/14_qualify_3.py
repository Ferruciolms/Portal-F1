import pandas as pd
import os
processed = "./processed"
file = "qualifying.csv"
dataframe = pd.read_csv("./data/" + file, header=0)

dataframe = dataframe.fillna("\\N")
dataframe = dataframe[['q3','qualifyId']]
dataframe = dataframe.drop(dataframe[dataframe['q3'] == "\\N"].index)
print(dataframe)


if not os.path.exists(processed):
    os.mkdir(processed)

dataframe.to_csv(processed +"/" + "14_Q3.csv", index=True, sep=";", index_label="id")