import mysql.connector
import logging


def server_db_connect():
    try:
        db = mysql.connector.connect(
            host="omega.uta.edu",
            user="drr0328",
            # passwd="GJ6FP004@dr0328",
            passwd="Apple123",
            database='db_project1'
        )
        return db
    except Exception as e:
        print(e)
        return None


def db_connect():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="password",
            database='db-project-1'
        )
        return db
    except Exception as e:
        print(e)
        return None


def insert_query(query, data):
    try:
        db = db_connect()
        if db is None:
            print('Database is Not connected!')
            return False

        cur = db.cursor()
        cur.execute(query, data)
        db.commit()

        return cur.rowcount
    except Exception as e:
        logging.error('Error Message: %s', e)
        print(e)
        return False


def update_query(query, data):
    try:
        db = db_connect()
        if db is None:
            print('Database is Not connected!')
            return False

        cur = db.cursor()
        cur.execute(query, data)
        db.commit()

        return cur.rowcount
    except Exception as e:
        print(e)
        return False


def delete_query(query, data):
    try:
        db = db_connect()
        if db is None:
            print('Database is Not connected!')
            return False

        cur = db.cursor()
        cur.execute(query, data)
        db.commit()

        return cur.rowcount
    except Exception as e:
        print(e)
        return False


def read_query(query, data=None):
    try:
        db = db_connect()
        if db is None:
            print('Database is not connected!')
            return False

        cur = db.cursor()
        cur.execute(query, data)
        result = cur.fetchall()

        return result
    except Exception as e:
        print(e)
        return False
