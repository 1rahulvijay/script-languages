import json
import sqlite3

import requests


def connect():
    global cursor, db, dataset
    try:
        url = "http://api.worldbank.org/v2/countries?format=json&per_page=100"
        content = requests.get(url)
        dataset = content.json()[1]

        print(len(dataset))

    except Exception as E:
        print('Error')
    else:
        print("DATA FETCHED SUCCESSFULLY")

    try:
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS COUNTRIES (id varchar(3), data json)")

    except Exception as E:
        print('ERROR :', E)
    else:
        print('TABLES CREATED')

    try:
        for country in dataset:
            cursor.execute('INSERT INTO COUNTRIES values (?, ?)',
                           [country['id'], json.dumps(country)])
            db.commit()
            print("DATA INSERTED")
        db.close()

    except Exception as E:
        print('ERROR :', E)


def view():
    try:
        db = sqlite3.connect('database.db')
        cursor = db.cursor()

        cursor.execute('''SELECT * FROM COUNTRIES''')

        rows = cursor.fetchall()
        db.close()
        return rows

    except Exception as E:
        print('ERROR :', E)


def delete_database():
    try:
        db = sqlite3.connect('database.db')
        cursor = db.cursor()

        cursor.execute('''DELETE FROM COUNTRIES''')

        db.commit()
        db.close()

    except Exception as E:
        print('ERROR :', E)




connect()
view()