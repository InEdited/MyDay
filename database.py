import sqlite3,os

#Get the directory of the current file and connect to the database in it
dirPath = os.path.abspath(os.path.dirname(__file__))
dbPath = os.path.join(dirPath, 'Database/main.db')
connection = sqlite3.connect(dbPath)

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS user")
cursor.execute('''CREATE TABLE user(
    u_id INTEGER  PRIMARY KEY 
                ,
    name VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    phone_no VARCHAR NOT NULL,
    b_date VARCHAR NOT NULL,
    gender VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    job VARCHAR,
    address VARCHAR
)
''')


cursor.execute("DROP TABLE IF EXISTS service")
cursor.execute('''CREATE TABLE service(
    s_id integer  PRIMARY KEY NOT NULL ,
    name VARCHAR NOT NULL,
    location VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    website VARCHAR NOT NULL,
    working_hr VARCHAR NOT NULL,
    workin_days VARCHAR NOT NULL
)
''')

cursor.execute("DROP TABLE IF EXISTS admin")
cursor.execute('''CREATE TABLE admin(
    a_id integer  PRIMARY KEY NOT NULL ,
    name VARCHAR NOT NULL,
    password VARCHAR NOT NULL
)
''')


cursor.execute("DROP TABLE IF EXISTS catalog")
cursor.execute('''CREATE TABLE catalog(
    c_code integer  PRIMARY KEY NOT NULL ,
    name VARCHAR NOT NULL
)
''')

cursor.execute("DROP TABLE IF EXISTS user_review_service")
cursor.execute('''CREATE TABLE user_review_service(
    u_id integer  PRIMARY KEY NOT NULL ,
    s_id VARCHAR NOT NULL,
    feedback VARCHAR,
    rate INTEGER 
)
''')

cursor.execute("DROP TABLE IF EXISTS sub_catalog")
cursor.execute('''CREATE TABLE sub_catalog(
    s_code integer  PRIMARY KEY NOT NULL ,
    name VARCHAR NOT NULL
)
''')

cursor.execute("DROP TABLE IF EXISTS service_has_sub_catalog")
cursor.execute('''CREATE TABLE service_has_sub_catalog(
    s_id integer  PRIMARY KEY NOT NULL ,
    name VARCHAR NOT NULL
)
''')

cursor.execute("DROP TABLE IF EXISTS catalog_has_sub_catalog")
cursor.execute('''CREATE TABLE catalog_has_sub_catalog(
    c_code integer  PRIMARY KEY NOT NULL ,
    s_code VARCHAR NOT NULL
)
''')