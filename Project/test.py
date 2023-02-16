kimbap = {'김밥': 2500, '참치김밥': 3000, '돈가스김밥': 3500, "고추참치김밥": 3500,'소고기김밥': 4500,
               '치즈김밥': 3000, '샐러드김밥': 2500, '꼬마김밥': 1200, '충무김밥': 2000,'꽈리김밥': 3500, '진미김밥': 3700}

ramen = {'라면': 4000, '치즈라면': 4500, '된장라면': 4700, '떡라면': 4800, '만두라면': 4500 ,
         '떡만두라면': 5000, '카레라면': 4500, '해물라면': 5500, '짜장라면': 4200, '비빔라면': 4200}

katsu = {'돈가스': 8000, '치즈돈가스': 9000, '고구마치즈돈가스': 10000, '등심돈가스': 7500,'안심돈가스': 7500,
         '피카츄돈가스': 500, '새우돈가스': 7500, '대왕돈가스': 12000, '치킨돈가스': 6000, '함박스테이크': 9500 }

deopbab =  {'제육덮밥': 7000, '오무라이스': 7000, '하이라이스': 7000, '오징어덮밥': 7500,
            '짜장덮밥': 6500, '소고기덮밥': 8000, '카레덮밥': 6500, '돌솥비빔밥': 7000, '김치덮밥': 6500 }

jjigae = {'김치찌개': 6500, '된장찌개': 6500, '순두부찌개': 6500, '내장찌개': 6500, '해물된장찌개': 8500, '부대찌개': 7800}

tteokbokki = {'떡볶이': 3000, '치즈떡볶이': 4500, '라볶이': 5000, '마약떡볶이': 99900, '컵떡볶이': 500}

udong = {'우동': 3000, '튀김우동': 4500, '김치우동': 4500, '유부우동': 4500}

extra = {'육개장': 6000, '갈비탕': 8000, '황태해장국': 7000, '순대국밥': 5500,'명태국밥': 7000 , '공기밥': 1000}

#저장된 메뉴 호출
def menu(x):
    for key, value in x.items():
        print(key,value)

def menu_counter(x):
    cost = 0
    if x in kimbap.keys():
        cost += kimbap.get(x)
    elif x in ramen.keys():
        cost += ramen.get(x)
    elif x in katsu.keys():
        cost += katsu.get(x)
    elif x in deopbab.keys():
        cost += deopbab.get(x)
    elif x in jjigae.keys():
        cost += jjigae.get(x)
    elif x in tteokbokki.keys():
        cost += tteokbokki.get(x)
    elif x in udong.keys():
        cost += udong.get(x)
    elif x in extra.keys():
        cost += extra.get(x)
    else:
        print("그런 메뉴 없습니다.")
    return cost

def order_count(x, y):
    count.append(y)
    a = menu_counter(x)
    order_cost.append(a*y)

print("---"*6,"김밥 헤븐","---"*6)
print("---" * 4, "계속할 옵션을 선택하세요", "---" * 4)
print("  [0] : 종료", "  [1]:메뉴 주문", "  [2]:금액 조회")


for i in range(0, 10):
    cnt_list = []
    ord_list = []
    ord_sum = []
    count = []
    order_cost = []

    if i>=1:
        print("---" * 4, "계속할 옵션을 선택하세요", "---" * 4)
        print("  [0] : 종료", "  [1]:메뉴 주문", "  [2]:금액 조회")
    opt_Num = int(input())
    while opt_Num == 0:
        print("종료합니다.")
        exit()

    if i <= 0:
        print("------김밥류------")
        menu(kimbap)
        print("------라면류------")
        menu(ramen)
        print("-----돈가스류------")
        menu(katsu)
        print("------덮밥류------")
        menu(deopbab)
        print("------찌개류------")
        menu(jjigae)
        print("-----떡볶이류------")
        menu(tteokbokki)
        print("------우동류------")
        menu(udong)
        print("------기타류------")
        menu(extra)
    else:
        continue

    while opt_Num == 1:
        ord_Menu, ord_cnt = input("주문할 메뉴와 수량을 입력하세요 ex) 김밥 2 : ").split()
        ord_cnt = int(ord_cnt)
        cnt_list.append(ord_cnt)
        ord_list.append(ord_Menu)
        order_count(ord_Menu,ord_cnt)

        print("[0]: 매장 식사 ", "[1]: 포장", "[2]: 배달")
        user_input = int(input())
        for j in range(0, len(cnt_list)):
            sum = 0
            if user_input == 0:  # 매장
                sum =+ order_cost[j]
                ord_sum.append(sum)
            elif user_input == 1:  # 포장
                sum =+ order_cost[j] * 0.9
                ord_sum.append(sum)
            elif user_input == 2:  # 배달
                sum =+ (order_cost[j] + 8900)
                ord_sum.append(sum)

        order_input= input(" 추가로 주문 할까요? [y/n] ")
        if order_input == 'y':
            continue

        elif order_input == 'n':
            print(f"주문한 메뉴 : {ord_list}, 갯수 : {cnt_list}, 매장 포장 배달 적용가 : {ord_sum}")
            break

    while opt_Num == 2:
        a = sum(ord_sum)
        print(f"매출의 총합은 {a}입니다.")
        exit()