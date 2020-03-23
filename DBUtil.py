import sqlite3,os

def initDB():
    #Get the directory of the current file and connect to the database in it
    dirPath = os.path.abspath(os.path.dirname(__file__))
    dbPath = os.path.join(dirPath, 'Database/main.db')
    connection = sqlite3.connect(dbPath)

    cursor = connection.cursor()
    return cursor

def get_sub_catalogs(name):
    print("yallayaba")
    cursor = initDB()
    #get subcats
    cursor.execute('''
    SELECT c_code FROM catalog where name=?
    ''',(str(name),))
    catalog_code = cursor.fetchall()
    #print(catalog_code[0][0])
    cursor.execute('''
    SELECT s_code FROM catalog_has_sub_catalog where c_code=?
    ''',(str(catalog_code[0][0]),))
    codes = cursor.fetchall()
    service_data = []
    for code in codes:
        #print(code[0])
        cursor.execute('''
        SELECT name FROM sub_catalog where s_code=?
        ''',(str(code[0]),))
        service_data.append(cursor.fetchall())
    print(service_data)
    return service_data


def get_services(name):
    cursor = initDB()
    #get subcats
    cursor.execute('''
    SELECT s_code FROM sub_catalog where name=?
    ''',(str(name),))
    sub_catalog_code = cursor.fetchall()
    print(sub_catalog_code[0][0])
    cursor.execute('''
    SELECT name FROM 
    (
        (service AS s INNER JOIN service_has_sub_catalog AS sc
        ON s.s_id = sc.s_id)
    )
    where sc.s_code=?
    ''',(str(sub_catalog_code[0][0]),))
    return cursor.fetchall()
    