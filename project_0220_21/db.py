import pymysql
conn = pymysql.connect(
host='127.0.0.1', user='root', password='wpdjvks1',
db='quiz', charset='utf8')
cursor = conn.cursor()

sql = '''
SELECT * FROM quiz
'''

cursor.execute(sql)
result = cursor.fetchall()
# for row in result:
    # print(row[1])
    
quiz_name = result[0][1]
quiz_answer = result[0][2]
print(quiz_name)
print(type(quiz_answer))
answer = str(input("answer : "))
if answer == quiz_answer:
    print("correct")
else:
    print("not")
# print(quiz_answer)


cursor.close()
conn.close()