contents = {'이상복의 인생은 무엇인가': '이상복', '감독님 농구가 하고십어요': '이상복', '아복타2': '이상복',
            '코딩의 길': '이상복', '인공지능은 무엇인가': '이상복', '빅데이터와 한전': 'KEPCO'}


view_count = 1 #기본 시청 횟수 1

old_contents = {}
# 컨텐츠 등록 함수, 등록시 카운트 +1(return 1)
def register_content(contents, title, creator):
    contents.update({title:creator})
    return 1

# 컨텐츠 딕셔너리 출력 함수
def contents_add(name):
    for key, value in name.items():
        print(key, ":", value)

# 컨텐츠 시청 - 시청목록 딕셔너리 추가 및 구구단 출력
def watch_content(contents, old_contents, title):
    if title in contents:
        old_contents.update({title: contents.get(title)})
        for i in range(1, 10):
            for j in range(2, 10):
                print(f"{i} * {j} = {i * j} ", end="")
            print("")
        return -1
    else:
        print("해당되는 컨텐츠가 없습니다.")
        return 0

while True:
    print("\n1 : 컨텐츠 신규등록\n2 : 컨텐츠 조회\n3 : 컨텐츠 시청\n4 : 사용가능한 대여횟수 조회\n5 : 시청한 컨텐츠 리스트\n0 : 종료")
    number = int(input("사용하실 기능의 번호를 입력해주세요 : "))
    # 컨텐츠 신규등록
    if number == 1:
        title = str(input("컨텐츠제목을 입력하세요 : "))
        creator = str(input("등록자 이름을 입력하세요 : "))
        view_count += register_content(contents, title, creator)

    elif number == 2:
        contents_add(contents)

    # 컨텐츠 시청
    elif number == 3:
        # 시청한 컨텐츠 목록 추가
        if view_count > 0:
            watch_name = str(input("시청할 컨텐츠 제목을 입력해주세요 : "))
            view_count += watch_content(contents, old_contents, watch_name)
        else :
            print("사용가능한 대여횟수가 없습니다. 컨텐츠를 신규등록해주세요")

            # 사용가능한 대여횟수 조회
    elif number == 4:
        print(f"\n사용가능한 대여횟수 = {view_count}")


    elif number == 5:
        print("\n시청한 컨텐츠 목록 ")
        print("----------------")
        contents_add(old_contents)

    elif number == 0:
        break


