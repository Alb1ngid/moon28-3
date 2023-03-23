# база_данных
# sql - язык структурированных данных
# СУБД-системы управления баз данных
# реляционные
# CRUD CREATE REED UPDATE DELETE

import sqlite3
from sqlite3 import Error


def create_connektion(db_file):
    conn = False
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def reed(conn):
    try:
        sql='SELECT * FROM student'
        cursor = conn.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()

        for i in rows:
            print(i)
    except Error as e:
        print(e)




def create_student(conn, student):
    sql = '''INSERT INTO student (name,mark,hobby,b_date,is_married)
    VALUES (?,?,?,?,?)
    '''
    try:
        cursor=conn.cursor()
        cursor.execute(sql,student)
        conn.commit()
    except Error as e:
        print(e)


database = r'puge.db'

sql_create_table = '''
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR (104) NOT NULL,
mark FLOAT NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
b_date DATE NOT NULL ,
is_married BOOLEAN DEFAULT FALSE
);
'''

connection = create_connektion(database)
if connection is not None:
    # create_table(connection, sql_create_table)
    # create_student(connection,('Бека',10.2,'пишу','2003-06-06',False))
    reed(connection)
    print('все работает')
