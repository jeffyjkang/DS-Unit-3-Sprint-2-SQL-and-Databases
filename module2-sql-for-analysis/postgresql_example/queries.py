# Queries for sqlite to PostGreSQL pipeline

# PostGreSQL
CREATE_TABLE = '''
CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR (30) NOT NULL,
    number INTEGER
);
'''

INSERT_DATE = '''
INSERT INTO test_table
(name, number)
VALUES ('A row name', 6), ('Another row', 72)
'''

SELECT_ALL = '''
SELECT *
FROM test_table
'''

CREATE_CHARACTER_TABLE = '''
    CREATE TABLE charactercreator_character (
        character_id SERIAL PRIMARY KEY,
        name VARCHAR (30),
        level INTEGER,
        exp INTEGER,
        hp INTEGER,
        strength INTEGER,
        intelligence INTEGER,
        dexterity INTEGER,
        wisdom INTEGER
    );
'''

# SQLite
ROW_COUNT = '''
SELECT COUNT(*)
FROM charactercreator_character;
'''

GET_CHARACTERS = '''
SELECT *
FROM charactercreator_character;
'''