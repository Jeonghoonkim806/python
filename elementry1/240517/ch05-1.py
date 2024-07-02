# 클래스 학습

result = 0
def add(num):
    global result
    result =+ num # 결과값(result)에 입력값(num) 더하기
    return result # 결과값 리턴

print(add(3)) # 0 + 3 -> 3
print(add(4)) # 3 + 4 -> 7

result2 = 0
def add1(num):
    global result2
    result2 += num

# calculator3.py
# calculator클래스 생성

class Calculator:
    def __init__(self):      # 생성자와(변수를 초기화) 비슷한 역할
        self.result = 0      # result변수를 0으로 초기화
    
    def add(self, num):      # add 일반함수
        self.result = self.result + num
        return self.result
    
cal1 = Calculator()  # 객체 생성(실제 붕어빵)하여 cal1변수에 대입
cal2 = Calculator()  # 객체 생성(실제 붕어빵)하여 cal2변수에 대입

a = cal1.add(3) # class Calculator안에 있는 addd함수를 호출
print(a)    