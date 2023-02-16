class Customer(object):
    def __init__(self, custid, name, address, phoneNum):
        self.__custid = custid
        self.name = name
        self.__address = address
        self.__phoneNum = phoneNum

    #Property 구현
    @property
    def custid(self):
        return self.__custid

    @property
    def address(self):
        return self.__address

    @property
    def phoneNum(self):
        return self.__phoneNum

    #자기소개 출력하는 함수 구현
    def introduce(self):
        print(f"내 이름은 {self.name},{self.__address},{self.__phoneNum}")