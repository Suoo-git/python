# def sum(lista):
#     result = 0
#     for i in lista:
#         result  += i
#     return result
#
# def ss(lista):
#     return sum(lista)
#
# def avg(listb):
#     return sum(listb) / len(listb)
#
# A = [1, 3, 4, 5, 6]
#
# print(sum(A))
# print(avg(A))
#
#
# def factorial(n):
#     if n==1 :
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(int(input("number?"))))
#
#
# f = open("yesterday (2).txt", 'r')
# y_lyric = f.readlines()
# f.close()
#
# contents = ""
# for line in y_lyric:
#     contents = contents + line.strip() + "\n"
#
# yes = contents.upper().count("YESTERDAY")
# print("number",yes)
#
#
# order_num = int(input())
#
# result = 100
# def order(order_num):
#     if order_num == 1:
#         result = result + result*0.1
#
# order()
# print(result)
#
# num = 0
# while num != 4:
#     num = int(input())
#     print("")

menu = str(input("메뉴를 입력하세요"))
menu_info = {"kim": 2500, 'cham': 3500}
order_info = {}
list = []
# print(menu_info[menu])
# list.append(menu_info["kim"])
# print(list)
order_info.update({menu:menu_info.get(menu)})
# order_info = menu_info.items()
print(order_info)