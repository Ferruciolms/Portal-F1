import pandas as pd
import os
processed = "./processed"
file = "races.csv"

dataframe = pd.read_csv("./data/" + file, header=0)
dataframe = dataframe[['fp1_date', 'fp1_time', 'fp2_date', 'fp2_time', 'fp3_date', 'fp3_time', 'raceId']]

dataframe1 = dataframe[['fp1_date', 'fp1_time', 'raceId']]
type_1 = 1
dataframe1.loc[:, 'type'] = type_1
dataframe1 = dataframe1[['type', 'fp1_date', 'fp1_time', 'raceId']]
dataframe1 = dataframe1.rename(columns={"fp1_date": "fp_date", "fp1_time": "fp_time"})

dataframe2 = dataframe[['fp2_date', 'fp2_time', 'raceId']]
type_2 = 2
dataframe2.loc[:, 'type'] = type_2
dataframe2 = dataframe2[['type', 'fp2_date', 'fp2_time', 'raceId']]
dataframe2 = dataframe2.rename(columns={"fp2_date": "fp_date", "fp2_time": "fp_time"})

dataframe3 = dataframe[['fp3_date', 'fp3_time', 'raceId']]
type_3 = 3
dataframe3.loc[:, 'type'] = type_3
dataframe3 = dataframe3[['type', 'fp3_date', 'fp3_time', 'raceId']]
dataframe3 = dataframe3.rename(columns={"fp3_date": "fp_date", "fp3_time": "fp_time"})

df = pd.concat([dataframe1, dataframe2, dataframe3], ignore_index=True)
mask = (df['fp_date'] == "\\N") | (df['fp_time'] == "\\N")
df = df.drop(df[mask].index)
df.reset_index(drop=True, inplace=True)
df.index = df.index + 1

print(df)


if not os.path.exists(processed):
    os.mkdir(processed)

df.to_csv(processed +"/22_" + "free_practice.csv", index=True, sep=";", index_label="ID")