import sqlite3 as sql
import queries as qrs
import pandas as pd

# assignment 1

def connect_db(db='../rpg_db.sqlite3'):
    return sql.connect(db)

def exec(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    res = curs.fetchall()
    return res


# assignment 2

df = pd.DataFrame(pd.read_csv('../buddymove_holidayiq.csv'))

print(df.shape)
print(df.isnull().count())

conn = sql.connect('../buddymove_holidayiq.sqlite3')
# df.to_sql('review', conn)

# how many rows
row_count = 'SELECT COUNT(*) FROM review'
# how many users who reviewed at least 100 'Nature' and at least 100 in 'Shopping'
nature_and_shopping = 'SELECT COUNT(*) FROM review WHERE Nature >= 100 AND Shopping >= 100'

print(exec(conn, row_count))
print(exec(conn, nature_and_shopping))
