import pymysql
import time
import random
import re

conn = pymysql.connect( 
host='127.0.0.1', user='root', password='wpdjvks1',
db='quiz', charset='utf8') # 데이터베이스 접속

def disconn():
    conn.close()

def sign_up():
    id = input("ID : ")
    pw = input("PW : ")
    cursor = conn.cursor()
    sql = '''
    INSERT INTO user (user_id, user_score, user_pw, playTime)
    values (%s, %s, %s, %s)
    '''
    cursor.execute(sql, (id, 0, pw, 0))
    conn.commit()
    cursor.close()
    disconn()

def login():
    try:
        user_id = input("ID : ")
        cursor = conn.cursor()
        sql = '''
        select * from user where user_id=%s
        '''
        cursor.execute(sql, user_id)
        row = cursor.fetchone()
        user_pw = input("PW : ")
        if row[2] == user_pw:
            print("success login")
        else:
            print("False PW")
    except:
        print("None ID")    

def update_quiz():
    cursor = conn.cursor()
    quiz_name = input("quiz_name : ")       # 질문
    quiz_answer = input("quiz answer : ")   # 답
    sql = '''
    insert into quiz (quiz_name, quiz_answer)
        values (%s, %s)
    '''
    cursor.execute(sql, (quiz_name, quiz_answer))
    conn.commit()

num = input('1. sign up\n2. login\n3. update quiz\n4. Play quiz\n5. Logout\n')

if num == '1':
    sign_up()
elif num == '2':
    login()
elif num == '3':
    update_quiz()
elif num == '4':
    