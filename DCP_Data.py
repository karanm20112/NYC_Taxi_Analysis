import pandas as pd
from sodapy import Socrata


# Example authenticated client (needed for non-public datasets):
client = Socrata("data.cityofnewyork.us",
                 "yourAPIToken",
                 username="yourEmailID",
                 password="yourPassword")

client.timeout = 600000
results_yellow = client.get("t29m-gskq", where="tpep_pickup_datetime between '2018-12-24T00:00:00' and '2019-01-01T00:00:00'"
                                       "and payment_type < 3 and fare_amount >= 2.5 "
                                               "and trip_distance>0"
                                                , limit=16000000)

results_green = client.get("w7fs-fd9i", where="lpep_pickup_datetime between '2018-12-24T00:00:00' and '2019-01-01T00:00:00'"
                                       "and payment_type < 3 and fare_amount >= 2.5"
                                              "and trip_distance > 0" , limit=16000000)
# # Convert to pandas DataFrame

results_df_yellow = pd.DataFrame.from_records(results_yellow)
results_df_yellow.rename(columns={"tpep_pickup_datetime":"pickup_datetime","tpep_dropoff_datetime":"dropoff_datetime"},inplace=True)
results_df_yellow['Type'] = results_df_yellow.apply(lambda x: "Yellow", axis=1)



results_df_green = pd.DataFrame.from_records(results_green)
results_df_green.rename(columns={"lpep_pickup_datetime":"pickup_datetime","lpep_dropoff_datetime":"dropoff_datetime"}, inplace=True)

results_df_green['Type'] = results_df_green.apply(lambda x: "Green", axis=1)

results_df = pd.concat([results_df_yellow, results_df_green],sort=True)
results_df_cleaned = results_df.drop(['extra','improvement_surcharge','mta_tax','store_and_fwd_flag','tolls_amount','trip_type', 'vendorid'], axis=1)

results_Yellow_cleaned = results_df_yellow.to_csv("results_Yellow_Cleaned.csv")
results_Green_cleaned = results_df_green.to_csv("results_Green_Cleaned.csv")
results_Merged_cleaned = results_df_cleaned.to_csv("results_cleaned_merged.csv")


