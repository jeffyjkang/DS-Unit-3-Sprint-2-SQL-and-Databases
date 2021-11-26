from dotenv import load_dotenv
from pathlib import Path
import os
import pymongo
import sqlite3

dotenv_path = Path('../../.env')
load_dotenv(dotenv_path=dotenv_path)

MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_DB = os.getenv('MONGO_DB')
client = pymongo.MongoClient("mongodb+srv://jeff:{}@cluster0.8nwfm.mongodb.net/{}?retryWrites=true&w=majority".format(MONGO_PASSWORD, MONGO_DB))
db = client[f'{MONGO_DB}']
print(db)

conn = sqlite3.connect('../../module1-introduction-to-sql/rpg_db.sqlite3')
curs = conn.cursor()

def execute_query(curs, query):
    return curs.execute(query).fetchall()

def character_doc_creation(db, character_table):
    for character in character_table:
        # (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        character_doc = {
            'character_id': character[0],
            'name': character[1],
            'level': character[2],
            'exp': character[3],
            'hp': character[4],
            'strength': character[5],
            'intelligence': character[6],
            'dexterity': character[7],
            'wisdom': character[8]
        }

if __name__ == '__main__':
    character_table = execute_query(curs, 'SELECT * FROM charactercreator_character')
    character_doc_creation(db, character_table)

