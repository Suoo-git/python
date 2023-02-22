import pymysql
import time
import random
import re

conn = pymysql.connect( 
host='127.0.0.1', user='root', password='wpdjvks1',
db='quiz', charset='utf8') # 데이터베이스 접속

loginId = ""

# def disconn():
#     conn.close()

def sign_up(): 
    print("3~6글자의 영문 대소문자, 숫자의 조합으로 만들어 주세요")
    id = input("ID : ")
    reg = '^[A-Za-z0-9]{3,6}$' # id = 영문 대소문자 숫자 3자 이상 6자 이하로 한다.
    if not re.search(reg, id):
        print                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ("False id")
        return
    
    print("최소 한개의 영문자와 숫자를 포함하고 6자 이상 12자 이하로 만들어 주세요")
    pw = input("PW : ") 
    reg = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,12}$' # pw = 최소 한개의 영문자, 숫자와 6자 이상 12자 이하로 한다
    if not re.search(reg, pw):
        print("False pw")
        return
    
    try:    
        cursor = conn.cursor()
        sql = '''
        INSERT INTO user (user_id, user_score, user_pw, playTime)
        values (%s, %s, %s, %s)
        '''
        cursor.execute(sql, (id, 0, pw, 0))
    except pymysql.err.IntegrityError: #user_id -> unique index (중복 불허)
        print("\nError : duplciate ID\nretry\n")
    conn.commit()
    cursor.close()


def login():
    global loginId
    if loginId != "":
        print('\nlogin on\n')
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
            print("\nsuccess login\n")
        else:
            print("\nFalse PW\n")
    except:
        print("\nNone ID\n")    


def logout():
    global loginId
    if loginId == "":
        print("pls login\n")
        return
    loginId = ""
    print("logOut!\n")


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
    # global loginId
    if loginId == "" :
        print("pls login\n")
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
            if Time > 30 :      # 제한시간 설정
                break
                
            if answer ==  quiz_answer:  
                print("\nCorrect") # 질문이 맞으면 correct 틀리면 not 
                score += 1
            else:
                print("\nNot correct")

            print("남은 시간 : ", 30 - round(Time),'초\n')  # 제한시간
        
        print("시간이 초과했습니다. 경과시간 = %d초" %round(Time))
        print("Score : %d" %score)
        return score, Time


def update_score(score, time, id):
    cursor = conn.cursor()
    sel = '''
    select user_score, playTime from user where user_id=%s
    '''
    cursor.execute(sel, id)
    result = cursor.fetchone() # 기존의 스코어 가져오기
    lscore = result[0]
    lplayTime = result[1]
    sql = '''
    UPDATE user set user_score = %s, playTime = %s where user_id = %s
    '''
    cursor.execute(sql, ((score+int(lscore)), (time+lplayTime), id)) # 스코어 누적하기
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


def info():
    if loginId == "":
        print("pls login\n")
    else:    
        cursor = conn.cursor()
        sql = '''
        select * from user where user_id = %s
        '''
        cursor.execute(sql, loginId)
        result = cursor.fetchone()
        print("ID     score   playtime")
        print('%-6s' %result[0], '%-7s' %result[1], result[3],'\n')
        

while True :
    print('1. sign up\n2. login\n3. logout\n4. Play quiz\n5. Rank\n6. update quiz\n7. Info\n0. Exit\n')
    num = input('input number : ')
    if num == '1':
        sign_up()
    elif num == '2':
        login()
    elif num == '3':
        logout()
    elif num == '4':
        score, time = play()
        update_score(score, time, loginId)
    elif num == '5':
        rank()
    elif num == '6':
        update_quiz()
    elif num == '7':
        info()
    elif num == '0':
        break
    else:
        print("\nError number\n")
    
