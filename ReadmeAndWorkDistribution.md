How to run this file?

Unzip and save all these files under one folder.
Language: Python and MySQL
Version: Python(3.7) MySQL(8.0)

Packages required:
1. Pandas
2. pymysql
3. csv
4. sodapy
5. sqlalchemy
6. matplotlib
7. seaborn

Step 1: Run file DCP_Data.py
This file Reads the data from the API and cleans the data
1. We are using the API socrata which provides us with the filtered dataset.
2. You need to create a account and then create an API Token which you can do it from
here : https://dev.socrata.com/foundry/data.cityofnewyork.us/t29m-gskq
3. Once you are aunthenticated you will be able to run the rest of the code.

Step 2: Run file DCP_CSV_To_SQL.py
This file puts the cleaned data into the database
1. Install the required packages.
2. Make sure you have mysql server at the back. Use your username(usually root), password,
host(usually localhost), port(usually 3306) and the schema name.
3. Rest of the code works well if you create the engine properly.

Step 3: Run file Statistical_Analysis.py
Thus file performs statistical analysis on some attributes of data.
1. Install the requried packages.
2. Connect the engine and read the entire database.

Step 4: Run Analysis 1.py
Step 5: Run Analysis 2.py
step 6: Run analysis 3.py
step 7: Run analysis 4.py
Step 8: Regression.py
Step 9: Regression_2.py
Step 10:Classification.py


Distribution of work:

1. The work was divided equally. Being a 2 member team made us divide the things evenly accross every part of this data analysis phase. 
2. Starting from the data collection the data was fetched by Karan Makhija. 
3. API connection was done by Jeet Thakur. 
4. MYSQL database loading was done by Karan Makhija. 
6. Querying and inital python connection was done by Jeet. 
7. After that the last phase was done equally. we both worked on Data Visualization and also the data mining part. 
8. Finally We also together worked on different parts of results. 