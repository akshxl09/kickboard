from flask import g
from pymysql import connect
import pymysql.cursors

def get_db(): #이거 개중요
    if 'db' not in g:     # 플라스크의 전역변수 g 속에 db 가 없으면
        g.db = connect(host="localhost", user="kickboard", password="0000", db="kickboard", charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
        # 내꺼 db에 접속.

def close_db(): #db 연결 종료
    db=g.pop('db',None) #db라는 거를 팝.
    if db is not None: #팝 한게 비어있지 않으면
        if db.open: #db가 열려있으면
            db.close() #종료해라

def init_db():
    #DB연결.
    db = connect(host="localhost", user="kickboard", password="0000", charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)

    with db.cursor() as cursor: #DB가 없으면 만들어라.
        sql = "CREATE DATABASE IF NOT EXISTS kickboard"
        cursor.execute(sql)
    db.commit()

    db.select_db('kickboard')

    #DB테이블생성

    with db.cursor() as cursor:
        sql = open("app/schema/user.sql").read()
        cursor.execute(sql)
        sql = open("app/schema/user_info.sql").read()
        cursor.execute(sql)
        sql = open("app/schema/kickboard.sql").read()
        cursor.execute(sql)
        sql = open("app/schema/kick_info.sql").read()
        cursor.execute(sql)
        sql = open("app/schema/kick_log.sql").read()
        cursor.execute(sql)
        sql = open("app/schema/broken_log.sql").read()
        cursor.execute(sql)
        sql = open("app/schema/feedback.sql").read()
        cursor.execute(sql)
    db.commit()
    db.close()
