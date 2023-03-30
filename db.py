import os
import sqlite3

from flask_sqlalchemy import SQLAlchemy


COREPI_DATABASE_PATH = os.path.join(os.path.dirname(__file__), '../respire.db')


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_thresholds():
    try:
        conn = sqlite3.connect(COREPI_DATABASE_PATH)
    except:
        return None
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute('SELECT voc,'
                'co2,'
                'pm1,'
                'pm2,'
                'pm10,'
                'temperature,'
                'humidity FROM air_thresholds WHERE id=1;')
    thresholds = cur.fetchone()
    return thresholds


def get_current_air_data():
    try:
        conn = sqlite3.connect(COREPI_DATABASE_PATH)
    except:
        return None
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute('SELECT voc_amount as voc,'
                'co2_amount as co2,'
                'pm1_amount as pm1,'
                'pm2_amount as pm2,'
                'pm10_amount as pm10,'
                'temperature,'
                'humidity FROM air_data WHERE id=1;')
    data = cur.fetchone()
    return data


user_db = SQLAlchemy()
