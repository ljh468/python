#########################  조코딩 #########################

# 자료에 대한 타입
# 숫자, 문자, 불
# 자료구조 (자료를 담는 구조)
# 변수, 리스트, 튜플, 딕셔너리, 집합
a = 2
b = 4

print(a)

# 사칙연산
print("a+b=", a+b)
print("b-a=", b-a) 
print("a*b=", a*b)
print("b/a=", b/a) # 나머지값까지 출력
print("b//a=", b//a) # 나눈 몫 출력
print("b%a=",b%a) # 나머지 출력

# 문자열을 만드는 4가지방법
print("Hello world")
print('python is fun')
print("""Life is too short, you need python""")
print('''Life is too short, you need python''')

# 따옴표포함
print("python 's favorite food is perl")
print('python \'s favorite food is perl') # \ 붙이면 문자열로 인식
print("Life is too short, \nyou need python") # \n 붙이면 줄넘어감

# 인덱싱
a = "Life is too short, you need python"
print(a[0])
print(a[12])
print(a[-1])

# 슬라이싱
a = "Life is too short, you need python"
print(a[0:4])

# 포맷팅
a = "I eat %d apples." % 3
print(a)
number = 10
day = "three"
print("I ate %d apples, so I was sick %s days." % (number, day))

# Count
a = "habby"
print(a.count('b'))

# Find
a = "Python is best choice"
print(a.find('b'))
print(a.find('k'))

# Index
a = "Life is too short"
print(a.index('t'))
# print(a.index('k')) 없으면 Error

# Join
a = ","
print(a.join('abcd'))

# Upper
a = "hi"
print(a.upper())

# Lower
a = "Hi"
print(a.lower())

# Strip (앞뒤 공백제거)
a = "         hello         "
print(a.strip())

# replace
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# Split
a = "Life is too short"
print(a.split())
a = "a:b:c:d"
print(a.split(":"))

# 리스트 자료형
odd = [1,3,5,7,9]
hap = [1,2,["Life", "is"]]
print(odd[1])
print(hap[2][0])

# 리스트 인덱싱
a = [1,2,3]
print(a[0] + a[2])
print(a[-1])

# 리스트 슬라이싱
a = [1,2,3,4,5]
print(a[0:2])
print(a[2:])

# 리스트 수정
a = [0,1,2,3,1]
a[4] = 4
print(a)
a[0:1] = ['a','b','c']
print(a)

# 리스트 삭제
a = [1, 'a', 'b', 'c', 4]
a[1:3] = []
print(a)
del a[1]
print(a)

# append
a = [1,2,3]
print(a)
a.append(4)
print(a)

# sort
a = [1, 4, 3, 2]
print(a)
a.sort()
print(a)

# reverse
a = ['a', 'b', 'c']
a.reverse()
print(a)

# index
a = [1, 2, 3]
print(a.index(3))

# insert
a = [5,3,2,1]
a.insert(1,4)
print(a)

# remove (값을 제거)
a = [1,2,3,1,2,3]
a.remove(3)
print(a)

# pop (꺼내기)
a = [1,2,3]
print(a.pop())
print(a)

# count
a = [1,2,3,1]
print(a.count(1))

# extend ( 확장하기 )
a = [1,2,3,4]
a.extend([5,6])
print(a)

b = [7,8]
a.extend(b)
print(a)