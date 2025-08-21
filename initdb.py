import psycopg2

database = psycopg2.connect(
    dbname = 'postgres',
    user = 'siddharth',
    password = 'siddharth',
    host = 'localhost',
    port = '5432'
)

database.autocommit = True
cur = database.cursor()

cur.execute('CREATE DATABASE maincrm;')

print('Database successfully created!')

cur.close()
database.close()