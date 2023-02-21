import pymysql
import time
import random
import re

conn = pymysql.connect( 
host='127.0.0.1', user='root', password='wpdjvks1',
db='quiz', charset='utf8') # 데이터베이스 접속

loginId = ""

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
    if loginId != "":
        print('login on')
        return 
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
            loginId = user_id
            print("success login")
        else:
            print("False PW")
    except:
        print("None ID")    

def logout():
    if loginId == "":
        print("pls login")
        return
    loginId = ""
    print("logOut!")

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


def play():
    if loginId != "" :
        print("pls login")
    else:
        cursor = conn.cursor()
        sql = '''
        select * from quiz
        '''
        cursor.execute(sql)
        result = cursor.fetchall()
        Time = 0
        score = 0
        while True:
            start_time = time.time()
            random_num = random.randrange(0, len(result))
            quiz_name = result[random_num][1]
            quiz_answer = result[random_num][2]
            print(quiz_name)                    # 퀴즈 출력

            answer = input("answer : ")
            end_time = time.time()
            Time = Time + (end_time - start_time)
            if Time > 10 : 
                break
                
            if answer ==  quiz_answer:  
                print("correct") # 질문이 맞으면 correct 틀리면 not 
                score += 1
            else:
                print("not")

            print("남은 시간 : ", 10 - round(Time),'초')
        
        print("시간이 초과했습니다. 경과시간 = %d초" %round(Time))
        print("Score : %d" %score)
        # return score


def update_score(score, id):
    cursor = conn.cursor()
    sel = '''
    select user_score from user where user_id=%s
    '''
    cursor.execute(sel, id)
    lscore = cursor.fetchone()[0] # 기존의 스코어 가져오기
    
    sql = '''
    UPDATE user set user_score = %s where user_id = %s
    '''
    cursor.execute(sql, ((score+lscore), id)) # 스코어 누적하기
    conn.commit()
    
def rank():
    cursor = conn.cursor()
    sql = '''
    select user_score, user_id from user
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    sort = sorted(result, reverse=True)
    count = 1
    print("순위  아이디  점수")
    for i in sort:
        print('%-5d' %count, '%-7s' %i[1], i[0])
        count +=1
        if count == 6:
            break    
    print("")
        

while True :
    num = input('1. sign up\n2. login\n3. update quiz\n4. Play quiz\n5. Rank\n6. logout\n7. Exit\n')

    if num == '1':
        sign_up()
    elif num == '2':
        login()
    elif num == '3':
        update_quiz()
    elif num == '4':
        score = play()
        update_score(score, loginId)
    elif num == '5':
        rank()
    elif num == '6':
        logout()
    elif num == '7':
        break
    
