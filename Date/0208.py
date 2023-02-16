# 컴프리헨션 구구단
# ox = [i*j for i in range(2,10) for j in range(1,10)]
# print(ox)

# 노래 가사

# f = open("yesterday.txt", 'r')
# lyric = f.readline()
#
# result = [i for i in lyric]
#
# number = open("number.txt")
# a_lyric = number.readline()
#
# y_lyric = ""
# for line in lyric:
#     y_lyric += line.strip() + "\n"
#
# print(a_lyric)
#
# print(result[0])
# num = []
# lyric = [ord(j) for j in result]
# print(lyric)
# #
# a_lyric = [chr(n) for n in a_lyric]
# print(*a_lyric)

# -----------------------
# # 숫자값 입력받기
# number = open("number.txt")
# a_lyric = number.readline()
#
# # 텍스트 값 입력받기
# text = open("yesterday.txt")
# b_lyric = text.readline()
#
# # 숫자를 텍스트로 변경
# num_lyric = [chr(int(i)) for i in a_lyric.split()]
# print(num_lyric)
# for i in num_lyric:
#     print(i,end="")
# print("")
# print(*num_lyric)
#
# # 텍스트를 숫자로 변경
# chr_lyric = [ord(j) for j in b_lyric]
#
# print(chr_lyric)
# print(*chr_lyric)

# --------------------------
# class soccerplayer(object):
#     def __init__(self, name, position, back_number):
#         self.name = name
#         self.position = position
#         self.back_number = back_number
#
# ------------------------------------

