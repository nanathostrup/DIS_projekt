import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user='USERNAME',
        password='PASSWORD')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS candidates;')

cur.execute('CREATE TABLE candidates (LANDSDEL varchar (150) NOT NULL,'
                                 'STORKREDS varchar (150) NOT NULL,'
                                 'PARTI varchar(50) NOT NULL,'
                                 'STEMMESEDDELNAVN varchar (150));'
                                )

# Remove all data from the table
#cur.execute('DELETE FROM candidates')

#cur.execute("COPY candidates(LANDSDEL, STORKREDS, PARTI, STEMMESEDDELNAVN) FROM '/dataset/FV2022.csv' DELIMITER ',' CSV HEADER;")
cur.execute('INSERT INTO candidates(LANDSDEL, STORKREDS, PARTI, STEMMESEDDELNAVN)'
            'VALUES (%s, %s, %s, %s);',
            ('Hovedstaden',
            'Københavns Storkreds',
            'A',
            'Ida Auken')
)

cur.execute('INSERT INTO candidates (LANDSDEL, STORKREDS, PARTI, STEMMESEDDELNAVN)'
            'VALUES (%s, %s, %s, %s);',
            ('Hovedstaden',
            'Københavns Storkreds',
            'C',
            'Helle Bonnesen')
)

conn.commit()

cur.close()
conn.close()

# 
# ALTER USER user_name WITH SUPERUSER;
