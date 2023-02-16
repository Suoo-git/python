
# print("your age?")
# age = int(input())
# if age < 30:
#     print("welcome")
# else:
#     print("No")

## 음수 양수 비교
# print("number?")
# num = int(input())
# if (num%2) == 0:
#     print("짝수")
# else :
#     print("홀수")


##두 수의 크기 비교
# print("number 1")
# num1 = int(input())
# print("number 2")
# num2 = int(input())
#
# if num1 < num2:
#     print("num1 < num2")
# elif num1 > num2:
#     print("num1 > num2")
# else:
#     print("num1 = num2")


## 목욕탕 요금
# print("age?")
# age = int(input())
# price = 0
#
# if age < 7:
#     price =5000
# elif age < 60:
#     price=7000
# else:
#     price=6000

# # print("price = %d"%price)
# print(f"price = {price}")


##점수 결과
# print("grade?")
# grade = int(input())
#
# if grade >= 90: print("notebook")
# elif grade >= 80: print("money")
# elif grade >= 70: print("book")
# elif grade >= 60: print(":)")
# else: print(":(")
#
# print(f" my grade = {grade}")


## 세 수중 가장 큰 수
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# if num1 > num2:
#     if num1 > num3:
#         print("num1")
#     else:
#         print("num3")
# elif num2 > num3:
#     print("num2")
# else:
#     print("num3")


## 나이로 학생 찾기
# print("당신이 태어난 연도를 입력하세요.")
# birth_year = int(input())
# age = 2020 - birth_year + 1
#
# if 26 >= age >= 20:
#     print("대학생")
# elif 20 > age >= 17:
#     print("고등학생")
# elif 17 > age >= 14:
#     print("중학생")
# elif 14 > age >= 8:
#     print("초등학생")
# else:
#     print("학생이 아닙니다.")


# 주민번호로 성별과 나이 구하기
# print("number?")
# number = str(input())
# sex = int(number[-1])
# year = int(number[0:4])
#
# age = 2022 - year + 1
#
# if (sex%2) == 0:
#     print(f"성별은 여자이고 나이는 {age}입니다.")
# else:
#     print(f"성별은 남자이고 나이는 {age}입니다.")
#


# 숫자 찾기 게임
# import random
# number = random.randint(1, 100)
# print("숫자를 맞혀보세요")
# num = int(input())
# while number != num:
#     if number < num:
#         print("숫자가 너무 큽니다")
#     else:
#         print("숫자가 너무 작습니다")
#     num = int(input())
# print(f"정답입니다. 입력한 숫자는 {num}입니다.")
#


## 구구단
# for i in range(2,10):
#     for j in range(1,10):
#         result = i*j
#         print(f"{i} X {j} = {result} ", end="")
#     print("")


## 평균구하기
# kor_score = [49, 80, 20, 100, 80]
# math_score = [43, 60, 85, 30, 90]
# eng_score = [49, 82, 48, 50, 100]
# midterm_score = [kor_score, math_score, eng_score]
#
# avg_score = []
# for j in range(0, 5):
#     sum = 0
#     for i in range(0, 3):
#         sum += midterm_score[i][j]
#     avg = sum /3
#     avg_score.append(avg)
# print(avg_score)


# # 별찍기 1
# for j in range(0,5):
#     for i in range(0,j):
#         print("0",end="")
#     print("*")

# # 별찍기 2
# for i in range(0,5):
#     for j in range(0, 5 - i):
#         print("*", end="")
#     print("")

# #별찍기 3
# for i in range(1,6):
#     for n in range(0,5-i):
#         print(" ",end="")
#     for j in range(0, 2*i-1):
#         print("*", end="")
#     print("")

# # 별찍기 4
# for i in range(5,0,-1):
#     for n in range(0, 5-i):
#         print(" ",end="")
#     for j in range(0,i*2-1):
#         print("*",end="")
#     print("")

## 별찍기 5
# for i in range(1,6):
#     for n in range(0,5-i):
#         print(" ",end="")
#     for j in range(0, 2*i-1):
#         print("*", end="")
#     print("")
# for i in range(4,0,-1):
#     for n in range(0, 5-i):
#         print(" ",end="")
#     for j in range(0,i*2-1):
#         print("*",end="")
#     print("")

# for i in range(0, 4):
#     print(" " * (4-i) + '*' * (i*2+1))
# for i in range(0, 5):
#     print(" " * i + '*' * (9 - (2 * i)))


## 별찍기 6
# for i in range(7,0,-1):
#     for n in range(0, 7-i):
#         print(" ",end="")
#     for j in range(0,i*2-1):
#         print("*",end="")
#     print("")
# for i in range(1,8):
#     for n in range(0,7-i):
#         print(" ",end="")
#     for j in range(0, 2*i-1):
#         print("*", end="")
#     print("")

# 별찍기 5-2

# for i in range(4,0,-1):
#     for j in range(0,i):
#         print("0",end="")
#     print("*")


