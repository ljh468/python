#########################  조코딩 #########################
# Immutable ( 변하지 않는 자료형 )
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

# Mutable ( 변하는 자료형 )
b = [1,2,3]
def vartest2(b):
    b = b.append(4)

vartest2(b)
print(b)

## 클래스, 모듈, 패키지, 예외처리, 내장함수, 외장함수

########################
## 클래스
# 반복되는 변수 & 메서드(함수)를 미리 정해놓은 틀(설계도)
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# 계산기
class FourCal:
        # __init__를 선언하면 무조건 맨 처음 실행된다 (생성자)     
    def __init__(self, first, second):
        self.first = first
        self.second = second
              # self는 객체가 들어간다
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result    
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(1,2) # 생성자로인해 바로 담아서 사용할 수 있다
print(a.first)
print(a.second)
print(a.add())

########################
## 상속
# 자식클래스가 우선순위
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

# 함수(메서드) 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second        

a = MoreFourCal(4, 2)
print(a.add())
print(a.pow())

b = SafeFourCal(4, 0)
print(b.div())

########################
# 클래스 변수
# 클래스 안에서 변수를 미리 정의할수 있다
class FourCal2:
    first = 2
    second = 3
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a2 = FourCal2()
print(a2.first)
b2 = FourCal2()
print(b2.first)

# 클래스에 미리 선언한 변수 -> 클래스 변수
class Family:
    lastname = "김"

Family.lastname = "박" # 설계도를 변경
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

########################
## 모듈이란? = 미리 만들어 놓은 .py파일 ( 함수, 변수, 클래스 )
import mod1
from mod1 import add  
# # mod1모듈에서 add만 사용
print(mod1.add(1,2))

# import할 모듈이 같은 폴더안에 없을때는 경로를 설정해야한다.
import sys
sys.path.append("c:/python") # 경로 설정
import mod1
print(mod1.sub(4,2))

########################
## 패키지란? 모듈을 여러개 모아 놓은것
# __init__.py파일은 패키지를 구성할때 패키지관련 설정하는곳

# 패키지 안의 함수 실행하기
import game.sound.echo
game.sound.echo.echo_test()

from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test as e
e()

########################
## __all__ 정의
from game.sound import *
# init파일에서 __all__ = ['echo']을 설정하여 가져올모듈을 설정해야함
echo.echo_test()

########################
## 예외처리
# 오류가 발생했을때 어떻게 할지 미리 정해놓는것

try: # 오류가 발생할 수 있는 구문
    4/0
except ZeroDivisionError as e: # 오류 발생
    print(e)
    
# 예외처리 구문이 있으면 프로그램이 꺼지지않음
print("예외처리 되었습니다.")

########################
## 예외처리 2
try:
    f = open('none', 'r')
except FileNotFoundError as e:
    print(str(e))

# 파일이 열리면
else:
    data = f.read()
    print(data)
    f.close()

########################
## 예외처리 3
f = open('foo.txt', 'r')
try:
    # 무언가를 수행한다.
    data = f.read()
    print(data)
    print("ddd")
except Exception as e:
    print(e)
finally:
    f.close()

########################
## 여러개의 예외처리
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")

## 오류를 패스하기
try:
    f = open("없는파일", 'r')
except FileNotFoundError:
    pass

########################
## 오류를 일부로 발생시키기
# 자식 함수로 변형해서 사용하고싶을때 사용
# 인터페이스 개념
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()

########################
## 내장함수 ( 이미 만들어져있는 함수 )

# 절대값
print(abs(-3))
# all 모두 참인지 검사
print(all([1,2,3]))
print(all([1,2,3,0]))
# any 하나라도 참이 있는지 검사
print(any([0,1,2]))
# chr ASCII코드를 입력받아 문자 출력
# ASCII코드는 0~127사이의 숫자를 각 문자에 대응
print(chr(97))
print(chr(65))
print(chr(48))
# dir 자체적으로 가지고 있는 변수나 함수를 보여줌
print(dir([1,2,3]))
print(dir({'1' : 'a'}))
# divmod 몫과 나머지를 튜플 형태로 돌려줌
print(divmod(7,3))
print(divmod(1.3, 0.2))
# enumerate 열거하다
# 인덱스랑 value형태로 보여줌
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval 실행 후 결과값을 돌려줌
print(eval('1+2'))
print(eval("'hi'+'a'"))

# filter 함수를 통과하여 참인 것만 돌려줌
def positive(x):
    return x > 0
a = list(filter(positive, [1,-3, 2, 0, -5, 6]))
print(a)
# id 주소값을 찾음
a = 3
id(3)
# int 10진수 정수 형태로 변환
print(int('3'))
print(int(3.4))
print(int('11', 2))
print(int('1A', 16))
# len 길이를 찾음
print(len("python"))
print(len([1,2,3]))
# list 리스트로 변환
print(list("python"))
a = [1,2,3]
b = list(a)
print(b)
## map 각요소가 수행한 결과를 보여줌
def two_times(x): return x*2
a = list(map(two_times, [1,2,3,4]))
print(a)

a = list(map(lambda a: a*2, [1,2,3,4]))
print(a)
# max 최대값
print(max([1,2,3]))
print(max("python"))
# min 최소값
print(min([1,2,3]))
print(min("python"))
# open 파일을 열때 사용
# f = open("binary_file", "rb")

# pow 제곱한 결과값반환
print(pow(2, 4))
print(pow(3, 3))
# range 범위
print(list(range(5)))
print(list(range(1, 10, 2)))
# round 반올림
print(round(4.6))
print(round(5.678, 2))
# sorted 정렬
print(sorted([3, 1, 2]))
print(sorted("zero"))
# str 문자열 반환
print(str(3))
print(str('hi'.upper()))
# tuple 튜플로 변환
print(tuple("abc"))
print(tuple([1,2,3]))
# type 타입을 출력
print(type("abc"))
print(type([1,2,3]))
# zip 자료형을 묶어주는 역할
print(list(zip([1,2,3], [4,5,6])))

########################
## 외장함수 ( 라이브러리 함수, import해서 쓰는함수 )
# argv_text.py
import sys
print(sys.argv)

# pickle 딕셔너리파일로 저장하고 꺼내올수있음
import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)

# time (파일생성일자 비교할때 쓰임)
import time
print(time.time())
# 1970년 1월 1일 기준으로 지난 시간초

# time,sleep
import time
for i in range(5):
    print(i)
    # time.sleep(1) # 1초텀을 두고 실행

# random 난수 생성
import random
print(random.random())
# 0~1 사이의 난수
lotto = sorted(random.sample(range(1, 46), 6))
print(lotto)

# webbrowser 웹페이지를 열어줌
import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")