import mysql.connector
import csv
import pymysql
import pandas as pd

from sqlalchemy import create_engine
import sqlalchemy
user = 'yourUsername'
passw = 'yourPassword'
host =  'localhost'
port = 3306
database = 'yourSchema'

mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)

date_cols = ['pickup_datetime', 'dropoff_datetime']
df = pd.read_csv('results_cleaned_merged.csv', parse_dates=date_cols)

df.drop(df.columns[0], axis=1, inplace=True)
# print(df)
print(df.columns)
print(df.dtypes)
df.to_sql(name="taxi", con=mydb, if_exists='replace', index=False,
            dtype={'dolocationid': sqlalchemy.types.INTEGER(),
                   'dropoff_datetime':  sqlalchemy.types.DATETIME(),
                   'fare_amount ': sqlalchemy.types.FLOAT(precision=3),
                   'passenger_count': sqlalchemy.types.INTEGER(),
                   'payment_type ': sqlalchemy.types.INTEGER(),
                   'pickup_datetime': sqlalchemy.types.DATETIME(),
                   'pulocationid ':  sqlalchemy.types.INTEGER(),
                   'ratecodeid  ': sqlalchemy.types.INTEGER(),
                   'tip_amount': sqlalchemy.types.FLOAT(precision=3),
                   'total_amount ': sqlalchemy.types.FLOAT(precision=3),
                   'trip_distance': sqlalchemy.types.FLOAT(precision=3),
                   'Type': sqlalchemy.types.VARCHAR(255)})


