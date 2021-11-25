import queries as q

# step 0. import sqlite
import sqlite3
# step 1. connect to database
# conn = sqlite3.connect('../rpg_db.sqlite3')
# # step 2. make your cursor
# curs = conn.cursor()
# # step 3. write our sql statement
# ''' select_all_query = 'SELECT * FROM charactercreator_character' '''
# # step 4. execute query on the cursor
# curs.execute(q.select_all_query)
# # step 5. pull the results
# results = curs.fetchall()
# # step 6. display head
# print(results[:5])

# conn = sqlite3.connect('../mock_db.sqlite3')
# curs = conn.cursor()
# create_statement = 'CREATE TABLE test_table (name char(20), age int);'
# curs.execute(create_statement)
# print(curs.fetchall())

# insert_statement = 'INSERT INTO test_table (name, age) VALUES ("Jimmy", 12);'
# curs.execute(insert_statement)
# insert_statement_2 = 'INSERT INTO test_table (name, age) VALUES ("Henry", 14);'
# curs.execute(insert_statement_2)

# **important for persistency**
# conn.commit()
# conn.close()

# select_statement = 'SELECT * FROM test_table;'
# curs.execute(select_statement)
# print(curs.fetchall())
# conn.close()

def connect_to_db(db_name='../rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    return results

if __name__ == '__main__':
    conn = connect_to_db()
    results = execute_query(conn, q.select_all_query)
    print(results[:5])
    print(len(results))
