import pandas as pd
import os
processed = "./processed"
file = "races.csv"

df = pd.read_csv("./data/" + file, header=0)
df = df[['quali_date','quali_time','raceId']]
mask = (df['quali_date'] == "\\N") | (df['quali_time'] == "\\N")
df = df.drop(df[mask].index)
df.reset_index(drop=True, inplace=True)
df.index = df.index + 1
print(df)

if not os.path.exists(processed):
    os.mkdir(processed)

df.to_csv(processed +"/" + "24_qualify_session.csv", index=True, sep=";", index_label="ID")