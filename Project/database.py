
import cx_Oracle
from customer import Customer



#오라클 DB에 사용자 연결!
con = cx_Oracle.connect("madang", "madang", "127.0.0.1:1521", encoding="UTF-8")

cursor = con.cursor()
cursor.execute("select * from customer")
# out_data = cursor.fetchone()
out_data = cursor.fetchall()
con.close()

customers = [Customer(row[0], row[1], row[2], row[3]) for row in out_data]

# for row in out_data:
#     customers.append(Customer(row[0], row[1], row[2], row[3]))

#custmers List에서 custmomer 객체를 불러와서 함수 실행!
for customer in customers:
    if type(customer) == Customer:
        customer.introduce()



# print(out_data)

