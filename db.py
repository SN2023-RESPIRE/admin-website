import os
import sqlite3

from flask_sqlalchemy import SQLAlchemy


COREPI_DATABASE_PATH = os.path.join(os.path.dirname(__file__), '../respire.db')


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_max_and_step_for_type(type):
    max_value = 0
    step_value = 1
    if type == 'co2':
        max_value = 2550
        step_value = 10
    elif type == 'voc':
        max_value = 65535
    elif type.startswith('pm'):
        max_value = 511
    elif type == 'temperature':
        max_value = 51
        step_value = 0.2
    elif type == 'humidity':
        max_value = 100
        step_value = 0.5
    return max_value, step_value



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
    cur.close()
    conn.close()
    return thresholds


def get_single_threshold(type):
    if type not in ['voc', 'co2', 'pm1', 'pm2', 'pm10', 'temperature', 'humidity']:
        return None
    try:
        conn = sqlite3.connect(COREPI_DATABASE_PATH)
    except:
        return
    cur = conn.cursor()
    cur.execute(f'SELECT {type} FROM air_thresholds WHERE id=1;')
    value = cur.fetchone()[0]
    cur.close()
    conn.close()
    max_value, step_value = get_max_and_step_for_type(type)
    return value, max_value, step_value


def set_threshold(type, value):
    if type not in ['voc', 'co2', 'pm1', 'pm2', 'pm10', 'temperature', 'humidity']:
        return False
    max_value, _ = get_max_and_step_for_type(type)
    if value > max_value:
        return False
    try:
        conn = sqlite3.connect(COREPI_DATABASE_PATH)
    except:
        return False
    cur = conn.cursor()
    with conn:
        cur.execute(f'UPDATE air_thresholds SET {type}={value} WHERE id=1;')
        conn.commit()
    cur.close()
    conn.close()
    return True


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
    cur.close()
    conn.close()
    return data


user_db = SQLAlchemy()
