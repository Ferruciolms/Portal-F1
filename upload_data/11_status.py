import pandas as pd
import os

file = "status.csv"
processed = "./processed"
df = pd.read_csv("./data/" + file, header=0)

if not os.path.exists(processed):
    os.mkdir(processed)

df.to_csv(processed +"/11_" + file, index=False, sep=";")
