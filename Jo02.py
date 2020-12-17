#########################  조코딩 #########################
from copy import copy
# 튜플
# sample = (1,2,3) 구조
# 자물쇠( 고정된 자료구조, 수정불가)
# 변하지 않는 속성 ( 결합시 새로운 튜플을 생성 )
t1 = (1, 2, 'a', 'b')
# del t1[0] -> Error
print(t1[0])
print(t1[1:])

# 딕셔너리
# sample = {key, value} 구조, Json객체타입
# Key 값은 중복될 수 없다
a = {'name' : 'pey', 'phone' : '011999', 'birth' : '1118'}

# key값 출력
print(a.keys())

# value값 출력
print(a.values())

# 모두 출력
print(a.items())

# 값이 없어도 오류없이 뽑아내는 get
print(a.get('name'))

# Key값 존재확인
print('name' in a)
print('email' in a)

# a리스트 청소
a.clear()
print(a)

# 집합(Set)
# 집합에 관련된 자료형
# 중복이 허용되지 않음
# 순서가 없다
s1 = set([1,2,3,4,5,6])
print(s1)

s2 = set("Hello")
print(s2)

# 교집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2)
s1.intersection(s2)

# 합집합
print(s1 | s2)
s1.union(s2)

# 차집합
print(s1-s2)
s1.difference(s2)
print(s2-s1)
s2.difference(s1)

# 값 1개 추가
s1 = set([1,2,3])
s1.add(4)
print(s1)

# 값 여러개 추가
s1 = set([1,2,3])
s1.update([4,5,6])
print(s2)

# 특정값 제거 (remove)
s1 = set([1,2,3])
s1.remove(2)
print(s1)

# bolean자료형 (불)
# 참(True), 거짓(False)를 나타내는 자료형

if False : 
    print(a)
while False :
    a += 1

a = [1,2,3,4]
while a: # a가 존재하면 반복
    print(a.pop())

# 변수
# 파이썬에서 변수는 메모리 주소 값을 가리킨다.

a = [1,2,3]
b = a # a가 가리키는 주소값을 b에 넣는다
a[1] = 4
print(a)
print(b)
print(a is b)

a = [1,2,3]
b = copy(a) # a의 값을 넣는다
# b = a[:]
a[1] = 4
print(a)
print(b)