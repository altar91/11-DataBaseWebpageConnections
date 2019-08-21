import mysql.connector
from mysql.connector import errorcode
import MySQLdb
import pandas

def getDataFromMYSQL(conditions):
    try:
        cnx = mysql.connector.connect(user='user_name', password='password',
                                      host='server_name',
                                      database='database_name')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        params = {'host': 'server_name', 'database': 'database_name', 'user': 'user_name', 'password': 'password'}
        conn = mysql.connector.connect(**params)
        cursor = cnx.cursor(buffered=True)
        query = ("""SELECT * FROM Table_Name WHERE date_column_name IN (%s, %s)""")
        df = pandas.read_sql(query, params=conditions, con=conn)
    return df


if __name__ == '__main__':
    try:
        conditions=['01/01/2019', '02/01/2019']
        df = getDataFromMYSQL(conditions)
    finally:
        if conn is not None:
            conn.close()
