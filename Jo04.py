# 함수
# 입력과 출력
def sum(a,b):
    result = a + b
    return result

# 호출
print(sum(1,2))

# 입력값이 없는 함수
def say():
    return 'HI'
print(say())

# 결과값이 없는 함수
def sum2(a,b):
    print("%d, %d의 합은 %d입니다" % (a,b,a+b))
sum2(1,2)

# EX
myList = [1,2,3]
myList.append(4) # return값이 없는 append함수
print(myList)
print(myList.pop()) # return값이 있는 pop함수

# 여러 개의 입력값
def sum_many(*args): # 여러개의 인자를 한번에 받기위해 *args를 사용
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3,4,5))

# 딕셔너리 형태의 여러개의 입력값
def print_kwargs(**kwargs): # 딕셔너리의 형태를 처리할수 있는 매개변수
    for k in kwargs.keys():
        if (k == "name"):
            print("당신의 이름은 : " + k)
print(print_kwargs(name="조수", b="2"))

# 함수의 결과값은 언제나 하나이다.
def sum_and_mul(a,b):
    return a+b, a*b
print(sum_and_mul(1,2))
print(sum_and_mul(1,2)[0]) # 더한값만 사용

# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True): # man은 기본값을 True로 설정
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.") 
    else:
        print("여자입니다.")

print(say_myself("이재훈", 27, True))
print(say_myself("이재훈", 27))
print(say_myself(old=27, name="이선영", man=False))

# 함수 안에서 선언된 변수의 효력범위
a = 1
def vartest(a):
    a = a + 1  # 함수안의 임시변수
vartest(a)
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는방법
a = 1
def vartest2(a):
    a = a + 1  # 함수안의 지역변수
    return a
a = vartest2(a)
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는방법2
a = 1
def vartest3():
    global a  # 전역변수로 선언
    a = a + 1

vartest3()
print(a)

## Lambda 함수 ( 함수를 간단히 표현하는 방법 )
## list안에서 함수 적용가능

# 일반함수
def add2(a,b):
    return a + b
# 람다함수
add = lambda a, b: a+b

result = add(3, 4)
print(result)

# 리스트안에 함수를 넣을수있음
myList = [lambda a,b: a+b, lambda a,b: a*b]
print(myList[1](1,2))

## 사용자 입력과 출력
# 내장함수 input
# number = input("숫자를 입력하세요 : ")
# print(number)

# 내장함수 print
print("Life" "is" "too short")
print("Life", "is", "too short") # 띄어쓰기 적용

# 반복문 출력에서 글자 사이에 넣기위한 end옵션
for i in range(10):
    print(i, end=' ')
print()
## 파일 읽고 쓰기
# 파일 생성하기
# w는 쓰기모드, r은 읽기모드, a는 추가모드
# f = open("새파일.txt", "w")
# f.close()

# 파일을 쓰기모드로 열어 출력값 적기
f = open("C:/python/새파일.txt", 'w', encoding="UTF-8") # 파일이 있으면 지우고 다시 쓰는
# 만약 파일에 내용을 추가 하려면 'a'옵션으로 변경
for i in range(1, 11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()

# 파일에서 한줄씩 읽는 readline() 함수
f = open("c:/python/새파일.txt", 'r', encoding="UTF-8")
line = f.readline()
print(line)
f.close()

# 파일의 여러줄 읽기
f = open("c:/python/새파일.txt", 'r', encoding="UTF-8")
while True:
    line = f.readline()
    if not line: break # line이 없으면
    print(line)
f.close()

# 파일에서 여러줄을 리스트형태로 가져오는 readlines() 함수
f = open("새파일.txt", 'r', encoding="UTF-8")
lines = f.readlines()
for line in lines:
    print(line.strip("\n"), end=" ")
f.close()
print()
# 파일을 전부 불러오는 read() 함수
f = open("새파일.txt", 'r', encoding="UTF-8")
data = f.read()
print(data)
f.close()

# with문과 함께 사용하기
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")