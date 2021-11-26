CREATE_TABLE = '''
CREATE TABLE titanic (
    id SERIAL PRIMARY KEY,
    Survived INTEGER,
    Pclass INTEGER,
    Name VARCHAR (90) NOT NULL,
    Sex VARCHAR(30),
    Age INTEGER,
    "Siblings/Spouses Aboard" INTEGER,
    "Parents/Children Aboard" INTEGER,
    Fare DECIMAL(12, 2)
)
'''

GET_ALL_TITANIC = '''
SELECT *
FROM titanic
'''