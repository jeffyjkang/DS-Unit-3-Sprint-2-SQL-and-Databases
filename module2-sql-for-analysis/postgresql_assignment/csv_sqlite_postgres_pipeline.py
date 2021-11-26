import pandas as pd
import sqlite3
from dotenv import load_dotenv
from pathlib import Path
import os
import psycopg2
from queries import *

''' Generate sqlite table'''
# df = pd.read_csv('../titanic.csv')
# print(df.isnull().sum())
# conn = sqlite3.connect('./titanic.sqlite3')
# df.to_sql('titanic', conn, if_exists='fail', index=False)

dotenv_path = Path('../../.env')
load_dotenv(dotenv_path=dotenv_path)

# connect to PostGreSQL DB
DB_NAME = os.getenv('DB_NAME')
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')

conn = psycopg2.connect(dbname=DB_NAME, user=USER_NAME, password=PASSWORD, host=HOST)
curs = conn.cursor()

lite_conn = sqlite3.connect('./titanic.sqlite3')
lite_curs = lite_conn.cursor()

def execute_query(curs, query):
    res = curs.execute(query)
    return res

def pop_pg_titanic_table(conn, curs, lst):
    for el in lst:
        insert_statement = '''
            INSERT INTO titanic
            (Survived, Pclass, Name, Sex, Age, "Siblings/Spouses Aboard", "Parents/Children Aboard", Fare)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''
        curs.execute(insert_statement, el)
        conn.commit()

''' python commands to run '''
# execute_query(curs, CREATE_TABLE)
# titanic_data = execute_query(lite_curs, GET_ALL_TITANIC).fetchall()
# pop_pg_titanic_table(conn, curs, titanic_data)
