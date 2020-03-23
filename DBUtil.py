import sqlite3,os

def initDB():
    #Get the directory of the current file and connect to the database in it
    dirPath = os.path.abspath(os.path.dirname(__file__))
    dbPath = os.path.join(dirPath, 'Database/main.db')
    connection = sqlite3.connect(dbPath)

    cursor = connection.cursor()
    return cursor

def get_catalog(name):
    cursor = initDB()
    #get subcats
    cursor.execute('''
    SELECT c_code FROM catalog where name=?
    ''',(str(name)))
    catalog_code = cursor.fetchall()
    cursor.execute('''
    SELECT s_code FROM catalog_has_sub_catalog where c_code=?
    ''',(str(catalog_code)))
    codes = cursor.fetchall()
    cursor.execute('''
    SELECT s_code FROM catalog_has_sub_catalog where c_code=?
    ''',(str(catalog_code)))
    codes = cursor.fetchall()
