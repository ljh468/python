#########################  조코딩 #########################
## 조건문 (if)
money = True
if money:
    print("택시를 타고 가라")
    # 들여쓰기가 잘못되면 syntax Error
else:
    print("걸어가라")


# 비교 연산자
a = 1
b = 2
if a >= b:
    print("택시를 타고 가라")
else :
    print("걸어가라")

########################
money = 2000
if money >= 3000:
    print("택시를 타고가라")
else:
    print("걸어가라")

########################
# or 연산자
money = 2000
card = 1
if money >= 3000 or card == 1:
# if money >= 3000 | card == 1:
    print("택시를 타고가라")
else:
    print("걸어가라")

########################
# and 연산자
money = 2000
card = 1
if money <= 3000 and card == 0:
# if money <= 3000 & card == 0:
    print("택시를 타고가라")
else:
    print("걸어가라")

########################
# not 연산자
money = 2000
if not money >= 3000:
    print("돈이 부족합니다.")
else:
    print("돈이 3000원이상 있습니다.")

########################
# in 연산자
money = 2000

if 1 in [1,2,3]:
    print("1은 [1,2,3]에 포함한다")
    # pass 그냥 넘어가고 싶으면 pass를 넣어준다
else:
    print("포함되지 않는다")

########################
# 조건이 여러개일 경우 elif 연산자
pocket = ['paper', 'cellphone']
if 'money' in pocket:
    pass
elif 'card' in pocket:
    print("카드가 있습니다.")
else:
    print("돈이나 카드가 없습니다.")

########################
## 조건부 표현식 (3항 연산자)
# 조건문을 한줄로 간단하게 쓸수 있다.
score = 70
message = "success" if score >= 60 else "failure"
print(message)

########################
## 반복문 (while문)
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    # treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

# break 사용법 ( 반복문 탈출 )
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee: # coffee가 0이면 실행
        print("커피가 다 떨어졌습니다. 판매를 종료합니다.")
        break

# continue 사용법 ( 맨위로 이동)
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue # continue를 만나면 다시 while 위로 올라감
    print(a)

# 무한루프
# while True:
#    print("계속 반복합니다.")

########################
## 반복문 (for문)
# for each문 과 같다
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 튜플에서 for문
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first , last)

# 60점이 넘으면 합격이고 아니면 불합격
marks = [90, 25, 67, 45, 80]
number = 0

for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# for문 continue
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60: 
        continue
    print("%d번 학생은 합격입니다." % number)

# for문과 함께 사용하는 range함수
sum = 0
for i in range(1,11):
# 1이상 11미만까지 반복
    sum = sum + i
print(sum)

########################
## 이중 for문 (구구단)
for i in range(2, 10):
    for j in range(1,10):
        print(i*j, end=" ")
        # end=" "는 print함수의 옵션임
    print('')
    # 줄 바꿈

########################
## 리스트 내포(List comprehension)
a = [1,2,3,4,5]
result = [num * 3 for num in a]
# a리스트에 있는 값을 num에 빼서 3곱하여 result 리스트를 만들어라
print(result)

result = [num * 3 for num in a if num % 2 == 0]
print(result)
# result = []
# for num in a:
#   if num % 2 ==0:
#       result.append(num * 3)

result = [x * y for x in range(2, 10) for y in range(1, 10)]
print(result)
# result = []
# for x in range(2, 10):
#   for y in range(1, 10):
#       result.append(x*y)