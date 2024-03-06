# importing libraries
import sqlite3
import pandas as pd 
import os

# file path
csv_file = 'gesture-vault\\Test.csv'

# set sqlite database
conn = sqlite3.connect('your_database.db')

# diver code
# df = pd.read_csv(csv_file)
# df.to_sql('test_data', conn, index=False, if_exists='replace')
# output = 'Mohan krishnan'
# query = f"SELECT * FROM test_data where Name = '{output}'";
# result = pd.read_sql_query(query, conn)
# print(result)

def db_connector(csv_file, name):
    conn = sqlite3.connect('your_database.db')
    df = pd.read_csv(csv_file)
    df.to_sql('test_data', conn, index=False, if_exists='replace')
    query = f"SELECT * FROM test_data where Name = '{name}'";
    result = pd.read_sql_query(query, conn)
    print(result)

