# class Inventory(object):
#     def __init__(self):
#         self.__items = []
#     def add_new_item(self, product):
#         if type(product) == Product:
#             self.__items.append(product)
#             print("new item added")
#         else:
#             raise ValueError("Invalid Item")
#     def get_number_of_items(self):
#         return len(self.__items)
#
#     @property
#     def items(self):
#         return self.__items
#
#
# class Product(object):
#     pass
#
# my_inventory = Inventory()
# my_inventory.add_new_item(Product())
# items = my_inventory.items
# items.append(Product())
#
# # print(my_inventory.items)



import cx_Oracle

con = cx_Oracle.connect("madang", "madang", "127.0.0.1:1521", encoding="UTF-8")
cursor = con.cursor()
cursor.execute("select * from customer")
# out_data = cursor.fetchone()
out_data = cursor.fetchall()

print(out_data)

# customer_date = []
# for data in out_data:
#     customer_date.append(data)

#
for i in range(0,4):
    for j in range(0,4):
        print(out_data[i][j], end=" ")
    print("")

con.close()

class customer(object):
    def __init__(self, custid, name, adress, phoneNum):
        self.__custid = custid
        self.name = name
        self.__adress = adress
        self.__phoneNum = phoneNum

    def introduce(self):
        print(f"내 이름은 {self.name}이고 사는 곳은 {self.__adress}입니다.")

customer(1, "박지성", "영국 멘체스터", "000-5000-0001").introduce()



