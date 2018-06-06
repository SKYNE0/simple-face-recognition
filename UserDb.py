#_*_encoding:utf-8_*_
"""
@Python -V: 3.X
@SoftWave:Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.6.5
"""

import time

import sqlite3

from sqlite3 import IntegrityError

def time_now():
    """
    :return: str
    """
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return time_now

def insert_name(name):
    """
    :param name: 需要写入数据库的名字
    :return:
    """
    db_name = 'user.db'

    CREATE_DB = """CREATE TABLE IF NOT EXISTS user (id INT(10) PRIMARY KEY, name CHAR(20) UNIQUE, date CHAR(50))"""

    SELECT_ID = """SELECT id FROM user ORDER BY id DESC"""

    INSERT_NAME = """INSERT INTO user (id, name, date) VALUES (%s, %s, %s)"""

    conn = sqlite3.connect(db_name)

    cursor = conn.cursor()

    cursor.execute(CREATE_DB)

    id = cursor.execute(SELECT_ID).fetchone()

    date = time_now()

    if not id:
        id = 1
        print("\n您的信息已经成功保存至数据库，请稍等！")
        cursor.execute(INSERT_NAME % (id, '\'' + name + '\'', '\'' + date + '\''))
        conn.commit()
        conn.close()
    else:
        try:
            print("\n您的信息已经成功保存至数据库，请稍等!")
            cursor.execute(INSERT_NAME % (id[0] + 1, '\'' + name + '\'', '\'' + date + '\''))
            conn.commit()
            conn.close()

        except IntegrityError:
            conn.rollback()
            conn.close()

def user_id(name):
    """
    :param name: 需要查询ID的名字
    :return: int
    """
    db_name = 'user.db'

    SELECT_ID = """SELECT id FROM user WHERE name = """ + '\'' + name + '\''

    conn = sqlite3.connect(db_name)

    cursor = conn.cursor()

    id = cursor.execute(SELECT_ID).fetchone()[0]

    return id

def get_all():
    """
    :return: tuple 返回数据库中所用的名字及对应的ID
    """
    db_name = 'user.db'

    SELECT = """SELECT id, name FROM user ORDER BY id DESC"""

    conn = sqlite3.connect(db_name)

    cursor = conn.cursor()

    names = cursor.execute(SELECT).fetchall()

    return names

