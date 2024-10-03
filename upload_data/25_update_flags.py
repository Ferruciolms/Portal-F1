import pandas as pd
import os
import psycopg2
processed = "./processed"
file = "update_flags.csv"

df = pd.read_csv("./data/" + file, header=0, delimiter=";")

db = psycopg2.connect(user='postgres',
                      password='123',
                      database='portal_f1_new',
                      host='localhost',
                      port='5432',
                      options="-c search_path=" + 'public')

db.set_session(autocommit='True')
cursor = db.cursor()
for i, row in df.iterrows():
    cursor.execute("""
                UPDATE public.analytics_circuit
                SET country_flag=%(country_flag)s
                WHERE id = %(id)s""",
                   ({
                       'id': row['id'],
                       'country_flag': row['country_flag']
                      }))

cursor.close()