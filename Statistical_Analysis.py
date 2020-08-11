import pandas as pd

from sqlalchemy import create_engine
import sqlalchemy
user = 'yourUsername'
passw = 'yourPassword'
host =  'yourHostname'
port = 3306
database = 'nyctaxi'
mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)
df = pd.read_sql('SELECT * FROM taxi', con=mydb)


pd.set_option('float_format', '{:,.2f}'.format)
print(df['trip_distance'].describe())
print(df['tip_amount'].describe())
print(df['total_amount'].describe())


