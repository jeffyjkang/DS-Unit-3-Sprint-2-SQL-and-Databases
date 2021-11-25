# Basic SQLite to PostGreSQL Data Pipeline
import psycopg2
import sqlite3
import os
from pathlib import Path
from dotenv import load_dotenv
from queries import *

dotenv_path = Path('../../.env')
load_dotenv(dotenv_path=dotenv_path)


# connect to PostGreSQL DB
DB_NAME = os.getenv('DB_NAME')
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')

pg_conn = psycopg2.connect(dbname=DB_NAME,user=USER_NAME, password=PASSWORD, host=HOST)
pg_curs = pg_conn.cursor()


# connect to SQLite DB
sl_conn = sqlite3.connect('./rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
# fetchall() to return

# PRAGMA table_info(charactercreator_character);

# functions
def execute_query(curs, query):
    result = curs.execute(query)
    return result

def populate_pg_character_table(pg_curs, characters_list):
    for character in characters_list:
        insert_statement = '''
            INSERT INTO charactercreator_character
                (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
                VALUES {}
        '''.format(character[1:])
        pg_curs.execute(insert_statement)
        pg_conn.commit()

if __name__ == '__main__':
    execute_query(pg_curs, CREATE_CHARACTER_TABLE)
    get_characters = execute_query(sl_curs, GET_CHARACTERS).fetchall()
    populate_pg_character_table(pg_curs, get_characters)