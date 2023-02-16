def set_discount(order_count): # 세트 할인 2개 20% 3개 25% 4개 30%
    discount = 0
    if order_count == 2:
        discount = 0.2
    elif order_count == 3:
        discount = 0.25
    elif order_count >= 4:
        discount = 0.3
    return discount

def order_total(order_num, order_sum, order_discount): # 포장 1 매장 2 배달 3
    total = 0
    if order_num == 1:
        total = order_sum - order_discount - order_sum * 0.1
    elif order_num == 2:
        total = order_sum - order_discount
    elif order_num == 3:
        total = order_sum - order_discount + 8900
    return total


order_num = int(input("주문방법을 골라주세요\n1 : 포장 - 전체 금액애서 10% 할인\n2 : 매장 - 할인 없음\n3 : 배달 - 배달료 8900원 추가 청구\n"))
menu_info = {"김밥":2500, '참치김밥':3500, '돈가스김밥':3500,'고추참치김밥':3500,'소고기김밥': 4500,'치즈김밥' :3000,'셀러드김밥': 2500,'꼬마김밥' :1200,'충무김밥' :20000,'꽈리김밥' :3500,'진미김밥': 3700,
'라면': 4000,'치즈라면': 4500,'된장라면':4700,'떡라면' :4800,'만두라면': 4500,'떡만두라면': 5000,'카레라면': 4500,'해물라면': 5500,'짜장라면': 4200,'비빔라면': 4200,
'돈가스': 8000,'치즈돈가스': 9000,'고치돈': 10000,'등심돈가스': 7500,'안심돈가스': 7500,'피카츄돈가스': 500,'새우돈가스': 7500,'대왕돈가스': 12000,'치킨돈가스' :6000,
'함박스테이크' :9500,'해물된장찌개': 8500,'부대찌개' :7800,'떡볶이': 3000,'치즈떡볶이': 4500,'라볶이' :5000,'마약떡볶이': 99900,'컵떡볶이': 500,'우동': 3000,
'튀김우동': 4500,'김치우동' :4500,'유부우동' :4500,'육개장': 6000,'알탕': 7500,'갈비탕' :8000,'황태해장국' :7000,'순대국밥': 5500,'명태국밥' :7000,'공기밥': 1000}

order_sum = 0
order_count = 0
order_info = {}
# 메뉴 입력받기
print("메뉴를 입력하시고 다 고르셨으면 3을 입력해주세요.")
while True:
    menu = str(input(" Menu : "))
    if menu == str(3):
        break
    order_sum += menu_info.get(menu, 0)
    order_count += 1

    # 주문내역 딕셔너리 만들기
    order_info.update({menu:menu_info.get(menu, 0)})

print("주문 내역 : ", order_info)
print("메뉴 갯수 : ", order_count)
print("메뉴 합계 : ", order_sum)

order_discount = order_sum * set_discount(order_count)
print("할인 금액 : ", order_discount)

total = order_total(order_num, order_sum, order_discount)
print("총 금액 : ", total)

